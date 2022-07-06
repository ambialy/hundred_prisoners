'''
Refer to the README.md for a description of the problem

07/05/2022 
Andy Bialy
https://github.com/ambialy/hundred_prisoners
'''


import random, argparse

parser = argparse.ArgumentParser(description='Solve the prisoner expirement')
parser.add_argument('-p', type=int,required=False, help='Number of prisoners, default=100')
parser.add_argument('-g', type=int,required=False, help='Number of guesses each prisoner gets, default=50')
parser.add_argument('-r', type=int,required=False, help='Number of runs, default=100')
args = parser.parse_args()

# Function to call for a prisoner to guess
def guess(box_dict, key, prisoner):
    # New guess is the value from the key, starting from the prisoners number
    new_guess = box_dict[key]
    if prisoner != new_guess:
        return new_guess
    else:
        return 'Got it'

outcome = []
def run(nPrisoners,nGuesses,nRuns):
    for _ in range(nRuns):

        # Set up a list with length of prisoners
        prisoner_list = [i+1 for i in range(nPrisoners)]
        # Set up dictionary keys
        box_key_list = [i+1 for i in range(nPrisoners)]
        box_value_list = [i+1 for i in range(nPrisoners)]
        random.shuffle(box_value_list)
        box_dict = {}

        # After shuffling values, zip them together
        # i.e. {1:44, 2:51, 3:19 .... 97:14, 98:1, 99:69}
        for key, val in zip(box_key_list, box_value_list):
            box_dict[key] = val

        # Keep tally of the prisoners that have guessed and those that found their number
        nPrisoners_that_guessed = 0
        nPrisoners_correct = 0

        # Guesses is a list that the first one is the prisoners number and gets
        # updated with the value of the new_guess and each value is called with the
        # value of i for each loop. 

        while nPrisoners_that_guessed <= len(prisoner_list) - 1:
            guesses = [prisoner_list[nPrisoners_that_guessed]]
            for i in range(nGuesses):
                guess_val = guess(box_dict, guesses[i], prisoner_list[nPrisoners_that_guessed])
                if guess_val == 'Got it':
                    nPrisoners_correct += 1
                    break
                guesses.append(guess_val)
            nPrisoners_that_guessed += 1
        outcome.append(nPrisoners_correct)

    # Find the percentage of how many groups of prisoners made it out  
    escaped = 0
    for tot in outcome:
        if tot == 100:
            escaped += 1
    perc = escaped / len(outcome)
    print(f'Percent of time all {nPrisoners} prisoners were correct with {nGuesses} guesses over {nRuns} runs:')
    print(f'{perc*100}%')

def main():
    # Set default if none are specified
    nPrisoners=100
    nGuesses=50
    nRuns=100
    if args.p:
        nPrisoners = args.p
    if args.g:
        nGuesses = args.g
    if args.r:
        nRuns = args.r
    run(nPrisoners,nGuesses,nRuns)


if __name__ == '__main__':
    main()
