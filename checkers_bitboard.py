from bitmanipulation import BitManipulation

class CheckersBitboard:
    def __init__(self):
        # Initializing a 64-bit board for an 8x8 checkers game
        self.board = 0
        self.utility = BitManipulation()

    # Initialize the checkers board with starting pieces
    def initialize_board(self):
        # Setting bits for black pieces (positions 1 to 12)
        for i in range(1, 13):
            self.board = self.utility.set_bit(self.board, i)
        # Setting bits for red pieces (positions 21 to 32)
        for i in range(21, 33):
            self.board = self.utility.set_bit(self.board, i)

    # Print the current state of the board in an 8x8 format
    def display_board(self):
        print("Checkers Bitboard:")
        for i in range(8):
            row = ""
            for j in range(8):
                pos = i * 8 + j
                if self.utility.is_bit_set(self.board, pos):
                    row += "1 "  # Piece present
                else:
                    row += "0 "  # Empty
            print(row)
    
    # Move a piece from one position to another
    def move_piece(self, from_pos, to_pos):
        if self.utility.is_bit_set(self.board, from_pos):
            self.board = self.utility.clear_bit(self.board, from_pos)
            self.board = self.utility.set_bit(self.board, to_pos)

    # Remove a piece from the board (simulate capture)
    def remove_piece(self, pos):
        if self.utility.is_bit_set(self.board, pos):
            self.board = self.utility.clear_bit(self.board, pos)

if __name__ == "__main__":
    # Create a Checkers Bitboard
    checkers = CheckersBitboard()

    # Initialize the board
    checkers.initialize_board()

    # Display the board
    checkers.display_board()

    # Move a piece from position 5 to position 13
    print("\nMoving a piece from 5 to 13...")
    checkers.move_piece(5, 13)
    checkers.display_board()

    # Remove a piece (simulate capture) at position 13
    print("\nRemoving the piece at position 13...")
    checkers.remove_piece(13)
    checkers.display_board()
