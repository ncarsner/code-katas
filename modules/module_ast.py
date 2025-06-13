import ast
from typing import Any, List, Dict
import re

"""
The `ast` (Abstract Syntax Tree) module allows you to parse, analyze, and modify Python code programmatically. Useful for code validation, dynamic code analysis, or building custom code linters.
"""


def safe_eval(expr: str, allowed_names: Dict[str, Any] = None) -> Any:
    """
    Safely evaluate a simple Python expression using AST parsing.
    Only allows literals and names in `allowed_names`.

    Args:
        expr (str): The expression to evaluate.
        allowed_names (dict): A dictionary of allowed variable names and their values.

    Returns:
        Any: The result of the evaluated expression.

    Raises:
        ValueError: If the expression contains unsafe nodes.
    """
    allowed_names = allowed_names or {}

    class SafeEvalVisitor(ast.NodeVisitor):
        SAFE_NODES = (
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Str, ast.Bytes,
            ast.Name, ast.Load, ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
            ast.Mod, ast.USub, ast.UAdd, ast.Constant
        )

        def visit(self, node):
            if not isinstance(node, self.SAFE_NODES):
                raise ValueError(f"Unsafe expression: {ast.dump(node)}")
            return super().visit(node)

        def visit_Name(self, node):
            if node.id not in allowed_names:
                raise ValueError(f"Use of unknown variable: {node.id}")

    tree = ast.parse(expr, mode='eval')
    SafeEvalVisitor().visit(tree)
    code = compile(tree, filename="<ast>", mode="eval")
    return eval(code, {"__builtins__": {}}, allowed_names)


def find_function_calls(source: str) -> List[str]:
    """
    Find all function calls in a given Python source code string.

    Args:
        source (str): Python source code.

    Returns:
        List[str]: List of function names called in the code.
    """
    class CallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.calls = []

        def visit_Call(self, node):
            if isinstance(node.func, ast.Name):
                self.calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                self.calls.append(node.func.attr)
            self.generic_visit(node)

    tree = ast.parse(source)
    visitor = CallVisitor()
    visitor.visit(tree)
    return visitor.calls


def extract_column_names_from_query(query: str) -> List[str]:
    """
    Example: Extract column names from a simple SQL SELECT statement embedded in Python code.

    Args:
        query (str): SQL query string.

    Returns:
        List[str]: List of column names.
    """
    # This is a naive implementation for demonstration purposes.
    # For production, use a SQL parser library.
    match = re.search(r"select\s+(.*?)\s+from", query, re.IGNORECASE)
    if match:
        columns = match.group(1)
        return [col.strip() for col in columns.split(",")]
    return []


def analyze_code_for_assignments(source: str) -> Dict[str, Any]:
    """
    Analyze Python code and return a dictionary of variable assignments.

    Args:
        source (str): Python source code.

    Returns:
        Dict[str, Any]: Mapping of variable names to their assigned values (as AST nodes).
    """
    class AssignVisitor(ast.NodeVisitor):
        def __init__(self):
            self.assignments = {}

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.assignments[target.id] = ast.dump(node.value)
            self.generic_visit(node)

    tree = ast.parse(source)
    visitor = AssignVisitor()
    visitor.visit(tree)
    return visitor.assignments


if __name__ == "__main__":
    # Safe evaluation
    expr = "a + b * 2"
    allowed = {"a": 10, "b": 5}
    print(f"Safe eval result: {safe_eval(expr, allowed)}")  # Output: 20

    # Find function calls
    code = """
def foo():
    print('Hello')
    data = [1, 2, 3]
    sum(data)
    max(data)
"""
    print(f"Function calls: {find_function_calls(code)}")  # Output: ['print', 'sum', 'max']

    # Extract columns from SQL query
    sql = "SELECT id, name, salary FROM employees WHERE salary > 50000"
    print(f"Columns: {extract_column_names_from_query(sql)}")  # Output: ['id', 'name', 'salary']

    # Analyze assignments
    code2 = """
x = 42
y = x + 1
z = 'hello'
"""
    print(f"Assignments: {analyze_code_for_assignments(code2)}")
    # Output: {'x': 'Constant(value=42)', 'y': 'BinOp(left=Name(id='x', ctx=Load()), op=Add(), right=Constant(value=1))', 'z': "Constant(value='hello')"}
