# #TODO: Create a letter using starting_letter.txt 
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
    
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# HOLD = "[name]"

# with open("./Input/Names/invited_names.txt", "r") as names:
#     # name_list = names.read()
#     list_all = names.readlines()
#     raw = list_all.strip("\n")
#     print(raw)


#     # print(list)
 
    
# # print(invitee)
    
    
# letter_full = []
# with open("./Input/Letters/starting_letter.txt", "r") as note:
#     letter = note.read()
#     for name in list_all:
#         name.strip("\n")
#         x = letter.replace(HOLD, name)
#         letter_full.append(x)
    
#     for i in letter_full:
#         print(i)
#         with open(f"./Output/ReadyToSend/Lee to {name}.txt", "w") as sender:
#             sender.write(i)
#     #     letter_full.append(x)
#     # print(letter_full)
       
# # for name in invitee:
# #     y = 2
    

    

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)