import logging


"""
Example configuration options:

1. Basic configuration:
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

2. Configuration using a dictionary:
logging.config.dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    }},
    'handlers': {'file': {
        'class': 'logging.FileHandler',
        'filename': 'app.log',
        'formatter': 'default',
    }, 'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'default',
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['file', 'console']
    },
})

3. Configuration using a config file:
logging.config.fileConfig('logging.conf')


4. Configuration using a custom logger:
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('app.log'))
logger.addHandler(logging.StreamHandler())
logger.propagate = False


5. Configuration using a custom handler:
class CustomHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        print(f'Custom handler: {log_entry}')

custom_handler = CustomHandler()
custom_handler.setLevel(logging.WARNING)
logger.addHandler(custom_handler)
logger.warning('This is a warning message with custom handler')
logger.error('This is an error message with custom handler')


6. Configuration using a custom filter:
class CustomFilter(logging.Filter):
    def filter(self, record):
        return 'special' in record.getMessage()

special_filter = CustomFilter()
logger.addFilter(special_filter)
logger.info('This is a special info message')
logger.info('This is a regular info message')


7. Configuration using a custom adapter:
class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f'CustomAdapter: {msg}', kwargs

adapter = CustomAdapter(logger, {})
adapter.info('This is an info message with adapter')


8. Configuration using a RotatingFileHandler:
rotating_handler = logging.handlers.RotatingFileHandler('rotating_app.log', maxBytes=1024**2, backupCount=5)
rotating_handler.setLevel(logging.INFO)
rotating_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

rotating_logger = logging.getLogger('rotating_logger')
rotating_logger.setLevel(logging.INFO)
rotating_logger.addHandler(rotating_handler)
rotating_logger.info('This is an info message with rotating file handler')
rotating_logger.error('This is an error message with rotating file handler')


9. Configuration using a TimedRotatingFileHandler:
timed_handler = logging.handlers.TimedRotatingFileHandler('timed_app.log', when='midnight', interval=1, backupCount=5)
timed_handler.setLevel(logging.INFO)
timed_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

timed_logger = logging.getLogger('timed_logger')
timed_logger.setLevel(logging.INFO)
timed_logger.addHandler(timed_handler)
timed_logger.info('This is an info message with timed rotating file handler')
timed_logger.error('This is an error message with timed rotating file handler')


10. Configuration using a SMTPHandler:
smtp_handler = logging.handlers.SMTPHandler(
    mailhost='smtp.example.com',             # SMTP server
    )

smtp_handler.setLevel(logging.ERROR)
smtp_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

smtp_logger = logging.getLogger('smtp_logger')
smtp_logger.setLevel(logging.ERROR)
smtp_logger.addHandler(smtp_handler)
smtp_logger.error('This is an error message sent via email')


11. Configuration using a SysLogHandler:
syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')

syslog_handler.setLevel(logging.ERROR)
syslog_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

syslog_logger = logging.getLogger('syslog_logger')
syslog_logger.setLevel(logging.ERROR)
syslog_logger.addHandler(syslog_handler)
syslog_logger.error('This is an error message sent to syslog')


12. Configuration using a QueueHandler:
queue = queue.Queue()
queue_handler = logging.handlers.QueueHandler(queue)

queue_handler.setLevel(logging.INFO)
queue_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

queue_logger = logging.getLogger('queue_logger')

queue_logger.addHandler(queue_handler)
queue_logger.info('This is an info message added to the queue')

record = queue.get()
print(record.getMessage())


13. Configuration using a QueueListener:
queue = queue.Queue()
queue_handler = logging.handlers.QueueHandler(queue)

queue_listener = logging.handlers.QueueListener(queue, logging.StreamHandler())
queue_listener.start()

queue_logger = logging.getLogger('queue_logger')
queue_logger.addHandler(queue_handler)
queue_logger.info('This is an info message added to the queue')

queue_listener.stop()


14. Configuration using a NullHandler:
null_handler = logging.NullHandler()

null_logger = logging.getLogger('null_logger')
null_logger.addHandler(null_handler)
null_logger.info('This is an info message that will not be logged')


15. Configuration using a MemoryHandler:
memory_handler = logging.handlers.MemoryHandler(1000)

memory_handler.setLevel(logging.INFO)
memory_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

memory_logger = logging.getLogger('memory_logger')
memory_logger.addHandler(memory_handler)
memory_logger.info('This is an info message added to the memory buffer')



References:
https://docs.python.org/3/library/logging.html
https://docs.python.org/3/library/logging.config.html
https://docs.python.org/3/library/logging.handlers.html
https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueListener
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.NullHandler
https://docs.python.org/3/library/logging.handlers.html#logging.handlers.MemoryHandler
https://docs.python.org/3/library/logging.html#logrecord-attributes

"""

# Configure the root logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

# Create custom logger
logger = logging.getLogger(__name__)

# Logging at different levels
logger.notset("This is a notset message")
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


def setup_rotating_logger():
    """
    Sets up a logger with a RotatingFileHandler.

    The RotatingFileHandler will log messages to a file and rotate the log file
    when it reaches a certain size. This prevents the log file from growing indefinitely.

    RotatingFileHandler arguments:
        filename (str): The name of the log file.
        maxBytes (int): The maximum size of the log file in bytes before it gets rotated.
        backupCount (int): The number of backup files to keep.

    Returns:
        logging.Logger: The logger with the RotatingFileHandler configured.
    """
    rotating_handler = logging.handlers.RotatingFileHandler(
        "rotating_app.log", maxBytes=1024**2, backupCount=5
    )
    rotating_handler.setLevel(logging.INFO)
    rotating_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    rotating_logger = logging.getLogger("rotating_logger")
    rotating_logger.setLevel(logging.INFO)
    rotating_logger.addHandler(rotating_handler)

    return rotating_logger


# Initialize the rotating logger
rotating_logger = setup_rotating_logger()
rotating_logger.info("This is an info message with rotating file handler")
rotating_logger.error("This is an error message with rotating file handler")
