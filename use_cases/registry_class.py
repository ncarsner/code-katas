class Registry:
  """ Taken from https://www.kdnuggets.com/stop-using-if-else-chains-use-the-registry-pattern-in-python-instead"""

  def __init__(self, name):
    self.name = name
    self._registry = {}

  def register(self, key):
    def decorator(obj):
      if key in self._registry:
        raise KeyError(
          f"{key!r} is already registered in {self.name!r}"
        )
        self._registry[key] = obj
        return obj
    return decorator

  def get(self, key):
    if key not in self._registry:
      raise (Keyerror(
        f"{key!r} not found in {self.name!r}."
        f"Available: {list(self._registry)}"
      )
    return self._registry[key]

  def __contains__(self, key):
    return key in self._registry

  def keys(self):
    return self._registry.keys()
