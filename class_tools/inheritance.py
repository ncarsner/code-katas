class AccessLevel:
    """Base class for all access levels."""

    def __init__(self, read: bool, write: bool, execute: bool) -> None:
        self.read = read
        self.write = write
        self.execute = execute

    def describe_permissions(self) -> str:
        permissions = []
        if self.read:
            permissions.append("read")
        if self.write:
            permissions.append("write")
        if self.execute:
            permissions.append("execute")
        return f"Permissions: {', '.join(permissions)}"


class ReadOnly(AccessLevel):
    def __init__(self) -> None:
        super().__init__(read=True, write=False, execute=False)


class ReadWrite(AccessLevel):
    def __init__(self) -> None:
        super().__init__(read=True, write=True, execute=False)


class FullAccess(AccessLevel):
    def __init__(self) -> None:
        super().__init__(read=True, write=True, execute=True)


if __name__ == "__main__":
    read_only = ReadOnly()
    read_write = ReadWrite()
    full_access = FullAccess()

    print(f"ReadOnly: {read_only.describe_permissions()}")
    print(f"ReadWrite: {read_write.describe_permissions()}")
    print(f"FullAccess: {full_access.describe_permissions()}")
