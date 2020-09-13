def main():
    n = int(input())
    x = 0
    y = 0
    z = 0
    while n > 0:
        vector = input().split(" ")
        x += int(vector[0])
        y += int(vector[1])
        z += int(vector[2])
        n -= 1
    if x == 0 and y == 0 and z == 0:
        return "YES"
    return "NO"

if __name__ == "__main__":
    print(main())