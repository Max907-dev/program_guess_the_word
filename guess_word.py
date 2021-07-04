def points(word, guess): # I have problem with counter
    p = 0
    for i in range(len(word)):
        if word[i] == guess:
            p += 1
        else:
            p -= 1

def maskWord(state, word, guess):
    state = list(state)
    for i in range(len(word)):
        if word[i] == guess:
             state[i] = guess
    return ''.join(state)

import os
word = str(input('Make a word '))
os.system('cls')
state = '_' * len(word)
tries = 0
points = 0
play = True

while play:
    if tries == len(word)*3: #number of attempts
        print ('Fail ')
        play = False
    guess = input('Name the letter: ')
    points = points + 1
    for j in range(len(word)):
        if guess == word[j]:
            print('there is such a letter')
            break
        if guess != word[j]:
            print('No the letter')
            break
    tries += 1
    state = maskWord(state, word, guess)
    print (state)
    print("Number of points scored: ", points)

    if maskWord(state, word, guess) == word:
        print ('You win!')
        play = False
