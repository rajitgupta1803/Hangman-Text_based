import random

err = True
attempts = 7

list_of_words = []
word_in_file = []

def open_file(name, access_mode):
    global word_in_file
    file = open(f"{name}.txt", access_mode)
    word_in_file = file.readlines()
    file.close()

open_file("words", "r")

for n in word_in_file:
    list_of_words.append(n.strip())

rand_word = random.choice(list_of_words)
original = rand_word.upper()
orig_list = list(original)
targ_list = list(original)

# make the target list with blanks
vowels = ["A", "I", "E", "O", "U"]
for j in range(len(original)):
    for c in vowels:
        if c != orig_list[j]:
            targ_list[j] = "_"
        elif c == orig_list[j]:
            targ_list[j] = c
            break


# prints the target list as a word
def print_list():
    for m in targ_list:
        print(m, end=" ")
    print()


# makes the changes to the list of user is right or give error otherwise
def main_logic():
    global err, attempts
    inp = str.upper(input("Enter some letter you think is correct: "))
    print()
    # checks if input is there in the original list and adds the letter to the target if it is
    if inp in orig_list and inp not in targ_list:
        for i in range(len(targ_list)):
            if orig_list[i] == inp:
                targ_list[i] = inp
                err = False
        # if the input is correct, it will print this
        if not err:
            print("Yes, you are correct!")
    # If the input letter is already there
    elif inp in targ_list and orig_list:
        print(f"See carefully, {inp} is already there!")
    # To give error if the input wasn't correct
    else:
        print("Nope, you are wrong")
        attempts -= 1
        print(f"Attempts left: {attempts}")
        print()
        # Quit if attempts are over
        if attempts == 0:
            print(f"Oops, your attempts are over! \nBetter luck next time! \nThe word was {original}")
            quit()
    print_list()
    print()


print_list()  # prints the list once in the beginning

while "_" in targ_list:
    main_logic()

print(f"Bravo! You have correctly guessed the word! \nThe word was {original} \nYou had {attempts} attempts left!")
print("Thanks for playing!")

