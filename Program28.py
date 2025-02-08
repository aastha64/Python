# DECORATORS
# Decorators are functions that modify the behaviour of other functions or methods.
# Decorators takes over function as an argument and returns a new function that adds so original function without modifying their source code
# In decorators, we try to send a complete function as a parameter inside another function
# A decorator is symbolized by uisng @ symbol

def my_decorator (greetings): #func say = hello ()
    def wrapper():
        print("Somathing is happening for Training.")
        greetings () # Actually Calling the say hello ()
        print("So far 50 People have Been Trained on Python")
    return wrapper

@my_decorator # Decorator my_decorator will execute First
def say_hello():
    print("Courtesy: Orange Business Services")
    print("*****")

say_hello() #Function is being Called