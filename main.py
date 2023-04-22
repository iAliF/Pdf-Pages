import os
import sys

from pypdf import PdfReader


def count(path: str) -> int:
    s = 0

    for file in os.listdir(path):
        if not file.endswith(".pdf"):
            continue

        fp = os.path.join(path, file)
        reader = PdfReader(fp)
        s += len(reader.pages)

    return s


def main() -> None:
    if len(args := sys.argv) != 2:
        print("Pass files directory path")
        exit()

    if not (os.path.isdir(path := args[1])):
        print("Directory was not found")
        exit()

    result = count(path)
    print(f"Total pages: {result}")


if __name__ == '__main__':
    main()
