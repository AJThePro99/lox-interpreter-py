def runFile(path):
    # For interpreting lox source code files
    with open(path, "r") as file:
        run(file.read())


def runPrompt():
    # For running in interactive mode
    while True:
        print("> ")
        line = input()
        if line == "":
            break
        run(line)


def run(source):
    # TODO: Scan tokens
    # TODO: For now, print the tokens
    pass
