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
    correct_answer = random.choice(list(word_bank.values()))
    english_word = get_key_by_value(word_bank, correct_answer)
    print(f"\nBangla Word: {correct_answer}")

    # Display English word choices
    print("Choose the correct English word:")
    print(f"1. {english_word}")
    
    # Generate three random incorrect choices (ensure they are unique)
    incorrect_choices = random.sample(set(word_bank.keys()) - {english_word}, 3)
    random.shuffle(incorrect_choices)
    randomizer = incorrect_choices + [english_word]
    

    for i, choice in enumerate(incorrect_choices, start=2):
        print(f"{i}. {choice}")

    user_answer = input("Select the correct number: ")

    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        selected_word = incorrect_choices[int(user_answer) - 2] if int(user_answer) >= 2 else english_word

        if selected_word == english_word:
            print("Correct! 🎉")
        else:
            print(f"Wrong! The correct answer is: {english_word}")
    else:
        print("Invalid input. Please enter a number between 1 and 4.")

def get_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key

# Your existing code for checking the language and calling Bangla() goes here.

# Example usage
Bangla()


#pick a subject, that subject wil have words for you to practice your vocab
#pick a word, and have to select the meaning of the word, multiple choice 
#works for both bangla and english

#practice commit and merge to main 
