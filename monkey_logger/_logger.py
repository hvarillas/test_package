from logging import Formatter


class MonkeyLogger:

    def __init__(self, name: str, log_level: str | int) -> None:
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

    def __new__(cls, *args, **kwargs):
        parameters: list = ["name", "log_level"]
        kwargs.update(dict(zip(parameters, args)))
        log_level = kwargs.get("log_level")
        if log_level is None:
            print("\033[91m[!] Falta indicar log_level\033[0m")
            return None
        if isinstance(log_level, str):
            log_level = log_level.lower()

        match log_level:
            case 0 | "noset":
                print("[+] No set")
            case 10 | "debug":
                print("[+] debug")
            case 20 | "info":
                print("[+] info")
            case 30 | "warning":
                print("[+] warning")
            case 40 | "error":
                print("[+] Error")
            case 50 | "critical":
                print("[+] critical")
            case _:
                print("[!] Invalid log level")

        return super().__new__(cls)


class ColorFormatter(Formatter):

    COLORS = {
        "DEBUG": "\033[94m",  # Azul
        "INFO": "\033[92m",  # Verde
        "WARNING": "\033[93m",  # Amarillo
        "ERROR": "\033[91m",  # Rojo
        "CRITICAL": "\033[95m",  # Magenta
    }
    RESET = "\033[0m"  # Resetear color

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{log_color}{message}{self.RESET}"
