VOWELS = ["A", "O", "Y", "E", "U", "I"]

def main():
    text = input()
    result = [l.lower() for l in text if l.upper() not in VOWELS]
    print("." + ".".join(result))

if __name__ == "__main__":
    main()