def initArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = i * j
    return array

array = [ [ 1, 2, 3, 4, 5, 6, 7, 8] ,[ 1, 2, 3, 4, 5 ] ]
print(initArray(array))