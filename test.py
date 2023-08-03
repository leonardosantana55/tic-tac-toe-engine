
"""
A1,A2,A3
B1.B2,B3
C1,C2,C3


se todos os 1,2,3 estiverem tomados, ganha
se todos os A,B,C estiverem tomados, ganha
se tiver tomado C1, B2, A3, ganha
se tiver tomado A1, B2, C3, ganha

(acho que isso aqui pode ser implementado um dicionário)

Tem que obter o estado de cada uma das celulas


"""


class Board:
    # cria a board 3x3
    letters = ['A','B','C']
    board = {i: {j+1: None for j in range(3)} for i in letters}
    # via atualizar as casa com X ou O
    def update(self, key, players_mark):
        row = key[0]
        column = int(key[1])
        
        new_play = {column: players_mark}
        self.board[row].update(new_play)

    def print_board(self):
        table = []
        for values in self.board.values():
            buffer = []    
            for value in values.values():
                if value == None:
                    buffer.append(" ")
                else:
                    buffer.append(value)
            table.append(buffer)
        
        for i in table:
            print(i)

            

class Players():
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.houses_captured = []
    """
    def play(self):
        print('escolha uma casa')
        turn = input()
        
        return turn
    """

class GameState():
    def __init__(self):
        self.on = False
        self.ended = False
        self.p1_wins = False
        self.p2_wins = False

        
def play(player: Players, board: Board):
    valid_play = False
    while valid_play == False:
        print('escolha uma casa')
        row_column = input()
        
        row = row_column[0]
        column = int(row_column[1])
            
        if board.board.get(row).get(column) == None: 
            valid_play = True
            player.houses_captured.append(row_column)
            return row_column
        else:
            print("essa casa já está ocupada, escolha outra!")



# o jogador cadastra uma jogada
# alguma coisa tem que passar essa jogada para o metodo update da Board

"""
def get_mark_input():
    valid_response = ["X", "O"]
    invalid_input = True
    while invalid_input:
        response = input()
        if response in valid_response:
            invalid_input = False
        else: print('você deve informar X ou O')
    return response
"""

board = Board()
player_1 = Players("Joao", "X")
player_2 = Players("Guilherme", "O")

rounds = 0
game_state = GameState()

board.print_board()
board.update(play(player_1, board), player_1.mark)
board.print_board()
board.update(play(player_2, board), player_2.mark)
board.print_board()

