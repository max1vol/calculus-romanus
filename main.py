import sys
from calculus_romanus.interpreter import run_calculus_romanus


def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        with open(file_path, "r") as f:
            code = f.read()
        run_calculus_romanus(code)
    else:
        print("Usage: python main.py <file_path>")


if __name__ == "__main__":
    main()
