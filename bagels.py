import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''' Bagels, a deductive logic game. 
          By: Al Sweigart al@inventwithpython.com
          
          I am thinking of a {}-digit number with no repeating digits. 
          Try to guess what it is. Here are some clues:
          
          When I say:       That means:
            Pico            One digit is correct but in the wrong position.
            Fermi           One digit is correct and in the right position.
            Bagels          No digit is correct.
            
        For example, if the secret number was 248 and your guess was 843, the 
        clues would be Fermi Pico'''.format(NUM_DIGITS))
    
    while True:
        # Main game loop
        # Store the secret number the player needs to guess.
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until the player enters a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input()
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                # secretNum was guessed so break out of the loop.
                break
                
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    
    print('Thanks for playing!')
    
# Return a string made up of NUM_DIGITS unique random digits.
def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        
    return secretNum

# Returns a string with the appropriate PIco Fermi Bagels clues
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
            
    if len(clues) == 0:
        return 'Bagels'
    else:
        # Sort the clues so they don't give away any information.
        clues.sort()
        return ' '.join(clues)
    
# If the program is run (instead of imported), run the game.
if __name__ == '__main__':
    main()