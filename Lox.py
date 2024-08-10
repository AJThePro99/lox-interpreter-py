import sys
from run_dir.run import runFile, runPrompt


def main(args):
    if len(args) > 1:
        print("Usage: python Lox.py [script]")
        exit(64)
    elif args.length == 1:
        runFile(args[0])
    else:
        runPrompt()


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
