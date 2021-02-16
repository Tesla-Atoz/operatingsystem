def recurse(files):
    flag = 0

    print("Enter the starting block and length of files:")
    startBlock, length = list(map(int, input().split(" ")))

    for i in range(startBlock, startBlock+length):
        if files[i] == 0:
            flag += 1

    if (length == flag):
        for k in range(startBlock, startBlock+length):
            if files[k] == 0:
                files[k] = 1
                print(k, files[k])
        if k != (startBlock+length-1):
            print("The file is allocatied to disk")
        else:
            print("Not allocated")

        print("Do u want to enter more files")
        ch = int(input())
        if ch:
            recurse(files)
            break

    return


if __name__ == "__main__":
    files = [0] * 50
    recurse(files)
