def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


with open('sunset.txt', 'r') as fin, open('common.txt', 'w') as fout:
    arr = fin.readline().strip('\n').split('; ')
    arr2 = fin.readline().strip('\n').split('; ')
    arr3 = intersection(arr, arr2)
    for i in range(len(arr3)):
        arr3[i] = arr3[i].capitalize()
    print(*arr3, sep="\n", file=fout)
