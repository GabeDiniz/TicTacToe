# Introduction
print('Player 1 goes first. The grid numbers go from 1 - 9.')

grid = [['1', '2', '3',],
        ['4', '5', '6',],
        ['7', '8', '9']]

for row in grid:
  print(row)


def game(grid, turn, taken):

  if turn%2 == 1:
    player = int(input("Player 1's pick: "))
    
  else:
    player = int(input("Player 2's pick: "))

  if player > 9:
    print('Invalid Entry')
    return game(grid, turn, taken)
  
  # finds the row and col of the entry
  row = 0
  col = 0
  for x in range(8):
    if x + 1 == player:
      break
    else: 
      if col < 2:
        col += 1
      else:
        row += 1
        col = 0
  
  # checks if there is already an x or o there
  if [row, col] in taken:
    print('Entry taken')
    return game(grid, turn, taken)

  # changes the grid accordingly
  if turn%2 == 1:
    grid[row][col] = 'x'
  else:
    grid[row][col] = 'o'
  
  for rows in grid:
    print(rows[0], rows[1], rows[2])
  
  # checks for winner
  if ['x', 'x', 'x'] in grid:
    print('player 1 wins!')
    return
  elif ['o', 'o', 'o'] in grid:
    print('player 2 wins!')
    return
  
  n = 0
  r = 0
  c = 0
  while n < 3:
    if grid[r][c] == 'x' and grid[r + 1][c] == 'x' and grid[r + 2][c] == 'x':
      print('player 1 wins!')
      return
    elif grid[r][c] == 'o' and grid[r + 1][c] == 'o' and grid[r + 2][c] == 'o':
      print('player 2 wins!')
      return
    
    c += 1  
    n += 1

  if grid[0][2] == 'x' and grid[1][1] == 'x' and grid[2][0] == 'x':
    print('player 1 wins!')
    return
  elif grid[0][2] == 'o' and grid[1][1] == 'o' and grid[2][0] == 'o':
    print('player 2 wins!')
    return
  elif grid[0][0] == 'x' and grid[1][1] == 'x' and grid[2][2] == 'x':
    print('player 1 wins!')
    return
  elif grid[0][0] == 'o' and grid[1][1] == 'o' and grid[2][2] == 'o':
    print('player 2 wins!')
    return
  
  


  # updates taken and grid
  taken = taken + [[row, col]]
  if len(taken) == 9:
    print('No one wins!')
    return
  return game(grid, turn + 1, taken)
  



taken = []
game(grid, 1, [])