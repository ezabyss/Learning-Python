# pydictionarys
from PyDictionary import PyDictionary

dict = PyDictionary()
print(" HELLO!! POCKET DICTIONARY")

word = input("Please Enter a word: ")
print(dict.meaning(word))

print("----- SYNONYM ------ ")
print(dict.getSynonyms(word))

print("----- ANTONYM ------ ")
print(dict.getAntonyms(word))