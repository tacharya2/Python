string = input("Enter your word: ")
#make your string a caseless
string = string.casefold()
# get its reverse
reverse = reversed(string)
if list(string)==list(reverse):
    print(string," is palindrome")
else:
    print(string," not a palindrome")
