import random
from typing import List, Tuple, Dict

class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.hits = 0
        self.positions: List[Tuple[int, int]] = []

    def is_sunk(self) -> bool:
        return self.hits >= self.size

class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships: List[Ship] = []

    def place_ship(self, ship: Ship, start_pos: Tuple[int, int], horizontal: bool) -> bool:
        x, y = start_pos
        positions = []

        # Check if placement is valid
        for i in range(ship.size):
            new_x = x + (i if horizontal else 0)
            new_y = y + (0 if horizontal else i)

            if not (0 <= new_x < self.size and 0 <= new_y < self.size):
                return False
            if self.board[new_y][new_x] != ' ':
                return False
            positions.append((new_x, new_y))

        # Place ship
        for pos_x, pos_y in positions:
            self.board[pos_y][pos_x] = 'S'
        ship.positions = positions
        self.ships.append(ship)
        return True

    def receive_attack(self, pos: Tuple[int, int]) -> str:
        x, y = pos
        if self.board[y][x] == 'S':
            self.board[y][x] = 'H'
            for ship in self.ships:
                if pos in ship.positions:
                    ship.hits += 1
                    if ship.is_sunk():
                        return f"You sunk my {ship.name}!"
                    return "Hit!"
        elif self.board[y][x] == ' ':
            self.board[y][x] = 'M'
            return "Miss!"
        return "Already attacked this position!"

class Game:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()
        self.ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2)
        ]

    def setup_game(self):
        # Place computer ships
        for ship in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                horizontal = random.choice([True, False])
                if self.computer_board.place_ship(Ship(ship.name, ship.size), (x, y), horizontal):
                    break

        # Place player ships (simplified for now - random placement)
        for ship in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                horizontal = random.choice([True, False])
                if self.player_board.place_ship(Ship(ship.name, ship.size), (x, y), horizontal):
                    break

    def display_boards(self):
        print("\nYour Board:")
        self._print_board(self.player_board)
        print("\nComputer's Board:")
        self._print_board(self.computer_board, hide_ships=True)

    def _print_board(self, board: Board, hide_ships: bool = False):
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(board.size):
            row = chr(65 + i) + " "
            for j in range(board.size):
                cell = board.board[i][j]
                if hide_ships and cell == 'S':
                    row += '  '
                else:
                    row += cell + " "
            print(row)

def main():
    game = Game()
    print("Welcome to Battleship!")
    game.setup_game()

    while True:
        game.display_boards()
        
        # Player's turn
        while True:
            try:
                move = input("\nEnter your move (e.g., A5): ").upper()
                y = ord(move[0]) - ord('A')
                x = int(move[1])
                if 0 <= x < 10 and 0 <= y < 10:
                    break
            except (ValueError, IndexError):
                pass
            print("Invalid input! Please enter a letter A-J followed by a number 0-9")

        result = game.computer_board.receive_attack((x, y))
        print(result)

        # Computer's turn
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if game.player_board.board[y][x] in [' ', 'S']:
                break
        
        result = game.player_board.receive_attack((x, y))
        print(f"Computer attacks {chr(65 + y)}{x}: {result}")

        # Check for win conditions
        if all(ship.is_sunk() for ship in game.computer_board.ships):
            print("\nCongratulations! You won!")
            break
        if all(ship.is_sunk() for ship in game.player_board.ships):
            print("\nGame Over! The computer won!")
            break

if __name__ == "__main__":
    main()