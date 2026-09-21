"""
Task: score a password's strength, and generate one that scores well.
Grow a function into a class, into a module, into a package.

Run it (from the repo root):
    python -m use_cases.developing_a_function --check "correct horse battery"
    python -m use_cases.developing_a_function --make 3 --length 20

Why -m: `python use_cases/developing_a_function.py` puts use_cases/ on sys.path, not the
repo root, so `from . import x` fails. -m runs from the current directory as a package, so
relative and absolute imports both work. Dotted name, no ".py", every folder needs __init__.py.
"""

from __future__ import annotations

import argparse
import math
import secrets
import string
from dataclasses import dataclass
from typing import Sequence

POOLS = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digit": string.digits,
    "symbol": "!@#$%^&*-_=+?",
}


# --- STAGE 1: one function ---------------------------------------------------------------
# Works, but scoring, judging and printing are welded together: no way to test it, reuse the
# score, or change the rules without editing the middle of it.


def stage1_check(password: str) -> None:
    pool = sum(
        len(chars) for chars in POOLS.values() if any(c in chars for c in password)
    )
    bits = len(password) * math.log2(pool or 1)
    print(f"{password!r}: {bits:.0f} bits")
    if len(password) < 12:
        print("  too short")
    if bits < 60:
        print("  weak")


# --- STAGE 2: small functions ------------------------------------------------------------
# One job each, values in and values out, nothing prints. Now each piece is testable alone:
#     assert entropy_bits("aaaa") < entropy_bits("aA1!aA1!")


def pools_used(password: str) -> list[str]:
    return [name for name, chars in POOLS.items() if any(c in chars for c in password)]


def entropy_bits(password: str) -> float:
    """Rough strength: how many bits a brute-forcer faces given the character classes used."""
    pool = sum(len(POOLS[name]) for name in pools_used(password))
    return len(password) * math.log2(pool) if pool else 0.0


def weaknesses(
    password: str, min_length: int = 12, required: Sequence[str] = tuple(POOLS)
) -> list[str]:
    found = pools_used(password)
    problems = [f"missing {name}" for name in required if name not in found]
    if len(password) < min_length:
        problems.insert(0, f"shorter than {min_length}")
    return problems


def verdict(bits: float) -> str:
    return "strong" if bits >= 80 else "fair" if bits >= 60 else "weak"


def format_report(password: str, problems: Sequence[str]) -> str:
    bits = entropy_bits(password)
    detail = "; ".join(problems) or "no issues"
    return f"{password!r}  {bits:>5.0f} bits  {verdict(bits):<6} {detail}"


# --- STAGE 3: a class --------------------------------------------------------------------
# min_length and required were getting re-passed on every call, and generate() needs the same
# settings to build a password that would pass. The class holds the policy; the stage 2
# functions still do the work. One method plus __init__ would mean you didn't need a class.


@dataclass(frozen=True)
class Policy:
    min_length: int = 12
    required: tuple[str, ...] = tuple(POOLS)

    def check(self, password: str) -> list[str]:
        return weaknesses(password, self.min_length, self.required)

    def report(self, password: str) -> str:
        return format_report(password, self.check(password))

    def generate(self, length: int | None = None) -> str:
        """Pick one char from each required pool, fill the rest, then shuffle."""
        length = max(length or self.min_length, len(self.required))
        chars = [secrets.choice(POOLS[name]) for name in self.required]
        everything = "".join(POOLS[name] for name in self.required)
        chars += [secrets.choice(everything) for _ in range(length - len(chars))]
        return "".join(secrets.SystemRandom().sample(chars, len(chars)))


# --- STAGE 4: a module -------------------------------------------------------------------
# Importing this file does nothing; shell behavior lives in main(argv) -> exit code, so tests
# can call main(["--check", "tracmalloc5"]). Exit 1 on a failing password makes it scriptable.


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m use_cases.developing_a_function")
    parser.add_argument("--check", metavar="PASSWORD", help="score a password")
    parser.add_argument("--make", type=int, metavar="N", help="generate N passwords")
    parser.add_argument("--length", type=int, default=16)
    args = parser.parse_args(argv)

    policy = Policy(min_length=args.length)
    if args.make:
        for _ in range(args.make):
            print(policy.report(policy.generate()))
        return 0
    if args.check:
        print(policy.report(args.check))
        return 1 if policy.check(args.check) else 0

    stage1_check("tracmalloc5")  # stage 1
    print(format_report("tracmalloc5", weaknesses("tracmalloc5")))  # stage 2
    print(policy.report(policy.generate()))  # stage 3
    return 0


# --- STAGE 5: a package ------------------------------------------------------------------
# Split when parts change for different reasons (rules churn, entropy math doesn't), or when
# another project needs to import it. Nothing is rewritten; files move and imports get dots.
#
#   passcheck/
#   ├── pyproject.toml         [project.scripts] passcheck = "passcheck.cli:main"
#   ├── passcheck/
#   │   ├── __init__.py        from .policy import Policy   + __all__   (the public API)
#   │   ├── __main__.py        from .cli import main; raise SystemExit(main())
#   │   ├── pools.py           POOLS, pools_used
#   │   ├── strength.py        entropy_bits, verdict, weaknesses   (from .pools import POOLS)
#   │   ├── policy.py          Policy, format_report              (from .strength import ...)
#   │   └── cli.py             main(argv)                         (from .policy import Policy)
#   └── tests/test_strength.py
#
# Imports flow one way: pools <- strength <- policy <- cli. Siblings import relatively, which
# is exactly why you then run `python -m passcheck --make 3`, never `python passcheck/cli.py`.
# After `pip install -e .` the same code is a `passcheck` command from any directory.

if __name__ == "__main__":
    raise SystemExit(main())
