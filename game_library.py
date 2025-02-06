from lib.game import Game
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="Game Library", description="A program for creating a library of games you've played")
    parser.add_argument("-l", "--load", help="Name of the file to load")
    args = parser.parse_args()
    games = list()
    if args.load:
        print(f"{args.load} loaded")
    else:
        print("New catalog started")

    while True:
        show_menu()
        try:
            select = int(input("Enter the number of the option you wish to select:"))
        except ValueError:
            print("\nInvalid selection")
        else:
            if select > 6 or select < 1:
                print("\nInvalid selection")
            else:
                match select:
                    case 1:
                        view_games(games)
                    case 2:
                        games = add_game(games)
                    case 3:
                        games = edit_game(games)
                    case 4:
                        games = delete_game(games)
                    case 5:
                        save_date(games)
                    case 6:
                        sys.exit("Goodbye")


def show_menu():
    print("\nOptions:")
    print("(1)View Games")
    print("(2)Add Game")
    print("(3)Edit Game")
    print("(4)Delete Game")
    print("(5)Save Data")
    print("(6)Exit")

def view_games(games:list[Game]):
    for i,game in enumerate(games):
        print(f"\nGame #{i+1}")
        print(game)

def add_game(games:list[Game])->list[Game]:
    new_game = Game()

    while True:
        try:
            new_game.title = input("Enter Title: ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.developer = input("Enter Developer: ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.genre = input("Enter Genre: ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.platform = input("Enter platform: ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.release = input("Enter Release Date(YYYY-MM-DD): ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.complete = input("Enter Completion Date(YYYY-MM-DD): ")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            new_game.rating = input("Enter Rating(1-5): ")
        except ValueError as e:
            print(e)
        else:
            break

    games.append(new_game)

    return games

def edit_game(games:list[Game])->list[Game]:
    pass
    return games

def delete_game(games:list[Game])->list[Game]:
    pass
    return games

def save_date(games:list[Game]):
    pass
    


if __name__ == "__main__":
    main()