import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"), #This handler writes log messages to a file named app1.log.
        logging.StreamHandler() #This handler writes log messages to the console (standard output).
    ]
)

logger = logging.getLogger("ArithmeticCalculator")

def add(a,b):
    res = a+b
    logger.debug(f"Adding {a} + {b} = {res}")
    return res

def subtract(a,b):
    res = a-b
    logger.debug(f"Subtracting {a} - {b} = {res}")
    return res

def multiply(a,b):
    res = a*b
    logger.debug(f"Multiply {a} * {b} = {res}")
    return res

def division(a,b):
    try:
        res = a//b
        logger.debug(f"Division {a} / {b} = {res}")
        return res
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(5,3)
subtract(5,3)    
multiply(5,3)
division(5,0)