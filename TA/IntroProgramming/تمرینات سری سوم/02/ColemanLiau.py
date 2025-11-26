def coleman_liau():
    txt = open("input.txt", "r")
    txt = txt.read()
    l = txt.split(" ")
    h = txt.split(".")
    let = 0
    for i in l:
        let += len(i)
    s = len(h) / len(l) * 100
    l = let / len(l) * 100
    return int(0.0588 * l - 0.296 * s - 15.8) + 1


if __name__ == "__main__":
    coleman_liau()
