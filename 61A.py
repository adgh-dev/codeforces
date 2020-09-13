def main():
    a = input()
    b = input()

    result = []
    i = 0

    while i < len(a):
        result.append(int(a[i]) ^ int(b[i]))
        i += 1

    print("".join(str(dig) for dig in result))

if __name__ == "__main__":
    main()