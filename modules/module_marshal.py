import marshal
import types
import time
from typing import Any, Dict
from pathlib import Path
import pickle

"""
While pickle is generally preferred for object serialization, marshal can be useful for:
- Caching compiled expressions/functions
- Fast serialization of simple Python objects (int, float, str, bytes, dict, list, set, tuple)
- Performance-critical scenarios with trusted data
- Reading/writing bytecode (.pyc files) directly

WARNING: marshal is NOT secure - only use with trusted data sources.
"""


# Caching Compiled Code Objects for Performance
def cache_compiled_expression(expression: str, cache_path: Path) -> types.CodeType:
    """
    Compile and cache a Python expression for repeated evaluation.

    Use case: BI dashboards with complex calculated metrics that don't change.

    Args:
        expression: Python expression as string (e.g., "revenue * 0.15 + fixed_cost")
        cache_path: Path to store the compiled bytecode

    Returns:
        Compiled code object ready for eval()

    Example:
        >>> code = cache_compiled_expression("price * quantity * 1.08", Path("tax_calc.pyc"))
        >>> result = eval(code, {"price": 100, "quantity": 5})
    """
    if cache_path.exists():
        # Load from cache - much faster than recompiling
        with open(cache_path, "rb") as f:
            return marshal.load(f)

    # Compile and cache
    code_obj = compile(expression, "<string>", "eval")
    with open(cache_path, "wb") as f:
        marshal.dump(code_obj, f)

    return code_obj


# Fast Serialization of Configuration Data
def save_config_fast(config: Dict[str, Any], filepath: Path) -> None:
    """
    Serialize configuration dictionaries with marshal for faster I/O.

    Use case: Saving pipeline configurations, database connection params, or ETL job metadata when performance matters.

    Args:
        config: Dictionary containing only marshal-supported types
        filepath: Where to save the marshalled data

    Note:
        Supports: None, int, float, complex, str, bytes, bytearray, tuple, list, set, frozenset, dict, and code objects.
        Does NOT support custom classes or functions.
    """
    with open(filepath, "wb") as f:
        marshal.dump(config, f)


def load_config_fast(filepath: Path) -> Dict[str, Any]:
    """
    Args:
        filepath: Path to marshalled configuration

    Returns:
        Configuration dictionary

    Raises:
        ValueError: If file is corrupted or version mismatch
    """
    try:
        with open(filepath, "rb") as f:
            return marshal.load(f)
    except ValueError as e:
        raise ValueError(f"Marshal file incompatible or corrupted: {e}")


# Versioning Support
def save_with_version(data: Any, filepath: Path, version: int = 4) -> None:
    """
    Use case: When deploying across different Python versions in distributed systems.

    Args:
        data: Object to serialize
        filepath: Output path
        version: Marshal version (0-4). Use 4 for Python 3.4+

    Note:
        Version 4 is most compact and efficient for Python 3.4+
        Lower versions provide backward compatibility
    """
    with open(filepath, "wb") as f:
        marshal.dump(data, f, version)


# Performance Comparison Helper
def benchmark_serialization(data: Dict[str, Any], iterations: int = 1000) -> Dict[str, float]:
    """
    Compare marshal vs pickle performance for your specific data.

    Args:
        data: Sample data to benchmark
        iterations: Number of serialization cycles

    Returns:
        Dictionary with timing results
    """

    results = {}

    # Marshal benchmark
    start = time.perf_counter()
    for _ in range(iterations):
        serialized = marshal.dumps(data)
        _ = marshal.loads(serialized)
    results["marshal_time"] = time.perf_counter() - start
    results["marshal_size"] = len(marshal.dumps(data))

    # Pickle benchmark
    start = time.perf_counter()
    for _ in range(iterations):
        serialized = pickle.dumps(data)
        _ = pickle.loads(serialized)
    results["pickle_time"] = time.perf_counter() - start
    results["pickle_size"] = len(pickle.dumps(data))

    results["speedup"] = results["pickle_time"] / results["marshal_time"]

    return results


# Metric Calculation Cache
class MetricCalculator:
    """
    Cache compiled metric formulas for a BI dashboard.

    Use case: Dashboard with 100+ KPIs that are evaluated thousands of times.
    Compiling once and caching with marshal provides significant speedup.
    """

    def __init__(self, cache_dir: Path):
        """
        Args:
            cache_dir: Directory to store compiled metric formulas
        """
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)
        self._compiled_metrics: Dict[str, types.CodeType] = {}

    def register_metric(self, metric_name: str, formula: str) -> None:
        """
        Register a metric formula and compile/cache it.

        Args:
            metric_name: Unique identifier for the metric
            formula: Python expression (e.g., "(revenue - cost) / revenue")
        """
        cache_file = self.cache_dir / f"{metric_name}.pyc"
        self._compiled_metrics[metric_name] = cache_compiled_expression(
            formula, cache_file
        )

    def calculate(self, metric_name: str, context: Dict[str, Any]) -> float:
        """
        Calculate metric value using cached compiled code.

        Args:
            metric_name: Name of registered metric
            context: Dictionary with variable values (e.g., {"revenue": 1000, "cost": 600})

        Returns:
            Calculated metric value
        """
        if metric_name not in self._compiled_metrics:
            raise ValueError(f"Metric '{metric_name}' not registered")

        return eval(self._compiled_metrics[metric_name], {}, context)


# Supported Types Reference
def demonstrate_supported_types() -> None:
    """
    Demonstrate all types that marshal supports.
    Helpful for troubleshooting serialization errors.
    """
    supported_examples = {
        "none": None,
        "bool": True,
        "int": 42,
        "float": 3.14159,
        "complex": complex(1, 2),
        "str": "Hello, World!",
        "bytes": b"binary data",
        "bytearray": bytearray(b"mutable binary"),
        "tuple": (1, 2, 3),
        "list": [1, 2, 3],
        "set": {1, 2, 3},
        "frozenset": frozenset({1, 2, 3}),
        "dict": {"key": "value", "nested": {"a": 1}},
    }

    for type_name, example in supported_examples.items():
        try:
            serialized = marshal.dumps(example)
            # deserialized = marshal.loads(serialized)
            _ = marshal.loads(serialized)
            print(f"✓ {type_name}: {type(example).__name__} - Success")
        except ValueError as e:
            print(f"✗ {type_name}: Failed - {e}")


if __name__ == "__main__":
    # Metric Calculator for BI Dashboard
    print("=== BI Metric Calculator Dashboard Demo ===")
    calc = MetricCalculator(Path("./metric_cache"))

    # Register business metrics
    calc.register_metric("gross_margin", "(revenue - cost) / revenue * 100")
    calc.register_metric("roi", "(revenue - investment) / investment * 100")

    # Calculate metrics with real data
    data = {"revenue": 150000, "cost": 90000, "investment": 50000}
    print(f"Gross Margin: {calc.calculate('gross_margin', data):.2f}%")
    print(f"ROI: {calc.calculate('roi', data):.2f}%")

    # Performance comparison
    print("\n=== Performance Benchmark ===")
    test_data = {
        "metrics": list(range(1000)),
        "config": {"host": "localhost", "port": 5432, "timeout": 30},
        "values": [float(x) for x in range(100)],
    }
    results = benchmark_serialization(test_data)
    print(f"Marshal: {results['marshal_time']:.4f}s, {results['marshal_size']} bytes")
    print(f"Pickle: {results['pickle_time']:.4f}s, {results['pickle_size']} bytes")
    print(f"Speedup: {results['speedup']:.2f}x")

    print("\n=== Supported Types Demo ===")
    demonstrate_supported_types()
