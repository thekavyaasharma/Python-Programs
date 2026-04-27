# rerse string "hello" : "olleh"

# using for loop
user_input = input("Enter string: ")
rev =""

for ch in user_input:
    rev = ch + rev

print(f'String: {user_input} \nReversed string: {rev}')


# using recursion: fxn calling itself until base condn satisfied
def rev_string(s):
    if len(s) ==1 :
        return s
    return rev_string(s[1:])+s[0]

st = input("ENTER STRING TO REVERSE USING RECURSION: ")
rev = rev_string(st)
print(f"Reversed String is: {rev}")

