def recursel(files):

    indBlock = int(input())

    if files[indBlock] != 1:
        print("Enter the number of blocks ")
        n = int(input())
    else:
        print(indBlock + "is already allocated")
        recursel(files)

    recure2(files, n, indBlock)


def recure2(files, n, indBlock):
    flag = 0
    indexBlock = []
    for i in range(n):
        indexBlock[i] = int(input())
        if files[indexBlock[i]] == 0:
            flag += 1

        if flag == n:
            for j in range(n):
                files[indexBlock[i]] = 1
                print("Allocated")
                print("File indexed")
                for k in range(n):
                    print("%d--------->%d:%d".format(indBlock,
                                                     indexBlock[k], files[indexBlock[k]]))
        else:
            print("File is alredy allocated")
            print("enter other index file")
            recurse2(files, n, block)


if __name__ == "__main__":
    files = [0]*50
    recursel(files)
