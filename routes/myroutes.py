import random
from config import app

@app.get('/message')
def greetnow():
    return "Hello Micro services How are you doing?"

@app.get('/number')
def fun():
    num =  random.randint(0,100)  #Return a random integer inside the range 0  & 100
    return f"{num} is returned"