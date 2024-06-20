class MonkeyLogger:

    def __init__(self, name: str) -> None:
        """
        Parameters:
        name (str):
            some name
        """
        self.name = name

    def greeting(self) -> None:
        """
        Make a simple greeting
        """
        print(f"Hello, {self.name}")
