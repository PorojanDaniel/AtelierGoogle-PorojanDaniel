#cuvant = "a _ _ a _ _ t"
#alfabet
#word = "address"

import random
from random_word import list_of_random_word
word = random.choise(list_of_random_word)
word_list = []
unique_letter = set(word)
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item.lower())
        #if item in unique_letter:
         #   unique_letter.remove(item)
word_lenght = len(unique_letter) - 2
print(" ".join(word_list))
count_nr = 1
list_already_checked = []
new_word = " ".join(word_list)
while count_nr <= word_lenght + 1:
    user_letter = input("alege o litera: ").lower()
    if user_letter == "":
        print("introdu o litera")
    if user_letter in word_list:
        print("Litera dega afisata pe ecran")
    elif user_letter in list_already_checked:
        print(list_already_checked)
        print(f"litera a fost deja incercata , literele incercate sunt: {' '.join(list_already_checked)}")
    else:
        if user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))

        else:
            count_nr += 1
        if '_' not in "".join(word_list):
            print("ai castigat")
            break
        elif count_nr > 7:
            print(f"ai pierdut! Cuvantul era {word}")

        list_already_checked.append(user_letter)
