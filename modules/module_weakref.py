import weakref
from typing import Any, Dict


class DataCache:
    """
    A class that uses weak references to cache data objects.
    This prevents memory leaks by allowing objects to be garbage collected
    when no strong references exist.
    """

    def __init__(self):
        # Store weak references to cached objects in dictionary
        self._cache: Dict[str, weakref.ref] = {}

    def add_to_cache(self, key: str, value: Any) -> None:
        """
        Add an object to the cache with a weak reference.

        Args:
            key (str): The key to identify the cached object.
            value (Any): The object to cache.
        """
        self._cache[key] = weakref.ref(value)
        print(f"Added {key} to cache.")

    def get_from_cache(self, key: str) -> Any:
        """
        Retrieve an object from the cache.

        Args:
            key (str): The key to identify the cached object.

        Returns:
            Any: The cached object, or None if the object has been garbage collected.
        """
        ref = self._cache.get(key)
        if ref is not None:
            obj = ref()
            if obj is not None:
                print(f"Retrieved {key} from cache.")
                return obj
            else:
                print(f"{key} has been garbage collected.")
        else:
            print(f"{key} not found in cache.")
        return None


if __name__ == "__main__":
    # Instantiate the DataCache
    cache = DataCache()

    # Create a sample data object
    class DataObject:
        def __init__(self, name: str):
            self.name = name

        def __repr__(self):
            return f"DataObject(name={self.name})"

    # Add objects to the cache
    obj1 = DataObject("Sales Data")
    cache.add_to_cache("sales", obj1)

    obj2 = DataObject("Marketing Data")
    cache.add_to_cache("marketing", obj2)

    # Retrieve objects from the cache
    retrieved_obj1 = cache.get_from_cache("sales")
    print(retrieved_obj1)

    # Delete the strong reference to obj1
    del obj1

    # Try to retrieve obj1 again
    retrieved_obj1 = cache.get_from_cache("sales")
    print(retrieved_obj1)

    # Retrieve obj2
    retrieved_obj2 = cache.get_from_cache("marketing")
    print(retrieved_obj2)
