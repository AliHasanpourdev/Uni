def palindrom(s):
    if len(s) == 1:
        return 1
    elif len(s) == 2:
        if s[0] == s[-1]:
            return 1
        return 0
    else:
        if s[0] == s[-1]:
            return palindrom(s[1:-1])
        return 0


def find_pal():
    t = open("input.txt", "r")
    t = t.read()
    t = t.split(" ")
    l = []
    for i in t:
        if palindrom(i):
            l.append(i)
    for i in l:
        f = open("output.txt", "a")
        f.write(i + "\n")
        f.close()


if __name__ == "__main__":
    find_pal()
