def main():
    num = input()
    # check original number
    s = sorted(set(num))
    if s == ["4"] or s == ["7"] or s == ["4", "7"]:
        return "YES"
    
    num = int(num)
    fact = 2
    while fact <= num/2:
        if num % fact == 0:
            _ = sorted(set(str(fact)))
            if  _ == ["4"] or _ == ["7"] or _ == ["4", "7"]:
                return "YES"
        fact += 1
    
    return "NO"

if __name__ == "__main__":
    print(main())