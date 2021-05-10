import logging
import logging.config
import yaml

# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')

# logging.basicConfig(format='%(process)d - %(levelname)s - %(message)s')
# logging.warning("This is warning")

# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info("Admin logged in....")

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')

# name = 'John'
# logging.error("%s raised error", name)
# logging.error(f'{name} raised error')

# a = 5
# b = 0
# try:
#     a/b
# except Exception as e:
#     logging.error("Exception occured!", exc_info=True)

# logger = logging.getLogger("first_logger")
# logger.warning("This is first logger")

# logger = logging.getLogger(__name__)
# # Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)
# # Create formatters and add it to handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)
# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)
# logger.warning('This is a warning')
# logger.error('This is an error')

# logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
# logger = logging.getLogger(__name__)
# logger.debug('This is a debug message')

# with open('config.yaml', 'r') as f:
#     config = yaml.safe_load(f.read())
#     logging.config.dictConfig(config)
# logger = logging.getLogger(__name__)
# logger.debug('This is a debug message')