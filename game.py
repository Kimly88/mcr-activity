def is_win(game):
    win = False
    
    # 检查行 (rows)
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
        
    # 检查列 (columns)
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][0] == 'X' or game[0][0] == 'O'):  # <-- 注意这里
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):  # <-- 还有这里
        win = True
        
    return win
