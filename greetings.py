#greetings.py

def greet(name):
    return "Hello, " + name + "!"

if __name__=="__main__":
    print("Greetings module is being run directly!")
    print(greet("Direct user"))