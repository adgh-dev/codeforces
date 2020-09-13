# In one step you can do one of the following moves:

# decrease n by 1;
# divide n by k if n is divisible by k.
# For example, if n=27 and k=3 you can do the following steps: 27→26→25→24→8→7→6→2→1→0.

# You are asked to calculate the minimum number of steps to reach 0 from n.

def main():
    test_cases = int(input())
    pairs = []
    while test_cases > 0:
        pairs.append(
            (input().split(" "))
            )
        test_cases -= 1

    for pair in pairs:
        n = int(pair[0])
        k = int(pair[1])
        steps = 0
        if k == 1:
            steps = n
        else:
            while n > 0:
                if n % k == 0:
                    n = n//k
                    steps += 1
                else:
                    steps += n % k
                    n -= n % k
        print(steps)

if __name__ == "__main__":
    main()