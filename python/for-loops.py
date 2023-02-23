# ==========================================================
# BASIC FOR LOOPS
# ==========================================================

# prices = [10, 20, 30]
# total = 0

# for item in prices:
#     total += item
#     print(f'Iterated Total: {total}')



# ==========================================================
# NESTED FOR LOOPS
# ==========================================================

# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')



# ==========================================================
# CHALLENGES/ACTIVITIES
# ==========================================================

# Expected output

# X X X X X
# X X
# X X X X X
# X X 
# X X 
# X X 

numbers = [5, 2, 5, 2, 2]
number_x = ''

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# Modifying the list modifies the output