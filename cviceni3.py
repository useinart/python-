def getMinValue(array):
    minimum = array[0][0]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] < minimum:
                minimum = array[i][j]
    return minimum


array = [[8,3,4],[4,5,6]]
print(getMinValue(array))