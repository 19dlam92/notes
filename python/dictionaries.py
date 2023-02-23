# ==========================================================
# DICTIONARIES
# ==========================================================

# customers = {
#     'name' : 'John Smith',
#     'age' : 30,
#     'is_verified' : True
# }

# # CASING MATTERS
#     # it'll throw KEY.ERROR
#     # to bypass this use 
#         # print(customers.get('name'))
# print(customers['name'])



# ==========================================================
# CHALLENGES/ACTIVITIES
# ==========================================================
phone_number = str(input('Phone: '))

digits_mapping = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}

output = ''
for digit in phone_number:
    output += digits_mapping.get(digit, '!') + ' '

print(output)