from graphlib import TopologicalSorter, CycleError
from typing import Dict, List

"""
Useful for dependency resolution, task scheduling, and cycle detection using TopologicalSorter, managing dependencies in data pipelines, and task scheduling.
"""


def resolve_dependencies(dependency_map: Dict[str, List[str]]) -> List[str]:
    """
    Given a dependency map, returns a list of items in a valid processing order.
    Raises CycleError if a cycle is detected.

    Args:
        dependency_map: Dict mapping item to list of dependencies.

    Returns:
        List of items in topological order.

    Example:
        >>> deps = {'report': ['extract', 'transform'], 'extract': [], 'transform': ['extract']}
        >>> resolve_dependencies(deps)
        ['extract', 'transform', 'report']
    """
    ts = TopologicalSorter(dependency_map)
    try:
        order = list(ts.static_order())
        return order
    except CycleError as e:
        print(f"Cycle detected: {e.args}")
        raise


def schedule_tasks(tasks: Dict[str, List[str]]) -> List[List[str]]:
    """
    Schedules tasks in levels, where each level contains tasks that can be run in parallel.

    Args:
        tasks: Dict mapping task name to list of dependencies.

    Returns:
        List of lists, each inner list contains tasks for that level.

    Example:
        >>> tasks = {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
        >>> schedule_tasks(tasks)
        [['A'], ['B', 'C'], ['D']]
    """
    ts = TopologicalSorter(tasks)
    ts.prepare()
    schedule = []
    while ts.is_active():
        ready = list(ts.get_ready())
        if ready:
            schedule.append(ready)
            ts.done(*ready)
    return schedule


def detect_cycles(dependency_map: Dict[str, List[str]]) -> bool:
    """
    Checks if the dependency map contains cycles.

    Args:
        dependency_map: Dict mapping item to list of dependencies.

    Returns:
        True if a cycle is detected, False otherwise.

    Example:
        >>> detect_cycles({'A': ['B'], 'B': ['A']})
        True
    """
    try:
        list(TopologicalSorter(dependency_map).static_order())
        return False
    except CycleError:
        return True


if __name__ == "__main__":
    # Dependency resolution for data pipeline
    pipeline = {
        "extract_sales": [],
        "extract_customers": [],
        "transform_sales": ["extract_sales"],
        "transform_customers": ["extract_customers"],
        "join_data": ["transform_sales", "transform_customers"],
        "generate_report": ["join_data"],
    }
    print("Pipeline order:", resolve_dependencies(pipeline))

    # Task scheduling for parallel execution
    tasks = {
        "load_data": [],
        "clean_data": ["load_data"],
        "analyze_data": ["clean_data"],
        "visualize": ["analyze_data"],
        "notify": ["visualize"],
    }
    print("Task schedule:", schedule_tasks(tasks))

    # Detecting cycles in dependencies
    cyclic = {"A": ["B"], "B": ["C"], "C": ["A"]}
    print("Cycle detected?", detect_cycles(cyclic))
