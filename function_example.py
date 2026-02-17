def greeting():
    """
    Prints out a bunch of greetings in various languages
    :return:
    """
    print("Hello")
    print("Hola")
    print("Bonjour")
    print("Ciao")
    print("Hallo")
    print("Ni hao")

def greeting2(name):
    """
    Prints out a bunch of greetings in various languages
    :param name: the name of the person to greet
    :return:
    """
    print("Hello", name)
    print("Hola", name)
    print("Bonjour", name)
    print("Ciao", name)
    print("Hallo", name)
    print("Ni hao", name)

def greeting3(name):
    """
    Prints out a bunch of greetings in various languages
    :param name: the name of the person to greet
    :return: the greeting string
    """
    message = ""
    message +=f"Hello, {name}\n"
    message +=f"Hola, {name}\n"
    message +=f"Bonjour, {name}\n"
    message +=f"Ciao, {name}\n"
    message +=f"Hallo, {name}\n"
    message +=f"Ni hao, {name}\n"
    return message

for i in range(10):
    greeting()
print("I can take a break")
for i in range(5):
    greeting2("John")


print(greeting3("Bob").replace("Bob", "Billy Bob").upper())