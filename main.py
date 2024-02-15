student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

word_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dic = {row.letter: row.code for (index, row) in word_data.iterrows()}
print(new_dic)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
right_answer = True

while right_answer:
    try:
        # Here with the help of try function to catch if user accidentally type number instead of text
        # which can throw KeyError
        word = input("Enter a word: ").upper()
        output_list = [new_dic[new_item] for new_item in word]
    except KeyError:
        # If user enter other than letter then this block will run and tell the user to input correctly
        print("sorry, only letters can be used as input")
    else:
        # if user entered correct input then this block will run after try block and show the output
        print(output_list)
        right_answer = False
