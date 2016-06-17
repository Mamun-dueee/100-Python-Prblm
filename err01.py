while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("No valid integer ! Please try again... ")

print("Great, you successfuly entered an integer !")
