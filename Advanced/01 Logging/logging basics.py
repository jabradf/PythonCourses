import logging

logger = logging.getLogger(__name__)

import sys
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

# the logging levels
print(logging.NOTSET)
print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)