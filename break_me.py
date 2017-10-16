"""Break Me."""


def name_error():
    # return a name error by using an unassigned variable
    name = input("What is your name? ")
    print ("Hello ", my_name)


def type_error(a, b):
    # return a type error by mixing str and int
    print(a + "b" + b)


x = 5
y = [1, 4, 5, ]


def attribute_error(obj):
    # return an attribute error by printing an attribute that is none
    print(obj.key[0])


k = {
    "key": 1,
    "key_2": [4, 5, 1, ],
}


# Break through 4 tracebacks
def factorial(x):
    # if x=3 | x=3*2*1
    total = 1
    while x > 0:
        total *= x
        x -= 1
        print (total)
        square(x)


def is_prime(x):
    x = '2'
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True


def square(x):
    print(x ** 2)
    print(is_prime(x))


def trace_fail(x):
    factorial(x)


trace_fail(2837)


# SyntaxError
# def no_loop(obj):
#    for item in obj --no colon
#        print("Shouldn't see this.")
