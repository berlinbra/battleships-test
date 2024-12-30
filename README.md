# Battleship Game

A Python implementation of the classic Battleship game where players try to sink each other's fleet.

## Features

- Command-line interface
- Two-player game (player vs computer)
- Standard Battleship grid (10x10)
- Five different ships with varying lengths
- Input validation and error handling

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/berlinbra/battleships-test.git
   ```
2. Navigate to the project directory:
   ```bash
   cd battleships-test
   ```

## How to Play

1. Run the game:
   ```bash
   python battleship.py
   ```
2. Follow the on-screen instructions to place your ships and make moves

## Game Rules

- The game is played on a 10x10 grid
- Each player has 5 ships of different lengths:
  - Carrier (5 spaces)
  - Battleship (4 spaces)
  - Cruiser (3 spaces)
  - Submarine (3 spaces)
  - Destroyer (2 spaces)
- Players take turns guessing coordinates to attack
- The game ends when all ships of one player are sunk

## Project Structure

- `battleship.py`: Main game file
- `board.py`: Board class implementation
- `ship.py`: Ship class implementation
- `player.py`: Player class implementation

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.