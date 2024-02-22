# marks = []
# system_select = int(input("Select you marks system: "))
# while True:
#     create_marks = int(input("Enter mark: "))
#     if create_marks == 0:
#         break
#     elif create_marks > system_select or create_marks < 0:
#         print("nonononono")
#     else:
#         marks.append(create_marks)
#
# print(*marks)

from random import randint

list = []
negat = 0
odd = 1
even = 1
index3 = 1

for i in range(randint(10, 30)):
    list.append(randint(-100, 100))

for i in range(len(list)):
    if list[i] < 0:
        negat = negat + list[i]

for i in range(len(list)):
    if list[i] % 2 == 0:
        even = even * list[i]
    else:
        odd = odd * list[i]

for i in range(len(list)):
    if i % 3:
        index3 = index3 * list[i]

min_numb = list.index(min(list))
max_numb = list.index(max(list))
minmax = 1

for i in range(len(list[min_numb+1:max_numb])):
    minmax = minmax * list[min_numb+1:max_numb][i]

print("\nNegative:", negat, "\nEven:", even, "\nOdd:", odd, "\nIndex 3:", index3, "\nMinMax:", minmax)
