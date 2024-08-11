def hello_world():
    message = "Hello, World!"
    for char in message:
        if char.isalpha():
            print(char.upper(), end="")
        else:
            print(char, end="")
    print()

hello_world()