from lib.game import Game
import sys
import argparse
import csv
import os.path
from tabulate import tabulate

def main():
    parser = argparse.ArgumentParser(prog="Game Library", description="A program for creating a library of games you've played")
    parser.add_argument("-l", "--load", help="Name of the file to load")
    args = parser.parse_args()
    games = list()
    new = True
    file_name = ""
    if args.load:
        print(f"{args.load} loaded")
        new = False
        file_name = args.load
        games = load_data()
    else:
        print("New catalog started")

    while True:
        show_menu()
        try:
            select = int(input("Enter the number of the option you wish to select: "))
        except ValueError:
            print("\nInvalid selection")
        else:
            if select > 6 or select < 1:
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
                        save_date(games, new, file_name)
                    case 6:
                        sys.exit("Goodbye")


def show_menu():
    options = [["(1)", "View Games"],["(2)", "Add Game"],["(3)", "Edit Game"],  ["(4)", "Delete Game"], ["(5)", "Save Data"], ["(6)", "Exit"]]
    print(tabulate(options))

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

    return sorted(games, key=lambda game: game.complete, reverse=True)

def edit_game(games:list[Game])->list[Game]:
    """ show_short_table(games)
    while True:
        try:
            select = int(input("Enter the number of the game you wish to edit: "))
        except ValueError:
            print("Invalid selection. Please try again")
        else:
            if select < 1 or select > len(games):
                print("Invalid selection. Please try again")
            else:
                break """
    return sorted(games, key=lambda game: game.complete, reverse=True)
    

def delete_game(games:list[Game])->list[Game]:
    pass
    return sorted(games, key=lambda game: game.complete, reverse=True)

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
    
def load_data()->list[Game]:
    pass
    games = list()
    return games

if __name__ == "__main__":
    main()