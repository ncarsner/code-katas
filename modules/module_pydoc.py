import pydoc


def generate_module_documentation(module_name):
    """Generate and print the documentation for a given module."""
    doc = pydoc.render_doc(module_name, renderer=pydoc.plaintext)
    print(doc)


def start_http_server(port=8080):
    """Start a local HTTP server to browse documentation."""
    pydoc.serve(port)


def generate_html_documentation(module_name, output_file):
    """Generate HTML documentation for a given module and save it to a file."""
    doc = pydoc.HTMLDoc().docmodule(pydoc.safeimport(module_name))
    with open(output_file, "w") as f:
        f.write(doc)


def show_function_documentation(module_name, func_name):
    """Show documentation for a specific function or class within a module."""
    module = pydoc.safeimport(module_name)
    if module:
        func = getattr(module, func_name, None)
        if func:
            print(pydoc.render_doc(func, renderer=pydoc.plaintext))
        else:
            print(
                f"Function or class '{func_name}' not found in module '{module_name}'"
            )
    else:
        print(f"Module '{module_name}' not found")


if __name__ == "__main__":
    generate_module_documentation("math")

    # start_http_server(8080)

    # generate_html_documentation("math", "math_doc.html")

    show_function_documentation("math", "sqrt")
