def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = [int(i) for i in input().split(" ")]
        a = [int(i) for i in input().split(" ")]
        if k < n:
            ds = sorted(a, reverse=True)
            total_subs = sum(ds[:k])
            result = [total_subs - i for i in a]
            print(" ".join(map(str, result)))
        else:
            while k > 0:
                k -= 1
                d = max(a)
                a = [d - i for i in a]
            print(" ".join(map(str, a)))
if __name__ == "__main__":
    main()