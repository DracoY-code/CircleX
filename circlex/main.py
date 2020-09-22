import os
import sys
from time import sleep

from colorama import init, Fore, Style
init(autoreset=True)
    

# The board dictionary
board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}


class Player:
    """ The class for players. 👦👧 """
    def __init__(self, name: str, sign: str) -> None:
        print(f'Welcome {Fore.GREEN}{name}{Style.RESET_ALL}! 👋')
        self.name = name
        self.sign = sign


class TheBoard:
    """ The game board class. 🕹 """
    def __init__(self) -> None:
        self.board = board

    def printBoard(self) -> None:
        """Prints the board on the console.
        """
        print(Fore.GREEN + '\n ' + self.board['top-L'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['top-M'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['top-R'])
        print(Fore.RED + '---+---+---')
        print(Fore.GREEN + ' ' + self.board['mid-L'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['mid-M'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['mid-R'])
        print(Fore.RED + '---+---+---')
        print(Fore.GREEN + ' ' + self.board['low-L'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['low-M'] + Fore.RED
              + ' | ' + Fore.GREEN + self.board['low-R'])

    def updateBoard(self, player: Player, move: str) -> None:
        """Updates the board after every move.
        """
        self.board[move] = player.sign

    def isValidSpace(self, position: str) -> bool:
        """Returns true if the point in the grid is a valid space.
        """
        return True if self.board[position] == ' ' else False

    def isBoardFull(self) -> bool:
        """Returns true if board is full.
        """
        for space in self.board:
            if self.board[space] == ' ':
                return False
        return True

    def isWinner(self, player: Player) -> bool:
        """Returns true if player has won the game.
        """
        return (
            (self.board['top-L'] == self.board['top-M']         # Match top row
             == self.board['top-R'] == player.sign) or
            (self.board['mid-L'] == self.board['mid-M']         # Match mid row
             == self.board['mid-R'] == player.sign) or
            (self.board['low-L'] == self.board['low-M']         # Match last row
             == self.board['low-R'] == player.sign) or
            (self.board['top-L'] == self.board['mid-L']         # Down left column
             == self.board['low-L'] == player.sign) or
            (self.board['top-M'] == self.board['mid-M']         # Down middle column
             == self.board['low-M'] == player.sign) or
            (self.board['top-R'] == self.board['mid-R']         # Down last column
             == self.board['low-R'] == player.sign) or
            (self.board['top-L'] == self.board['mid-M']         # Diagonal
             == self.board['low-R'] == player.sign) or
            (self.board['top-R'] == self.board['mid-M']         # Diagonal
             == self.board['low-L'] == player.sign)
        )


def clear() -> None:
    """Clears cconsole window.
    """
    os.system('cls')


def rules() -> None:
    """Displays rules and details about the game.
    """
    print(f'{Fore.GREEN}CircleX{Style.RESET_ALL}: A Simple '
          + f'{Fore.BLUE}Tic Tac Toe{Style.RESET_ALL} Game 🎮')
    print('\nPossible moves:')
    print(f'{Fore.YELLOW}top-L{Style.RESET_ALL}; {Fore.YELLOW}top-M'
          + f'{Style.RESET_ALL}; {Fore.YELLOW}top-R{Style.RESET_ALL};')
    print(f'{Fore.YELLOW}mid-L{Style.RESET_ALL}; {Fore.YELLOW}mid-M'
          + f'{Style.RESET_ALL}; {Fore.YELLOW}mid-R{Style.RESET_ALL};')
    print(f'{Fore.YELLOW}low-L{Style.RESET_ALL}; {Fore.YELLOW}low-M'
          + f'{Style.RESET_ALL}; {Fore.YELLOW}low-R{Style.RESET_ALL};')
    sleep(1)


def load_results() -> None:
    """Displays result info.
    """
    print(f'\nLoading results{Fore.GREEN}...', end='')
    sys.stdout.flush()
    sleep(5); print();


def main() -> None:
    """Runs the game.
    """
    theBoard = TheBoard()
    theBoard.printBoard()

    print('\nWhat is your name?')
    name1 = input('\nPlayer 1 : ')
    player1 = Player(name1, 'X')

    name2 = input('\nPlayer 2 : ')
    player2 = Player(name2, 'O')

    currentPlayer, nextPlayer = player1, player2

    print(f'\nLoading{Fore.GREEN}...', end='')
    sys.stdout.flush()
    sleep(5)
    print()

    while True:
        clear(); rules();
        
        theBoard.printBoard()
        name = f'{Fore.GREEN}{currentPlayer.name}{Style.RESET_ALL}'
        
        move = input(f"\n{name}'s turn. Move on which space? ")
        if move not in theBoard.board:
            print(f'\nPlease retry{Fore.RED}...', end='')
            sleep(2); print();
            continue

        if theBoard.isValidSpace(move):
            theBoard.updateBoard(currentPlayer, move)
        else:
            print(f"\n{Fore.RED}error{Style.RESET_ALL}: "
                  + f"{name}'s turn was invalid!")
            sleep(3)
            continue

        if theBoard.isWinner(currentPlayer):
            clear(); theBoard.printBoard(); load_results(); clear();
            print(f'🎉 {Fore.GREEN}CONGRATULATIONS!{Style.RESET_ALL} 🎉\n');
            print(f'{name} has won the game!')
            break
        elif theBoard.isBoardFull():
            clear(); theBoard.printBoard(); load_results();
            clear(); print(f'😞 {Fore.RED}OH NO!{Style.RESET_ALL} 👻\n');
            print(f'The game is a {Fore.YELLOW}tie{Style.RESET_ALL}!')
            break

        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    print('Thanks for playing! 😊\n')
    os.system('pause')


if __name__ == '__main__':
    main()