from lib.game import Game
from lib.exceptions import RatingError
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="Game Library", description="A program for creating a library of games you've played")
    parser.add_argument("-l", "--load", help="Name of the file to load")
    args = parser.parse_args()
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
    


if __name__ == "__main__":
    main()