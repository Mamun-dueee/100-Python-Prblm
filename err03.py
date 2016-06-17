def f():
    x = int("four")

try:
    f()
except ValueError as e:
    print("got it :-) ", e)


print("Let's get on")
