def main():
    n, m = [int(i) for i in input().split(" ")]
    task_houses = [int(i) for i in input().split(" ")]
    ttime = 0
    start_house = 1
    ttime = task_houses[0] - start_house
    for i in range(1, m):
        t = task_houses[i] - task_houses[i - 1]
        if t < 0:
            t += n
        ttime += t

    print(
        ttime
    )

if __name__ == "__main__":
    main()