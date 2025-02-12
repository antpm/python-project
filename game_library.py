from lib.game import Game
import sys
import argparse
import csv
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(prog="Game Library", description="A program for creating a library of games you've played")
    parser.add_argument("-l", "--load", help="Name of the file to load")
    args = parser.parse_args()
    games = list()
    new = True
    file_name = ""
    options = [["(1)", "View Games"],["(2)", "Add Game"],["(3)", "Edit Game"],  ["(4)", "Delete Game"], ["(5)", "Sort Games"], ["(6)", "Save Data"], ["(7)","Exit"]]

    if args.load:
        print(f"{args.load} loaded")
        new = False
        file_name = args.load
        games = load_data(file_name)
    else:
        print("New catalog started")

    while True:
        print(tabulate(options))
        try:
            select = int(input("Enter the number of the option you wish to select: "))
        except ValueError:
            print("\nInvalid selection")
        else:
            if select > len(options) or select < 1:
                print("\nInvalid selection")
            else:
                match select:
                    case 1:
                        show_full_table(games)
                    case 2:
                        games = add_game(games)
                    case 3:
                        games = edit_game(games)
                    case 4:
                        games = delete_game(games)
                    case 5:
                        games = sort_games(games)
                    case 6:
                        save_date(games, new, file_name)
                    case 7:
                        sys.exit("Goodbye")


def show_full_table(games:list[Game]):
    headers= ["#","Title","Developer","Genre","Platform","Release Date","Completion Date","Rating"]
    data= []
    for i,game in enumerate(games):
        data.append(game.full_list_data(i+1))
    print(tabulate(data, headers=headers, tablefmt="grid"))

def show_short_table(games:list[Game]):

    headers= ["#","Title"]
    data = []

    for i, game in enumerate(games):
        data.append(game.short_list_data(i+1))

    print(tabulate(data, headers=headers, tablefmt="grid"))

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
            new_game.platform = input("Enter Platform: ")
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

def select_game(games:list[Game], mode:str)->int:
    show_short_table(games)

    while True:
        try:
            game_num = int(input(f"Enter the number of the game to {mode}: "))
        except ValueError:
            print("Invalid selection. Please try again")
        else:
            if game_num < 1 or game_num > len(games):
                print("Invalid selection. Please try again")
            else:
                return game_num
            
def select_field(msg:str)->int:
    fields = [["(1)", "Title"],["(2)", "Developer"],["(3)", "Genre"],["(4)", "Platform"],["(5)", "Release Date"],["(6)", "Complete Date"],["(7)", "Rating"]]
    field_num = 0

    while True:
        print(tabulate(fields))
        try:
            field_num = int(input(msg))
        except ValueError:
            print("Invalid selection. Please try again.")
        else:
            if field_num < 1 or field_num > len(fields):
                print("\nInvalid selection. Please try again.")
            else:
                return field_num

def edit_game(games:list[Game])->list[Game]:

    game_num = select_game(games, "edit")
    game = games[game_num -1]
    
    field_num = select_field("Enter the number of the field to edit: ")

    match field_num:
        case 1:
             while True:
                try:
                    game.title = input("Enter New Title: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 2:
            while True:
                try:
                    game.developer = input("Enter New Developer: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 3:
            while True:
                try:
                    game.genre = input("Enter New Genre: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 4:
            while True:
                try:
                    game.platform = input("Enter New Platform: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 5:
            while True:
                try:
                    game.release = input("Enter New Release Date: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 6:
            while True:
                try:
                    game.complete = input("Enter New Completion Date: ")
                except ValueError as e:
                    print(e)
                else:
                    break
        case 7:
            while True:
                try:
                    game.rating = input("Enter New Rating(1-5): ")
                except ValueError as e:
                    print(e)
                else:
                    break
        
    print("\nGame Edited. Returning to main menu...\n")

    return games
    
def delete_game(games:list[Game])->list[Game]:
    game_num = select_game(games, "delete")
    game = games[game_num -1]
    while True:
        confirm = input(f"\nDeleting {game.title}. Are you sure? Y/N: ").lower()
        if confirm == "y":
            games.remove(game)
            print("\nGame deleted.", end=" ")
            break
        elif confirm == "n":
            print("\nCanceling deletion.", end=" ")
            break
        else:
            print("Invalid input, please try again.")
    
    print("Returning to main menu...")

    return games

def sort_games(games:list[Game])->list[Game]:
    
    field_num = select_field("Enter the number of field to sort by: ")

    match field_num:
        case 1:
            games = sorted(games, key=lambda game: game.title, reverse=True)
        case 2:
            games = sorted(games, key=lambda game: game.developer, reverse=True)
        case 3:
            games = sorted(games, key=lambda game: game.genre, reverse=True)
        case 4:
            games = sorted(games, key=lambda game: game.platform, reverse=True)
        case 5:
            games = sorted(games, key=lambda game: game.release, reverse=True)
        case 6:
            games = sorted(games, key=lambda game: game.complete, reverse=True)
        case 7:
            games = sorted(games, key=lambda game: game.rating, reverse=True)

    print("\nGames sorted. Returning to main menu...\n")
    return games

def save_date(games:list[Game], new:bool, file_name:str):
    if new:
        file_name = get_new_file_name()

    data = []    
    for game in games:
        data.append(game.dict_convert())

    with open(f"saved_data/{file_name}.csv", "w", newline="") as file:
        headers = ["title","developer","genre","platform","release date","complete date","rating"]
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        for item in data:
            writer.writerow(item)
        
    print("\nData Saved\n")
    
def get_new_file_name()->str:
    while True:
            file_name = input("Enter the name of file to save: ")
            try:
                file = open(f"saved_data/{file_name}.csv", "x")
            except FileExistsError:
                print("File with that name already exists, please try again.")
            else:
                file.close()
                break

    return file_name.strip()
    
def load_data(file_name:str)->list[Game]:
    
    games = list()
    try:
        with open(f"saved_data/{file_name}.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                game = Game(row["title"],row["developer"],row["genre"],row["platform"],row["release date"],row["complete date"],int(row["rating"]))
                games.append(game)
    except FileNotFoundError:
        sys.exit("File to load could not be found. Program will now close...")
    
    return games

if __name__ == "__main__":
    main()