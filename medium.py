# medium 2
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
import sys
def morethanNBy3(arr, n):
    count1 = 0
    count2 = 0
    first = sys.maxsize
    second = sys.maxsize

    for i in range(0, n):     # if the element is seen previously then increment it by count1.
        if (first == arr[i]):
            count1 += 1
                               # if the element is seen previously then increment it by count2
        elif (second == arr[i]):
            count2 += 1

        elif (count1 == 0):
            count1 += 1
            first = arr[i]

        elif (count2 == 0):
            count2 += 1
            second = arr[i]
                   # if current element is different from both the previously seen variables, decrement both the counts.
        else:
            count1 -= 1
            count2 -= 1

    count1 = 0
    count2 = 0

    #now traverse the array and find the actual counts.
    for i in range(0, n):
        if (arr[i] == first):
            count1 += 1

        elif (arr[i] == second):
            count2 += 1

    if (count1 > n / 3):
        return first

    if (count2 > n / 3):
        return second

    return -1


# example 1
nums = [3,2,3]
n = len(nums)
print(morethanNBy3(nums, n))

#example 2
num = [1]
n = len(num)
print(morethanNBy3(num,n))

