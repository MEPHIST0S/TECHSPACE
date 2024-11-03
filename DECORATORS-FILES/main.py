#MODULES
from os.path import exists
from datetime import datetime

#PRIME CONDITION AND TXT FILE CREATION IN WRITING MODE
if not exists("records.txt"):
    with open("records.txt", "w") as file:
        #TABLE TITLES
        file.write("     FUNCTION NAME     |     WORKED TIME     |     ARGUMENTS     |     KEYWORD ARGMUNETS     |     RESULT     \n")

#DECORATOR
def logger(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            result_str = str(result)
        except Exception as e:
            result_str = str(e)
        
        func_name = f"{func.__name__:<16}"
        worked_time = f"{datetime.now}"
        args_str = ", ".join(map(str, args))
        kwargs_str = ", ".join(f"{key} = {value}" for key, value in kwargs.items())
        
        with open("records.txt", "a") as file:
            file.write(f"     {func_name}     |     {worked_time}     |     {args_str}     |     {kwargs_str}     |     {result_str}     \n")
    return inner

#FUNCTION FOR SUMM
@logger
def summ(a, b):
    return a + b

#FUNTCTION FOR DIVISION
@logger
def division(a, b):
    return a / b

#APPLICATION
summ(1, 4)
division(a = 5, b = 1)