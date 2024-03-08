before = input("Input: ")

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for vowel in vowels:
    before = before.replace(f"{vowel}", "")

print(before)
