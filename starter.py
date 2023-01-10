import pyjokes
import art
import random
from imdb import Cinemagoer
import tqdm
import json


def menu() -> str:
    """User interface menu"""
    action = input('1. Tell a joke\n'
                   '2. Suggest a movie\n'
                   '3. Suggest a song\n'
                   '4. Let\'s play \'Guess a number\'\n'
                   '5. Let\'s play \'rock-paper-scissors\'\n'
                   '6. Exit\n'
                   'Choose an action: ')
    return action


def main(user_choice: str):
    """Main controller"""
    match user_choice:
        case '1':
            return joke()
        case '2':
            return movie()
        case '3':
            return song()
        case '4':
            return number_guess()
        case '5':
            return rock_paper_scissors()
        case '6':
            print('Thanks, bye!')
            return False


def number_guess() -> bool:
    """A simple game to guess numbers"""
    my_number = random.randint(1, 100)
    print('I am thinking of a number...')
    while True:
        user_guess = int(input('What is my number?: '))
        if my_number == user_guess:
            art.tprint('Winner-winner chicken dinner')
            again = input('You are correct! Play again [y/n]?: ')
            if again == 'y':
                number_guess()
            else:
                return True
        elif user_guess > my_number:
            print('My number is lower! Try again')
        elif user_guess < my_number:
            print('My number is higher! Try again')


def song() -> bool:
    """Suggests a song"""
    art.tprint('SUGGEST-A-SONG 3000')
    print('Let me think...')
    for _ in tqdm.tqdm(range(10000000), colour='#b3b3b3'):
        pass
    with open('songs.json', 'r') as f:
        songs = json.loads(f.read())
        song_choice = random.choice(songs['songs'])
        print(f'How about {song_choice["title"]} by {song_choice["artist"]}?')
    return True


def movie() -> bool:
    """Suggests a movie """
    art.tprint('SUGGEST-A-MOVIE 2000')
    print('Let me think...')
    for _ in tqdm.tqdm(range(10000000), colour='#b3b3b3'):
        pass
    ia = Cinemagoer()
    movies = ia.get_top250_movies()
    movie_choice = random.choice(movies)
    print(f'\nHow about {movie_choice} ({movie_choice["year"]})?\n\n')
    return True


def rock_paper_scissors() -> bool:
    """A simple rock-paper-scissors game"""
    art.tprint('ROCK-PAPER-SCISSORS')
    player_score = 0
    comp_score = 0
    while True:
        print(f'The score is: Computer - {comp_score}, Human - {player_score}')
        user_choice = input('Type [rock], [paper] or [scissors]: ')
        choices = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(choices)
        if user_choice in choices:
            print(f'Your choice is {user_choice}')
            print(f'I choose {comp_choice}')
            if user_choice == 'rock':
                if comp_choice == 'rock':
                    again = input('It is a draw. Play again [y/n]: ')
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'paper':
                    again = input('I win. Play again [y/n]: ')
                    comp_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'scissors':
                    again = input('I lost. Play again [y/n]: ')
                    player_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
            elif user_choice == 'paper':
                if comp_choice == 'paper':
                    again = input('It is a draw. Play again [y/n]: ')
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'scissors':
                    again = input('I win. Play again [y/n]: ')
                    comp_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'rock':
                    again = input('I lost. Play again [y/n]: ')
                    player_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
            elif user_choice == 'scissors':
                if comp_choice == 'scissors':
                    again = input('It is a draw. Play again [y/n]: ')
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'rock':
                    again = input('I win. Play again [y/n]: ')
                    comp_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
                elif comp_choice == 'paper':
                    again = input('I lost. Play again [y/n]: ')
                    player_score += 1
                    if again == 'y':
                        continue
                    else:
                        return True
        else:
            print('Wrong input, try [rock], [paper] or [scissors]')


def joke() -> bool:
    art.tprint('A JOKE')
    print(pyjokes.get_joke(), end='\n\n')
    return True


if __name__ == '__main__':
    while True:
        choice = menu()
        if not main(choice):
            break
