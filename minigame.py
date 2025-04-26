'''
    Minigame Hub For Diferent Minigames In Python

    - User name is taken in and they are greeted.
    - They are asked to play any of the available games.
    - Once chosen, they can replay that game for as long as they like, or have a choice to switch games or logout.
    - The games included are: Hangman, Time Attack Mental Maths, Rock Paper Scissors PVC, Reaction Time Tester.
'''
import time
import random
import operator

def hangman():
    caategories_and_words = {'video_games': ['MINECRAFT', 'FORTNITE', 'TETRIS', 'OVERWATCH', 'PACMAN', 'ROBLOX', 'HALO' ], 
     'countries': ['AUSTRALIA', 'UKRAINE', 'BRAZIL', 'GERMANY', 'FRANCE', 'CANADA', 'ITALY', 'SWITZERLAND', 'MOROCCO'], 
     'movies': ['INCEPTION', 'TITANIC', 'GLADIATOR', 'FROZEN', 'JAWS', 'AVATAR'], 
     'animals': ['ELEPHANT', 'KANGAROO', 'CHEETAH', 'GIRAFFE', 'PENGUIN', 'OCTOPUS']
    }
    
    def get_input():
        while True:
            choice = input('Pick a category from: Video Games, Movies, Countries, Animals. ').lower()
            if choice not in ['video games', 'movies', 'countries', 'animals']:
                print('Invalid option, try again')
            elif choice == 'video games':
                return 'video_games'
            else:
                return choice
    def validate_guess(guessed_letters):
        while True:
            guess = input('Enter a letter: ')
            if len(guess) != 1:
                print('Please enter one letter')
            elif not guess.isalpha():
                print('This is not a letter, try again')
            elif guess in guessed_letters:
                print('Already used!')
            else:
                return guess
                
    def check_for_instance(guess, blurred_word):
        indexes = []
        for i in range(len(word)):
            if guess.upper() == word[i]:
                indexes.append(i)
        for index in indexes:
            blurred_word_list[index] = guess.upper()
        return indexes, blurred_word_list
                
    print('Welcome to Hangman!')
    time.sleep(0.75)
    print('I am thinking of a word, guess the word letter by letter, you have 9 tries')
    time.sleep(0.75)
    
    choice = get_input()
    
    word = random.choice(caategories_and_words[choice])
    blurred_word_list = ['_' for letter in word]
    
    lives = 9
    guessed_letters = []
    
    while lives > 0 and ''.join(blurred_word_list) != word:
        print(f'{lives}/9 lives left')
        print(f'Word: {"".join(blurred_word_list)}')
        
        guess = validate_guess(guessed_letters)
        guessed_letters.append(guess)
        
        indexes, blurred_word_list = check_for_instance(guess, blurred_word_list)
        
        if not indexes:
            lives -= 1
            print('Not in word!')
        else:
            print('Correct')
            continue
            
    if lives == 0:
        print('No lives left')
        print('Game Over, the answer was', word)
    else:
        print(word)
        print(f'Well done, you guessed it with {lives} lives left!')
        
def time_attack_maths():
    operators = {'*': operator.mul, '/': operator.floordiv, '+': operator.add, '-': operator.sub}

    def create_random_question():
        operator = random.choice(['/','-','+','*'])
        if operator == '*':
            a = random.randint(1, 12)
            b = random.randint(1, 12)
        elif operator == '/':
            b = random.randint(1, 12)
            result = random.randint(1, 12)
            a = b * result
        else:
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            
        question = f'{a} {operator} {b}'
        answer = operators[operator](a, b)
        
        return question, answer
        
    
    print('When you are ready, you will have 30 seconds to answer as many mental maths questions as you can!')
    input('Press enter to begin countdown: ')
    
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5)
    print('Start!')

    start_time = time.time()
    score = 0
    while time.time() - start_time < 30:
        question, answer = create_random_question()
        print(question)
        player_answer = input()
        try:
            int(player_answer)
            if int(player_answer) == answer:
                print('Correct!')
                score += 1
            else:
                print(f'Incorrect!, the answer was {answer}')
            
        except ValueError:
            print(f'Incorrect!, the answer was {answer}')

    print('Time is up, you answered', score, 'correctly!')

def rock_paper_scissors():

    def validate_choice():
        while True:
            choice = input(f'Choose from: {", ".join(choices).title()}, or enter r p s: ').lower()
            if choice.lower() == 'r':
                choice = 'rock'
            elif choice.lower() == 'p':
                choice = 'paper'
            elif choice.lower() == 's':
                choice = 'scissors'
                
            if choice not in ['rock', 'paper', 'scissors']:
                print('Not an option! try again')
            else:
                return choice

    print('Welcome to Rock Paper Scissors, press enter to play: ')
    input()

    player_score = 0
    computer_score = 0

    while player_score < 5 and computer_score < 5:
        choice_number_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
        choices = ['rock', 'paper', 'scissors']

        player_choice = validate_choice()
        player_choice_number = choice_number_dict[player_choice]
        computer_choice = random.choice(choices)
        computer_choice_number = choice_number_dict[computer_choice]

        if player_choice_number == computer_choice_number:
            game_message = 'Draw'
        elif ((player_choice_number - computer_choice_number) % 3) == 2:
            game_message = 'You lost'
            computer_score += 1
        else:
            game_message = 'You won'
            player_score += 1
        print(f'Computer chose: {computer_choice}. {game_message}')


        print(f'You: {player_score}, Computer: {computer_score}')

    winner_message = 'Congratulations! You' if player_score > computer_score else 'Better luck next time! Computer'

    print(winner_message, 'won!')

def reaction_game():
    print('Welcome to the Reaction Test Game!')
    print('Once you hit enter, wait for the \'GO!\' command and hit enter again as quick as you can!')
    input('Press enter to start countdown: ')
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5)
    print('Wait for command...')
    random_delay = random.uniform(1,5)
    time.sleep(random_delay)
    print('GO!')
    start_time = time.time()
    input()
    end_time = time.time()
    reaction_time = round(end_time - start_time, 2)
    if reaction_time == 0.0:
        print('You hit too fast! No score.')
    else:
        print(f'Your reaction time was {reaction_time} seconds!')

def get_game_choice():
    print('Enter either the name, or number choice of the game you would like to play, alternatively, type \'Exit\' to exit the hub: ')
   
    while True:
        game_choice = input().lower()
        if game_choice in ['1', 'rock paper scissors']:
            return '1'
        elif game_choice in ['2', 'reaction test']:
            return '2'
        elif game_choice in ['3', 'hangman']:
            return '3'
        elif game_choice in ['4', 'Mental Maths Time Attack']:
            return '4'
        elif game_choice == 'exit':
            return game_choice
        else:
            print('Invalid option, try again')
    

def ask_to_replay():
    print('Would you like to replay this game?')
    while True:
        replay_choice = input('Y/N: ').lower()
        if replay_choice in ['y', 'yes']:
            return True
        elif replay_choice in ['n', 'no']:
            return False
        else:
            print('I didnt quite get that, try again')


game_choices_dict = {'1': rock_paper_scissors, 
                     '2': reaction_game, 
                     '3': hangman, 
                     '4': time_attack_maths
                    }

exit_game = False

print('Welcome to the Minigame Hub!')
time.sleep(1)

while not exit_game:
    print('1) Rock Paper Scissors 2) Reaction Test 3) Hangman 4) Mental Maths Time Attack')
    game_choice = get_game_choice()
    if game_choice == 'exit':
        exit_game = True
        print('Have A Good Day!')
        continue
    else:
        replay_option = True
        while replay_option:
            if game_choice in game_choices_dict:
                game_choices_dict[game_choice]()
                time.sleep(0.5)
                replay_option = ask_to_replay()