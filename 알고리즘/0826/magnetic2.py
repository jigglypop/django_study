for tc in range(1,11):
    size = int(input())
    board = []
    for i in range(100):
        board.append(input().split())
    count = 0
    board = list(zip(*board))
    print(board)
    for i in range(100):
        minus = 0
        temp_line =''.join(''.join(board[i]).split('0')).split('2')
        if temp_line[len(temp_line) - 1] != '':
            minus = 1
        count += len(temp_line) - temp_line.count('') - minus
    print('#{} {}'.format(tc,count))