string = input("Enter a string: ")
string = string.lower()
vowels = "aeiou"
string = input("Enter a string: ")

#lowercase for case insensitivity
string = string.lower()

#vowels
vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for char in string:
    if char.isalpha():  
        if char in vowels:  
            vowel_count += 1
        else:  
            consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
