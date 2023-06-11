def quitting():
    play_again = input("Play again (y, n)? ")
    if play_again == "n":
        return False
    elif play_again == "y":
        return True

