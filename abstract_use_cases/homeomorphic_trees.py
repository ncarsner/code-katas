import itertools


def get_canonical_form(adj, u, p=-1):
    child_forms = []
    for v in adj[u]:
        if v != p:
            child_forms.append(get_canonical_form(adj, v, u))
    return "(" + "".join(sorted(child_forms)) + ")"


def get_tree_hash(edges, n):
    adj = [[] for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Check connectivity
    visited = [False] * n
    stack = [0]
    visited[0] = True
    while stack:
        curr = stack.pop()
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    if not all(visited):
        return None, None

    # Find center(s)
    leaves = [i for i in range(n) if degree[i] == 1]
    count, deg_copy = n, list(degree)
    while count > 2:
        count -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            for neighbor in adj[leaf]:
                deg_copy[neighbor] -= 1
                if deg_copy[neighbor] == 1:
                    new_leaves.append(neighbor)
        leaves = new_leaves

    thash = min(get_canonical_form(adj, c) for c in leaves)
    return thash, adj


def draw_legal_tree(adj, u, p=-1, level=0, index=1, prefix="", is_last=True):
    """
    Renders tree with ASCII branches and Legal Style markers:
    - Root: *
    - Level 1: 1, 2, 3...
    - Level 2+: a, b, c...
    """
    # 1. Determine Marker
    if level == 0:
        marker = "*"
    elif level == 1:
        marker = str(index)
    else:
        marker = chr(97 + (index - 1) % 26)

    # 2. Build the current line
    if level == 0:
        line = f"{marker} ({u})\n"
    else:
        connector = "└── " if is_last else "├── "
        line = f"{prefix}{connector}{marker} ({u})\n"

    # 3. Recurse children
    new_prefix = prefix + ("    " if is_last else "│   ")
    children = sorted([v for v in adj[u] if v != p])
    result = line
    for i, v in enumerate(children):
        result += draw_legal_tree(
            adj, v, u, level + 1, i + 1, new_prefix, i == len(children) - 1
        )
    return result


def solve_and_print(n):
    if n == 3:
        print(f"n={n}: No homeomorphic irreducible trees exist (requires degree 2).")
        return

    target_sum = 2 * n - 2
    # Irreducible constraint: exclude degree 2
    possible_degrees = [1] + list(range(3, n))
    valid_sequences = [
        sorted(seq, reverse=True)
        for seq in itertools.combinations_with_replacement(possible_degrees, n)
        if sum(seq) == target_sum
    ]

    unique_hashes = set()
    tree_count = 0

    def backtrack(u, current_degrees, edges):
        nonlocal tree_count
        if tree_count >= 10:
            return

        if len(edges) == n - 1:
            thash, adj = get_tree_hash(edges, n)
            if thash and thash not in unique_hashes:
                unique_hashes.add(thash)
                tree_count += 1
                print(f"\n--- Design {tree_count} ---")
                # Root at 0 for visual consistency
                print(draw_legal_tree(adj, 0))
            return

        if u >= n:
            return

        for v in range(u + 1, n):
            if current_degrees[u] > 0 and current_degrees[v] > 0:
                current_degrees[u] -= 1
                current_degrees[v] -= 1
                edges.append((u, v))
                backtrack(
                    u if current_degrees[u] > 0 else u + 1, current_degrees, edges
                )
                edges.pop()
                current_degrees[u] += 1
                current_degrees[v] += 1

    for seq in valid_sequences:
        if tree_count < 10:
            backtrack(0, list(seq), [])


# --- Run ---
N = 8
solve_and_print(N)
