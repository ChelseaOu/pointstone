import random
import string

WORDLIST_FILENAME = "words.txt"
letters_list = "input"
available_letters_list = "list"
available_letters_string = "string"
n = 6
underscores = "_"
letter_guessed = "letter"
secret_word_ = "secret"
word_list = "list"
letters_fit = 0
x = 0
a = 0

def load_words(filename):

    print("Loading word list from file...")
    inFile = open(filename, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)
    

wordlist = load_words(WORDLIST_FILENAME)


def is_word_guessed(secret_word):

	global letters_fit

	if letters_fit == len(secret_word):
		return True

	else:
		return False

def not_a_letter(letter):
    global a 
    global n 
    global underscores

    if str.isalpha(str.lower(letter)) == False: 

        if letter != "*":
            while a<3:
                a += 1
                print "Oops! That's not a valid letter. You have", (3-a), "warnings left."
                print """
                    You have %r guesses left.
                    %r
                    """ %(n, "".join(underscores))
        
                letter = raw_input("Please guess a letter:")

                global letter_guessed
                letter_guessed = letter
        

        else:
            show_possible_matches(underscores, wordlist)

def get_a_word(guessed_word, letter):
    global underscores
    underscores = list(underscores)
    global available_letters_string
    global n 

    position = guessed_word.find(letter)

    if position != -1 :

        word_list = list(guessed_word)
        word_list[position] = "_"
        guessed_word = "".join(word_list)
        global secret_word_
        secret_word_ = guessed_word
        underscores[position] = letter
        underscores = "".join(underscores)
        print "Good guess:",underscores
        global letters_fit
        letters_fit += 1

    elif available_letters_string.find(letter) == -1 and string.ascii_lowercase.find(letter) != -1:
        a += 1
        print """
              Oops! You have already guessed that letter. You have %r warnings left.
              %r
              """ %(n,"".join(underscores))

    elif letter == "*":
        pass

    else:
        print """
              Oops, that letter is not in my word.
              """, "".join(underscores)
    


def get_guessed_word(guessed_word, letter):
    
    a = 0
    global n

    not_a_letter(letter)


    if a == 3 and str.isalpha(str.lower(letter))==False:  
        print "You ran out of guesses. The word was", guessed_word
        exit(1)

    consonants = "bcdfghjklmnpqrstuvwxyz"

    get_a_word(guessed_word, letter)


    if consonants.find(letter):
    	n -= 1

    else :
    	n -= 2


    print "_"*8


def get_available_letters(letters_guessed):

	if available_letters_string.find(letters_guessed) == -1 and string.ascii_lowercase.find(letters_guessed) == -1:
		pass

	else:
		global available_letters_list
		available_letters_list.remove(letters_guessed)
		global available_letters_string
		available_letters_string = "".join(available_letters_list)
		return available_letters_string

def positions(my_word,other_words):
	global x
	x = 0
	words_list = list(other_words)
	if len(words_list) == len(my_word):
		for letter in list(my_word):
			if letter != "_":
				if words_list[my_word.find(letter)]== letter:
					x += 1
			else:
				words_list[other_words.find(letter)] = "_"
				x += 1



					

def match_with_gaps(my_word, other_word):
    
    
    positions(my_word,other_word)

    n_of_blanks = my_word.count("_")

    global x

    if x == len(my_word):
        return True

    else:
        False



def show_possible_matches(my_word, other_word):
   
    for possible_matches in other_word:
        if match_with_gaps(my_word, possible_matches):
            print possible_matches


def letters_more_than_one(secret_word):


    for letter in secret_word:

        if secret_word.count(letter)>1:
            return letter*(secret_word.count(letter)-1)

        else:
            continue

def total_score(t,secret_word):

        kinds_of_letters = len(list(set(secret_word)))
        total_score = t*kinds_of_letters
        return total_score

def original_letters(word):
    global available_letters_list
    global available_letters_string
    global secret_word
    global letters_list

    available_letters_list = list(string.ascii_lowercase)
    available_letters_list.insert(0,letters_more_than_one(word))  
    available_letters_string = ''.join(available_letters_list)
    letters_list= []

def final_result(secret_word):
	global n 
	if is_word_guessed(secret_word):
		print """
              Congratulations, you won!
              Your total score for this game is :
              """,total_score(n,secret_word)

	else:
		"Sorry, you ran out of guesses. The word was", secret_word


def hangman_with_hints(secret_word):
   
    print """
          Welcome to the game Hangman!
          I am thinking of a word that is %r letters long.
          _ _ _ _ _ _ _ _ 
          """ %len(secret_word)

    global word_list
    word_list = list(secret_word)
    global secret_word_
    secret_word_ = secret_word

    global underscores
    underscores = ["_"]*len(secret_word)

    global n
    n = 6

    original_letters(secret_word)
    
    while n > 0 and is_word_guessed(secret_word) == False:

        print """
              You have %r guesses left.
              Available letters : %r
              """ %(n,available_letters_string)

        global letter_guessed 
        letter_guessed = raw_input("Please guess a letter:")
        letters_list.append(letter_guessed)

        global letters_list
        
        get_guessed_word(secret_word_,letter_guessed)

        get_available_letters(letter_guessed)

	is_word_guessed(secret_word)
	final_result(secret_word)


hangman_with_hints(choose_word(wordlist))



 