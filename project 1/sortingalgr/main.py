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
def insertion_sort(list):
    #average of 126 tries with 20 items
    global rounds
    n = len(list)
    for i in range(n):
        key = list[i]

        j = i-1
        while j >= 0 and key < list[j]:
            rounds +=1
            list[j+1]=list[j]
            j-=1

        list[j+1] = key
    return list
def selection_sort(list):
    #average of 43 tries with 20 objects
    global rounds
    n = len(list)
    for i in range(n):
        minum = i
        for j in range(i+1, n):
            if list[minum] > list[j]:
                minum = j
                rounds +=1

        list[i],list[minum] = list[minum], list[i]
    return list
def mergeSort(list):
    #average of 78 tries with 20 objects
    global rounds
    if len(list) > 1:
        mid = len(list) //2
        L=list[:mid]
        R=list[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i < len(L) and j< len(R):
            rounds +=1
            if L[i] < R[j]:
                list[k] = L[i]
                i+=1
            else:
                list[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k +=1
        while j < len(R):
            list[k] = R[j]
            j+=1
            k+=1
    return list
def randomSort(list):
    global rounds
    for i in range(len(list)):
        # for j in range(i+1,len(list)):
        rounds += 1
        x = random.choice(list)
        y = random.choice(list)
        if x < y:
            z = list.pop(x-1)
            list.insert(0,z)
        elif y < x:
            z = list.pop(y-1)
            list.insert(0, z)
    return list


array = []
colorsIndex = ["red","orangishRed","redOrange","RedishOrange","orange","yellowishOrange","orangeyellow","orangishYellow","yellow","GreenishYellow","uglylime","YellowishGreen","green","Greendigo","indigo","Seanigo","blue","DarkishBlue","darkblue","RedishBlue","purple","magenta","violet"]
colors = []
for i in range(len(colorsIndex)):
    array.append(i+1)
#
# random.shuffle(array)
# for i in range(len(array)):
#     x = array[i]
#     colors.append(colorsIndex[x-1])
# print(array)
# print(colors)
random.shuffle(array)
print(array)
array = randomSort(array)
for i in range(len(array)):
    x = array[i]
    colors.append(colorsIndex[x-1])
print(array)
print(colors)
print(rounds)
total = 0
n = 1000
for i in range(n):
    rounds = 0
    random.shuffle(array)
    array = randomSort(array)
    total += rounds
average = total // n
print(average)
