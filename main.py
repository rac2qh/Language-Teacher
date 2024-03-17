#!/Applications/.dce/python/python_3/bin/python3.9 

import time
import random

language = input("What language would you like to learn? " )
languagechoices = ["Bangla", "Spanish", "English", "Arabic"]
yes_or_no = input(f"The language you selected is {language}, is that correct? ")  
answer = ["yes", "no", "y", "n"]
if yes_or_no in answer: 
    print("ok")   
else: 
    print("Please select an answer")
if language in languagechoices: 
    print("Welcome I hope you learn something new today!")
else: 
    print(f"This answer is not in the list, please pick between the options that are taught here {languagechoices}")

def Bangla(): 
    print("Welcome to Bangla School")
    word_bank = {
    "house": "Gor",
    "dog": "Kukur",
    "cat": "Biṛāl",
    "car": "Gāṛī",
    "wife": "Bo",
    "husband": "Jamai",
    "light": "Ālō", 
    "bed": "Khāṭ",  
    "desk": "Ḍēska", 
    "door": "Darajā", 
    "glasses": "Shoshma", 
    "orphanage": "Ētimakhānā",
    "chair": "Cēẏāra", 
    "mom": "amu",
    "dad": "abu"
    } 
    # Add more word pairs as needed
    
    #score tracker
    num_questions = 10; 
    score = 0; 

    #rnadomly selects a bangla word, from the dictionry values, then the next line finds the corresponding english word for the randomly chosen bangla word using the helper function get_key_by_values
    bangla_word = random.choice(list(word_bank.values()))
    english_word = get_key_by_value(word_bank, bangla_word)
    print(f"\nBangla Word: {bangla_word}")

    # Display English word choices
    print("Choose the correct English word:")
    
    # Generate three random incorrect choices (ensure they are unique)
    incorrect_choices = random.sample(set(word_bank.keys()), 3)
    randomizer = incorrect_choices + [english_word]
    random.shuffle(randomizer)
    

    for i, choice in enumerate(randomizer, start=1):
        print(f"{i}. {choice}")

    #user_answer = input("Select the correct number: ")
    user_answer = input("Type the correct word: ")
    user_answer = user_answer.lower() 
    #validates answer is number and less than or equal to 4. 
    #if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        #this will always return true, it's not checking user answer at all
    if (list(word_bank.keys())[list(word_bank.values()).index(bangla_word)]) == user_answer:
        #if (list(word_bank.keys())[list(word_bank.values()).index(bangla_word)]) == english_word:
        #if the number you selected matches with the index of the english_word     
        print("Correct! 🎉")
    else:
        print(f"Wrong! The correct answer is: {english_word}")
    #else:
    #    print("Invalid input. Please enter a number between 1 and 4.")

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

# Your existing code for checking the language and calling Bangla() goes here.

Bangla()


#pick a subject, that subject wil have words for you to practice your vocab
#pick a word, and have to select the meaning of the word, multiple choice 
#works for both bangla and english

#practice commit and merge to main 
#https://stackoverflow.com/questions/42820840/how-to-push-changes-to-branch
#add this link 