#RANDOM SUDOKU!

base  = 3
side  = base*base

# pattern per una soluzione valida
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize linee, colonne and numeri
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produrre una matrice che raccolga la randomizzazione dei numeri
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

print('\nquesto è il sudoku generato casualmente: ')
for line in board: print(line)

#SUDOKU Validatore!

def find_next_empty(puzzle):
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == -1:
				return r,c
	return None, None

def is_valid(puzzle, guess, row, col):

	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	col_vals = [puzzle[i][col] for i in range (9)]
	if guess in col_vals:
		return False

	row_start = (row //3) * 3
	col_start = (col //3) * 3

	for r in range(row_start, row_start + 3):
		for c in range(col_start, col_start + 3):
			if puzzle [r][c] == guess:
				return False

def solve_sudoku(puzzle):
	row, col = find_next_empty(puzzle)

	if row is None:
		return True

	for guess in range(1, 10):
		if is_valid(puzzle, guess, row, col):
			puzzle [row][col] = guess
			if solve_sudoku(puzzle):
				return True

		puzzle[row][col] = -1 

	return False


if __name__ == '__main__':
			board



#CAMUFFATORE!!
squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

numSize = len(str(side))
print("\nIl precedente sudoku in versione in versione puzzle: ")
for line in board: print("["+"  ".join(f"{n or '.':{numSize}}" for n in line)+"]")

# Interfaccia GRAFICA 

print('\nStampa di interfaccia grafica: ')
def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
line0  = expandLine("╔═══╤═══╦═══╗")
line1  = expandLine("║ . │ . ║ . ║")
line2  = expandLine("╟───┼───╫───╢")
line3  = expandLine("╠═══╪═══╬═══╣")
line4  = expandLine("╚═══╧═══╩═══╝")

symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums   = [ [""]+[symbol[n] for n in row] for row in board ]
print(line0)
for r in range(1,side+1):
    print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
    print([line2,line3,line4][(r%side==0)+(r%base==0)])

print('\nverifica che si stia valutando esattamente quel sudoku: ')
for line in board: print(line)
print ('\nPosso risolvere questo sudoku?: ' + str(solve_sudoku(board)))







