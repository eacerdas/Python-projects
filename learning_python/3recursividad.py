def recur(num):

    if num == 1:
        return 1
    else:
        return num + recur(num-1)

print(recur(5))