# "H" prints "Hello, World!",
# "Q" prints the source code of the program itself,
# "9" prints the lyrics of "99 Bottles of Beer" song,
# "+" increments the value stored in the internal accumulator.

def main():
    num_groups = int(input())
    groups = input().split(" ")

    four = groups.count("4")
    three = groups.count("3")
    two = groups.count("2")
    one = groups.count("1")

    cabs = four
    if three > one:
        cabs += three
        one = 0
    else:
        cabs += three
        one = one - three

    if two % 2 == 0:
        cabs += two // 2
        two = 0
    else:
        cabs += two // 2
        two = 1
        if one > 2:
            cabs += 1
            two = 0
            one = one - 2
        else:
            cabs += 1
            two = 0
            one = 0

    if one:
        cabs += one // 4
        one = one % 4

    if one:
        cabs += 1

    print(cabs)
            

if __name__ == "__main__":
    main()