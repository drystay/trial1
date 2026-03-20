s = input('Enter a string of your choice\n')
alphabet = 0
vowel = 0

for i in s:
    if i in "aeiouAEIOU":
        vowel += 1
    elif i.isalpha():
        alphabet += 1
print("Vowels:", vowel)
print("Alphabets (excluding vowels):", alphabet)
