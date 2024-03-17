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
    
    # Generates list of answer choices
    for i, choice in enumerate(randomizer, start=1):
        print(f"{i}. {choice}")
    user_answer = input("Type the correct word: ")
    user_answer = user_answer.lower() 
    #checks if user_answer == bangla_words key value
    if (list(word_bank.keys())[list(word_bank.values()).index(bangla_word)]) == user_answer:  
        print("Correct! 🎉")
    else:
        print(f"Wrong! The correct answer is: {english_word}")
#populates dictionary
def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

#method call
Bangla()