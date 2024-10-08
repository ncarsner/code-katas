import gc
import sys

def show_memory_usage():
    """Function to show current memory usage."""
    print(f"Memory usage: {sys.getsizeof(object())} bytes")

def enable_gc():
    """Function to enable garbage collection."""
    gc.enable()
    print("Garbage collection enabled.")

def disable_gc():
    """Function to disable garbage collection."""
    gc.disable()
    print("Garbage collection disabled.")

def collect_garbage():
    """Function to manually invoke garbage collection."""
    collected_objects = gc.collect()
    print(f"Garbage collector: collected {collected_objects} objects.")

def create_circular_reference():
    """Function to create a circular reference."""
    class CircularReference:
        def __init__(self):
            self.reference = self

    obj = CircularReference()
    print("Circular reference created.")

def observe_gc_effectiveness():
    """Function to observe the effectiveness of the garbage collector."""
    print("Creating circular reference...")
    create_circular_reference()

    print("Disabling garbage collection and creating circular reference again...")
    disable_gc()
    create_circular_reference()

    print("Enabling garbage collection and collecting garbage...")
    enable_gc()
    collect_garbage()

    print("Garbage collection completed.")

# Demonstrate the usage of the functions
show_memory_usage()
observe_gc_effectiveness()
show_memory_usage()