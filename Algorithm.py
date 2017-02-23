def Victory(Board)
    Win = ' '
    
    for i in range(3):
        if Board[i][1] == Board[i][2] == Board[i][3]
            Win = Board[i][1]

    for i in range(3):
        if Board[1][i] == Board[2][i] == Board[3][i]
            Win = Board[1][i]
    
    if Board[1][1] == Board[2][2] == Board[3][3]
            Win = Board[1][1]
                
    if Board[1][3] == Board[2][2] == Board[3][1]
            Win = Board[1][3]
    return Win        
