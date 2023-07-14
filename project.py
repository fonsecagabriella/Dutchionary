import dutchonary #import library that acts as a dictionary
import json
import re
import cowsay
import os

def main():
    # clean terminal
    os.system("clear")
    # gets user word
    w = input("What's the word? ")

    #checks if input is valid
    if is_valid(w):
        p = dutchonary.return_prompt(w) # returns prompt answer based on user input
        # check if it can be converted to JSON
        if is_valid_dic(p):
            print_definition(p) #prints definition of word
            zin = input("\n\nNow that you know the word, try to write a sentence with it: ") #asks user to write a sentence
            dutch_cow(zin) #correct user sentences
        else:
            print("Error! Are you sure you used a Dutch word? Try again.")
    else:
        print("Your input was not a valid word. REMEMBER: numbers are not allowed, only letters and spaces!")

   # print(return_webcall(w)) #test return of a webcall


def is_valid(str):
#this function checks if the string is valid
    try:
        #remove spaces
        str = str.strip()
        if len(str)  == 0:
            raise ValueError("Input cannot be zero")
        elif len(str) > 40:
            raise ValueError("Input is too long")
        elif not check_spaces_letters(str):
            raise ValueError("Only letters and spaces are allowed")
        else:
            return True
    except Exception:
        return False

def check_spaces_letters(str):
# this function makes sure the string contains only letters and spaces
    if not re.match("^[A-Za-z ]+$", str) == None:
        return True
    else:
        return False

def is_valid_dic(str):
# this function checks if a string can be converted to JSON format
    try:
        dic = json.loads(str)
        #print(dic)
        if not dic["meaning"] == "NOT_FOUND":
            return True
        else:
            return False
    except (ValueError, TypeError, KeyError):
        return False

def print_definition(string):
    # you receive string, need to convert to dictionary
    list_def = json.loads(string)

    print(f"\n\n|----------------------------------|\n")
    #print the definition
    for item in list_def:
        if not item.upper() == "WORD": # I want the first line to be in CAPS
            print(item.capitalize(), list_def[item].capitalize(), sep=": ")
        else:
            print(item.upper(), list_def[item].upper(), sep=": ")
    print(f"\n\n|----------------------------------|\n\n")

def return_webcall(s):
# returns the web call for string s
    try:
        p = dutchonary.return_prompt(s) #get prompt for string

        if is_valid_dic(p): #if answer is a valid d
            #check if return is valid dictionary
            list_def = json.loads(p)
            return list_def
        else:
            return "There was an error"
    except Exception:
        return ("Something is not right. Try again later 😢")

def check_sentence(s):
    try:
        return(dutchonary.correct_zin(s))
    except Exception:
        return("There was a problem. Try again later! 😢")

def dutch_cow(zin):
#for fun, let the cow correct the sentence in Dutch
    correct = check_sentence(zin)
    return cowsay.cow(correct)

if __name__ == "__main__":
    main()
