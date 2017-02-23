def Victory(Board):
    Win = ' '
    
    for i in range(3):
        if (Board[i][0] == Board[i][1] == Board[i][2]):
            return Board[i][0]

    for i in range(3):
        if (Board[0][i] == Board[1][i] == Board[2][i]):
            return Board[0][i]
    
    if (Board[0][0] == Board[1][1] == Board[2][2]):
            return Board[0][0]
                
    if (Board[0][2] == Board[1][1] == Board[2][0]):
            return Board[0][2]
        
    return ' '  
