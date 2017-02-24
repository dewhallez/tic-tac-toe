def startGame(playerOne,playerTwo):
  print('Welcome to tic-tac-toe!')

  p1name = str(input('Player 1 name?: '))
  playerOne['name'] = p1name

  p1piece = str(input('X or O?: '))

  while p1piece not in ['x','X','o','O']:
      print ('Invalid choice.')
      p1piece = str(input('X or O?: '))
      playerOne['piece'] = p1piece

  if p1piece in ['x','X']:
       p1piece = 'X'
       p2piece = 'O'
  else:
       p1piece = 'O'
       p2piece = 'X'

  p2name = str(input('Player 2 name?'))
  playerTwo['name'] = p2name

  playerOne['piece'] = p1piece
  playerTwo['piece'] = p2piece

  print('Player 1: ',playerOne['name'],', is playing as ',playerOne['piece'])
  print('Player 2: ',playerTwo['name'],', is playing as ',playerTwo['piece'])

  return
