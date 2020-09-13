def main():
    text = input()
    lower_case_found = False
    for letter in text[1:]:
        if letter.islower():
            lower_case_found = True
            break
    if not lower_case_found:
        text = text.swapcase()
    print(text)

if __name__ == "__main__":
    main()