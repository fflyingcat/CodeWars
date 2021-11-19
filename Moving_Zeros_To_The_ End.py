def move_zeros(array):
    arr = []
    zeros = []
    for i in range (0,len(array)):
        if (array[i]!=0):
            arr.append(array[i])
        else:
            zeros.append(array[i])
    for i in range (0,len(zeros)):
        arr.append(zeros[i])
    return arr
#https://www.codewars.com/kata/52597aa56021e91c93000cb0