numvow = 0
s = input("Word: ")
#azcbobobegghakl
for charachter in s:
    if charachter in ['a','e','i','o','u','A','E','I','O','U']:
        numvow +=1
print("Number of vowels: " + str(numvow))
k = input("END")
