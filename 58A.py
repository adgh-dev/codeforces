from collections import OrderedDict

def main():
    string = input()
    match = "hello"

    i = 0
    j = 0
    found = 0

    while i < len(string):
        if string[i] == match[j]:
            j += 1
            found += 1
            if found == 5:
                return "YES"
        i += 1
    return "NO"


if __name__ == "__main__":
    print(main())