class Board:
    def __init__(self):
        self.size = 10
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []

    def display(self, hide_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row = [str(i)]
            for j in range(self.size):
                cell = self.grid[i][j]
                if hide_ships and cell == 'S':
                    row.append(' ')
                else:
                    row.append(cell)
            print(" ".join(row))

    def is_valid_position(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def place_ship(self, ship, x, y, horizontal):
        if not self.is_valid_position(x, y):
            raise ValueError("Position out of bounds")

        # Check if ship placement is within bounds
        end_x = x + (ship.length - 1 if horizontal else 0)
        end_y = y + (0 if horizontal else ship.length - 1)
        if not self.is_valid_position(end_x, end_y):
            raise ValueError("Ship placement out of bounds")

        # Check for overlapping ships
        for i in range(ship.length):
            check_x = x + (i if horizontal else 0)
            check_y = y + (0 if horizontal else i)
            if self.grid[check_y][check_x] != ' ':
                raise ValueError("Ships cannot overlap")

        # Place the ship
        ship.positions = []
        for i in range(ship.length):
            pos_x = x + (i if horizontal else 0)
            pos_y = y + (0 if horizontal else i)
            self.grid[pos_y][pos_x] = 'S'
            ship.positions.append((pos_x, pos_y))

        self.ships.append(ship)

    def receive_attack(self, x, y):
        if not self.is_valid_position(x, y):
            raise ValueError("Attack position out of bounds")

        if self.grid[y][x] in ['X', 'O']:
            raise ValueError("Position already attacked")

        hit = self.grid[y][x] == 'S'
        self.grid[y][x] = 'X' if hit else 'O'
        
        if hit:
            for ship in self.ships:
                if (x, y) in ship.positions:
                    ship.hits += 1
        
        return hit

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)