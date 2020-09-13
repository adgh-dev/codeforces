def main():
    a = int(input())
    b = int(input())
    c = int(input())

    if a == 1 and b == 1 and c == 1:
        return a + b + c

    if a == 1:
        if b == 1:
            return (a + b) * c
        else:
            return a + b + c
    
    if b == 1:
        return ( min(a, c) + 1 ) *  max(a, c)

    if c == 1:
        return a * (b + c)

    return a * b * c
     

if __name__ == "__main__":
    print(main())