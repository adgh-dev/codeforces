def main():
    a = input().lower()
    b = input().lower()
    if a == b:
        print(0)
        return
    print(-1) if a < b else print(1)


if __name__ == "__main__":
    main()