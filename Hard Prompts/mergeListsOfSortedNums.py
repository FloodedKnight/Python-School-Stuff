# Write a function that merges k sorted linked lists into one sorted linked list. The input will be a list of k linked lists, each of which is already sorted in ascending order.
# Input: lists = [[1,4,5], [1,3,4], [2,6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]


list = [
    [1,4,5],
    [1,3,4],
    [2,6]
]

singleList = [a for i in list for a in i]
singleList.sort()
print(singleList)
