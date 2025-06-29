import logging

##logging setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H-%M-%S',
    force=True,
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]  
)

logger=logging.getLogger("ArithmeticApp")

def add(a,b):
    result=a+b
    logger.debug("Adding {a} + {b} = {result}")
    return result

def sub(a,b):
    result=a-b
    logger.debug("Subtracting {a} - {b} = {result}")
    return result

def mul(a,b):
    result=a*b
    logger.debug("Multiplying {a} * {b} = {result}")
    return result

def div(a,b):
    try:
        result=a / b
        logger.debug("Dividing {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by Zerp error")
        return None
    
add(12,32)
sub(23,12)
mul(23,11)
div(12,2)
div(12,0)