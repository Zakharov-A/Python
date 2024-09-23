# lambda parameters: expression

# def mult(a, b):
#     return a * b

# mult_2 = lambda a, b: a * b

# print(mult(3, 3))
# print(mult_2(4, 4))

# ----

def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good Morning")

print(morning_greeting("Jimmy"))

evening_greeting = greeting("Good Evening")

print(evening_greeting('Jimmy'))
