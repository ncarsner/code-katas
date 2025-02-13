import logging
import logging.config


# Configure the root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

# Create custom logger
logger = logging.getLogger(__name__)

# Logging at different levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


### Using nested import module

logging.config.fileConfig("logging.conf")

module_logger = logging.getLogger("module_logger")
module_logger.info("This is an info message from module_logger")


class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        print(f"Custom handler: {log_entry}")


custom_handler = CustomHandler()
custom_handler.setLevel(logging.WARNING)
custom_handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(custom_handler)

logger.warning("This is a warning message with custom handler")
logger.error("This is an error message with custom handler")


class CustomFilter(logging.Filter):
    def filter(self, record):
        return "special" in record.getMessage()


special_filter = CustomFilter()
logger.addFilter(special_filter)

logger.info("This is a special info message")
logger.info("This is a regular info message")


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f"CustomAdapter: {msg}", kwargs


adapter = CustomAdapter(logger, {})
adapter.info("This is an info message with adapter")
