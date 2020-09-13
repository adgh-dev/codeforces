# "H" prints "Hello, World!",
# "Q" prints the source code of the program itself,
# "9" prints the lyrics of "99 Bottles of Beer" song,
# "+" increments the value stored in the internal accumulator.

def main():
    code = input()
    if "H" in code or "Q" in code or "9" in code:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()