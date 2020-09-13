def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        passwd = [int(i) for i in input().split(" ")]
        if len(set(passwd)) == 1:
            print(len(passwd))
        else:
            while len(set(passwd)) != 1:
                adder = max(passwd)
                if passwd.index(adder) == 0 and passwd[1] != adder:
                    passwd[1] += adder
                    passwd.pop(0)
                else:
                    index = 0
                    while index < len(passwd):
                        index += 1
                        if passwd[index] == adder and passwd[index - 1] != adder:
                            passwd[index - 1] += adder
                            passwd.pop(index)
                            break
            print(len(passwd))

if __name__ == "__main__":
    main()