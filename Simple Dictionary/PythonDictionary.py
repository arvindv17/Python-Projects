"""
This program is to take a user input and return the Dictionary result based on a json that already contains the result
__author__ = Arvind
__Date__ = 09/18/2017
"""
import os
import glob2
import json
from difflib import get_close_matches


filename = glob2.glob("*.json")

for file in filename:
    data=json.load(open(file))

def dictionary(word):

    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s? Enter Y or N : " % get_close_matches(word,data.keys())[0]).lower()
        if yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="n":
            return "Word does not exist, Please double check."
        else:
            return "We did not understand the input you provided."

    else:
        return "The word does not exist in this dictionary. Please try again"

word = input("Enter the word to be searched :").lower()
output =dictionary(word)

if type(output)==list:
    for item in output:
        print(item)

else:
    print(output)