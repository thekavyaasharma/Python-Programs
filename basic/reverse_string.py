# rerse string "hello" : "olleh"

# using for loop
user_input = input("Enter string: ")
rev =""

for ch in user_input:
    rev = ch + rev

print(f'String: {user_input} \nReversed string: {rev}')


