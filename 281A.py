def main():
    word = input()
    result = []

    result.append(word[0].upper())
    result += word[1:]

    print("".join(result))

if __name__ == "__main__":
    main()