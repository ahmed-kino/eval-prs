import logging


class Logger:
    def __init__(self):
        self.logging = logging
        self.logging.getLogger().setLevel(logging.INFO)
        self.logging.basicConfig(
            level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
        )

    def info(self, message):
        return self.logging.info(message)

    def debug(self, message):
        return self.logging.debug(message)

    def warning(self, message):
        return self.logging.warning(message)

    def error(self, message):
        return self.logging.error(message)

    def critical(self, message):
        return self.logging.critical(message)

    def prompt(self, message):
        print(message)
