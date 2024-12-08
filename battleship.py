import random

class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, length, is_horizontal, row, col):
        if is_horizontal:
            if col + length > self.size:
                return False
            for i in range(length):
                if self.board[row][col + i] != ' ':
                    return False
            for i in range(length):
                self.board[row][col + i] = 'S'
        else:
            if row + length > self.size:
                return False
            for i in range(length):
                if self.board[row + i][col] != ' ':
                    return False
            for i in range(length):
                self.board[row + i][col] = 'S'
        self.ships.append({'length': length, 'positions': [(row + i if not is_horizontal else row,
                                                          col + i if is_horizontal else col)
                                                         for i in range(length)]})
        return True

    def receive_attack(self, row, col):
        if not (0 <= row < self.size and 0 <= col < self.size):
            return 'Invalid'
        if self.board[row][col] == 'S':
            self.board[row][col] = 'H'
            return 'Hit'
        elif self.board[row][col] == ' ':
            self.board[row][col] = 'M'
            return 'Miss'
        return 'Already attacked'

    def display(self, hide_ships=True):
        print('  ' + ' '.join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row_display = [self.board[i][j] if not hide_ships or self.board[i][j] in ['H', 'M']
                          else ' ' for j in range(self.size)]
            print(f'{i} {" ".join(row_display)}')

class Game:
    def __init__(self):
        self.player_board = Board()
        self.computer_board = Board()
        self.setup_game()

    def setup_game(self):
        ships = [5, 4, 3, 3, 2]  # Standard battleship ship sizes
        # Place computer's ships
        for ship in ships:
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                is_horizontal = random.choice([True, False])
                if self.computer_board.place_ship(ship, is_horizontal, row, col):
                    break

        print("Place your ships!")
        for ship in ships:
            self.player_board.display(hide_ships=False)
            while True:
                try:
                    print(f"\nPlacing ship of length {ship}")
                    row = int(input("Enter row (0-9): "))
                    col = int(input("Enter column (0-9): "))
                    is_horizontal = input("Place horizontally? (y/n): ").lower() == 'y'
                    if self.player_board.place_ship(ship, is_horizontal, row, col):
                        break
                    print("Invalid placement. Try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers for row and column.")

    def play(self):
        while True:
            # Player's turn
            print("\nYour board:")
            self.player_board.display(hide_ships=False)
            print("\nComputer's board:")
            self.computer_board.display()

            # Player attack
            while True:
                try:
                    row = int(input("Enter attack row (0-9): "))
                    col = int(input("Enter attack column (0-9): "))
                    result = self.computer_board.receive_attack(row, col)
                    if result != 'Already attacked':
                        break
                    print("You've already attacked this position. Try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers.")

            print(f"Your attack result: {result}")

            # Computer's turn
            while True:
                row = random.randint(0, 9)
                col = random.randint(0, 9)
                result = self.player_board.receive_attack(row, col)
                if result != 'Already attacked':
                    break

            print(f"Computer attacked position ({row}, {col}): {result}")

            # Check for game over
            if self.check_game_over():
                break

    def check_game_over(self):
        player_ships = sum(1 for row in self.player_board.board for cell in row if cell == 'S')
        computer_ships = sum(1 for row in self.computer_board.board for cell in row if cell == 'S')

        if player_ships == 0:
            print("Game Over! Computer wins!")
            return True
        elif computer_ships == 0:
            print("Congratulations! You win!")
            return True
        return False

if __name__ == "__main__":
    print("Welcome to Battleship!")
    game = Game()
    game.play()