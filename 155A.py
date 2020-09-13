
def main():
    n = int(input())
    games = [int(i) for i in input().split(" ")]
    rez_min = None
    rez_max = None
    amz = 0
    for game in games:
        if rez_min == None and rez_max == None:
            rez_min = game
            rez_max = game
        else:
            if game < rez_min or game > rez_max:
                rez_min = min(rez_min, game)
                rez_max = max(rez_max, game)
                amz += 1

    print(amz)


if __name__ == "__main__":
    main()