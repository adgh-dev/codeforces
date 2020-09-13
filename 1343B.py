
def main():
    n = int(input())
    if n < 4 or n % 4 != 0:
        print("NO")
        return
    
    odd = []
    even = []
    for i in range(1, n // 2 + 1):
        odd.append(i * 2 - 1)
        even.append(i * 2)

    odd[-1] += n // 2

    # print(odd, sum(odd))
    # print(even, sum(even))

    print(" ".join([str(i) for i in even + odd]))


if __name__ == "__main__":
    main()