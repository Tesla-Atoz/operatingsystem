def Search(arr, x):
    if x in arr:
        return 1
    return 0


if __name__ == "__main__":
    print("Enter the number of frames")
    frames = int(input())

    x = [-1]*frames

    print("Enter the number of page slots")

    n = int(input())

    string = []
    print("Enter pages slots")
    for i in range(n):

        value = int(input())
        string.append(value)

    pos = 0
    pf = 0
    for i in range(n):
        if (Search(x, string[i]) != 1):
            x[pos] = string[i]
            pos = (pos+1) % frames
            pf += 1

    print("Total page faults ", pf)
