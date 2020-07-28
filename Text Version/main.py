import time
import random

def read_words(file_name, words):
	f = open(file_name, "r")
	lines = f.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].strip('\n')
	return lines

def del_word(word, lista):
	for i in range(len(lista) - 1):
		if lista[i] == word:
			lista.remove(word)

def split(word): 
    return ["_" for char in word]

def print_man(num, word):

	if num == 1:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |      \n"
              " |       \n"
              " |       \n"
              " |       \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 2:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |       \n"
              " |       \n"
              " |       \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 3:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |       \n"
              " |       \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 4:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |     |  \n"
              " |       \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 5:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |    /|  \n"
              " |        \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 6:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |    /|\\  \n"
              " |        \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 7:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |    /|\\  \n"
              " |    /  \n"
              "_|_      \n")
		print(f"Wrong guesses: {num}")
		print("Try again!\n")
		return 0

	if num == 8:
		print("  _____  \n"
              " |     | \n"
              " |     | \n"
              " |     | \n"
              " |     O  \n"
              " |    /|\\  \n"
              " |    / \\  \n"
              "_|_      \n")
		print(f"Better luck next time! The word was {word}")
		return 1


words = []
run = True
total_count = 0

words = read_words("Words.txt", words)

#Choose a word from the list
word = random.choice(words)
del_word(word, words)

guess_word = split(word)

print("\n-----Game Ready-----\n")

while run:
	count = 0
	flag = 0
	print(guess_word)
	guess = input("Letter to guess: ")
	print('\n')

	size = len(guess_word)

	for i in range(len(word)):
		if guess == word[i]:
			guess_word[i] = guess
			flag = 1 #if flag = 0, guess was wrong

	#check if guess wasnt right!
	if flag != 1:
		total_count += 1
		if print_man(total_count, word) == 1:
			run = False



	for i in guess_word:
		if i != '_':
			count += 1

		if count == size:
			print(f"The word was: {word}\n")
			print("\n-----Congratulations, you WIN!-----\n")
			run = False

