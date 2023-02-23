# ==========================================================
# BASIC LISTS
# ==========================================================

# FIND THE LARGEST NUMBER

# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]

# for item in numbers:
#     if item > max:
#         max = item
# print(max)



# ==========================================================
# 2D LISTS
# ==========================================================

# 3 x 3 Matrix
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)



# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

numbers = [2 ,2,4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)