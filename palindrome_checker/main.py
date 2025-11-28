user_phrase = input("Enter phrase that you want to verify for palindrome : ")

user_phrase = user_phrase.lower().replace(" ","")

if user_phrase == user_phrase[::-1]:
    print("The phrase you entered is a palindrome.")
else:
    print("No , the phrase you entered is not a palindrome")