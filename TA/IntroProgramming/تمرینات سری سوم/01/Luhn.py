def luhn(n):
    s = ""
    for i in range(2, len(n) + 1, 2):
        s += str(2 * int(n[-i]))
        n = n[:-i] + "0" + n[-1:-i:-1]
    summ = sum(list(map(int, n)))
    summ += sum(list(map(int, s)))
    if summ % 10 == 0:
        return True
    return False


def main():
    n = input()
    print(luhn(n))


if __name__ == "__main__":
    main()
