def main():
    _ = input().split(" ")
    k = int(_[1])
    _ = input().split(" ")
    scores = [int(i) for i in _]
    cutout_score = scores[k-1]
    scores = [i for i in scores if i > 0 and i >= cutout_score]
    print(len(scores))

if __name__ == "__main__":
    main()