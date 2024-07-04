#1

string1 = input("Enter the string: ")
if string1 == string1[::-1]:
  print("The entered string is a palindrome")
else:
  print("The entered string is not a palindrome")

#2

text = input("Enter the text: ")
reservedwords = input("Enter a list of reserved words separated by commas: ").split(',')
for i in text.split():
 if i.lower() in reservedwords:
   text = text.replace(i, i.upper())
print(text)

#3

text1 = input("Enter the text: ")
num = text1.count('.') + text1.count('!') + text1.count('?')
print(f"Number of sentences in the text: {num}")