import random
global rounds
rounds = 0
def bubble(list):
    # average of 181 rounds with 20 items
    global rounds
    n = len(list)
    for i in range(n):

        sorted = True
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

                sorted = False
            rounds += 1
        if sorted:
            break
    return list
def quicksort(list):
    #average of 13 tries with 20 items
    global rounds
    if len(list) < 2:
        return list

    rounds += 1
    low = []
    same = []
    high = []
    pivot = random.choice(list)

    for item in list:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)


    return quicksort(low) + same + quicksort(high)


array = []
for i in range(20):
    array.append(i+1)

random.shuffle(array)
print(array)
array = quicksort(array)
print(array)
print(rounds)


# total = 0
# n = 15000
# for i in range(n):
#     rounds = 0
#     random.shuffle(array)
#     array = quicksort(array)
#     total += rounds
# average = total / n
# print(average)
# def random_pick(list):
#     n = len(list)
#     used = []
#     for i in range(n):


#         yes = True
#         while yes:
#             item = random.choice(list)
#             if item in used:
#                 continue
#             else:
#                 itemtwo = random.choice(list)
#                 if itemtwo == item:
#                     continue
#                 else:
#                     yes = False
#         index = list.index(item)
#         indextwo = list.index(itemtwo)
#         if item > itemtwo:
#             if index > indextwo:
#                 continue
#             else:
#                 list[index], list[indextwo] = list[indextwo],list[index]
#     return list


