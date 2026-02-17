def add_numbers(a, b, c=0):
    """
    Adds 2 or 3 numbers
    :param a: first number
    :param b: second number
    :param c: third number
    :return: result of addition of two/three numbers
    """
    return a + b + c

print(add_numbers(1, 2, 3))
print(add_numbers(5, 7, )) # missing an argument unless c is default value of 0

# a function can call itself (recursive function)
def factorial(n):
    """
    Calculates the factorial of n
    :param n: the n
    :return: factorial result
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def rec_factorial(n):
    if n==0:
        return 1
    return n * rec_factorial(n-1)

print(factorial(5))
print(rec_factorial(5))

# functions can call other functions

def bond_greeting(first, last, lang="es"):
    """
    Does the bond greeting
    :param first: first name
    :param last: last name
    :param lang: language
    :return: the greeting
    """
    if lang == "en":
        return english_greeting(first, last)
    elif lang == "fr":
        return french_greeting(first, last)
    elif lang == "es":
        return spanish_greeting(first, last)

def english_greeting(first, last):
    return f"The name is: {last}, {first} {last}"

def french_greeting(first, last):
    return f"Je m'appelle: Le{last}, {first} Le{last}"

def spanish_greeting(first, last):
    return f"Me llamo: {last}ito, {first}ito {last}ito"

print(bond_greeting(first="James", last="Bond", lang="es"))

