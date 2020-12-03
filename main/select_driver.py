import platform
from os import getcwd, path


class SelectDriver:
    def __init__(self):
        self.driver_version = self.GetDriver()

    def GetDriver(self):
        os = platform.system()
        drivers_dir = path.join(getcwd(), path.dirname(__file__), "web_drivers")
        if os == "Windows":
            return path.join(drivers_dir, "chromedriver.exe")
        if os == "Linux":
            return path.join(drivers_dir, "chromedriver_linux")
        else:
            return path.join(drivers_dir, "chromedriver_macos")
