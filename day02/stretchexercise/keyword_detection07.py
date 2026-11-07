sentence = input("Enter sentence: ")
keyword = input("Enter keyword: ")

if keyword.casefold() in sentence.casefold():
    print("Keyword found")
else:
    print("Keyword not found")