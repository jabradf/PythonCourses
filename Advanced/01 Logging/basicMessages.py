import logging
import sys

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG) # default level is WARNING
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
        
def division():
  try:
    dividend = float(input("Enter the dividend: "))
    logger.info(dividend) #step 4 info message doesn't get printed
    divisor = float(input("Enter the divisor: "))
    logger.info(divisor)  #step 4
  except ValueError:
    logger.log(logging.CRITICAL, "No dividend or divisor value entered!") #step 2 add critical using log(level, method) for values 6, (no value))
    return None
  if divisor == 0:
    logger.error("Attempting to divide by 0!")  # step 1 add error for values 6, 0
    return None
  else:
    return dividend/divisor
result = division()

# step 3 print a warning for 6, 0
if result==None:
  logger.warning("The result value is None!")
  