import random
from board import Board
from player import Player
from ship import Ship

class BattleshipGame:
    def __init__(self):
        self.player = Player("Human")
        self.computer = Player("Computer")
        self.current_player = self.player

    def setup_game(self):
        print("Welcome to Battleship!")
        print("\nPlace your ships on the board:")
        self._place_ships(self.player, manual=True)
        print("\nComputer is placing ships...")
        self._place_ships(self.computer, manual=False)

    def _place_ships(self, player, manual=False):
        ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2)
        ]

        for ship in ships:
            placed = False
            while not placed:
                if manual:
                    print(f"\nPlacing {ship.name} (length: {ship.length})")
                    player.board.display()
                    try:
                        x = int(input("Enter x coordinate (0-9): "))
                        y = int(input("Enter y coordinate (0-9): "))
                        direction = input("Enter direction (h/v): ").lower()
                        if direction not in ['h', 'v']:
                            raise ValueError("Direction must be 'h' or 'v'")
                    except ValueError as e:
                        print(f"Invalid input: {e}")
                        continue
                else:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.choice(['h', 'v'])

                try:
                    player.board.place_ship(ship, x, y, direction == 'h')
                    placed = True
                except ValueError as e:
                    if manual:
                        print(f"Cannot place ship: {e}")

    def play(self):
        self.setup_game()
        game_over = False

        while not game_over:
            print(f"\n{self.current_player.name}'s turn")
            if self.current_player == self.player:
                print("\nYour board:")
                self.player.board.display()
                print("\nComputer's board:")
                self.computer.board.display(hide_ships=True)

                try:
                    x = int(input("Enter x coordinate to attack (0-9): "))
                    y = int(input("Enter y coordinate to attack (0-9): "))
                    hit = self.computer.board.receive_attack(x, y)
                except ValueError as e:
                    print(f"Invalid input: {e}")
                    continue
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                hit = self.player.board.receive_attack(x, y)

            if hit:
                print(f"\n{self.current_player.name} hit a ship at ({x}, {y})!")
                if self.current_player == self.player:
                    if self.computer.board.all_ships_sunk():
                        print("\nCongratulations! You won!")
                        game_over = True
                else:
                    if self.player.board.all_ships_sunk():
                        print("\nGame Over! Computer won!")
                        game_over = True
            else:
                print(f"\n{self.current_player.name} missed at ({x}, {y})")

            self.current_player = self.computer if self.current_player == self.player else self.player

def main():
    game = BattleshipGame()
    game.play()

if __name__ == "__main__":
    main()