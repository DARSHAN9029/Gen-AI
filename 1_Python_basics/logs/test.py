from logger import logging

def add(a,b):
    logging.debug("the addition is taking place")
    return a+b

logging.debug("the addition function is called")
add(12,23)