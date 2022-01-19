#Programmet undersøker om en løsning til eight queens problem er gyldig

AMOUNT_OF_ROWS    = 8
AMOUNT_OF_COLUMNS = 8
class EQ:
    def __init__(self, queens = AMOUNT_OF_ROWS * [-1]):
        self.queens = queens

    def set(self, row, column):
        self.queens[row] = column
    
    def get(self, row):
        return self.queens[row]
        
    def is_solved(self):

        for i in range(AMOUNT_OF_COLUMNS):
            queens_in_column = 0
            for j in range(AMOUNT_OF_ROWS):
                if self.queens[j] == i:
                    queens_in_column += 1
                    if queens_in_column > 1:
                        return False

        for i in range( len(self.queens) - 1):
            next_quuens = self.queens[i + 1 : ]
            for j in range( len(next_quuens) ):
               delta_column = next_quuens[j] - self.queens[i] 
               delta_row = j + 1
               slope = abs(delta_row / delta_column)
               if slope == 1:
                   return False

        return True


    def print_board(self):
        space  = ""
        square = "| |"
        queen  = "|X|"
        for i in range(AMOUNT_OF_ROWS):
            print( (self.queens[i] ) * (square + space)
                + queen
                + ( AMOUNT_OF_ROWS - 1 - self.queens[i] ) * (square + space) )
        
def main():
    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?",
        board1.is_solved())

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.is_solved():

        print("Eight queens are placed correctly in board2")

        board2.print_board()

    else:

        print("Eight queens are placed incorrectly in board2")

main()

