
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

"""
letters = ['A','B','C']
board = {i: {j+1: 0 for j in range(3)} for i in letters}
houses_captured = ['B1', 'A1', 'A2', 'B3', 'B2']

each_row = {}
for l in letters:
    each_row[l] = []



print(len(board))

# Check columns
houses_captured.sort()
temp = None
column_checker = 0
for i in houses_captured:
    if i[0] == temp or temp == None:
        print(i)
        temp = i[0]
        column_checker +=1
print(column_checker)

# Check rows
houses_captured.sort()
temp = None
row_checker = 0
for i in houses_captured:
    if int(i[1])-1 == temp or temp == None:
        print(int(i[1]))
        temp = int(i[1])
        row_checker += 1

"""

# se capturou tres de uma mesma coluna ou linha e é uma sequencia de três, ganha
import itertools as it

class Board:
    # cria a board 3x3
    letters = ['A','B','C']
    board = {i: {j+1: 0 for j in range(3)} for i in letters}
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
                if value == 0:
                    buffer.append(" ")
                else:
                    buffer.append(value)
            table.append(buffer)
        
        for i in table:
            print(i)



class Players(Board):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

        self.houses_captured = {}
        for l in self.letters:
            self.houses_captured[l] = []
    """
    def play(self):
        print('escolha uma casa')
        turn = input()
        
        return turn
    """

"""

houses = {"A": [1,2], "B": [3,2], "C": [2]}
for key in houses.keys():
    if len(houses[key]) == 3:
        print(True)

for i in range(len(houses)):
    flat_list = list(it.chain.from_iterable(houses.values()))
    if flat_list.count(i) == 3:
        print(True)

"""


class GameState():
    def __init__(self):
        self.on = True
        self.victory = False

    def check_game_state(self, player: Players):
        #checa se ganhou por colunas
        for key in player.houses_captured.keys():
            if len(player.houses_captured[key]) == 3:
                self.victory = True
                print(True)
        #checa se ganhou por linhas
        for i in range(len(player.houses_captured)):
            flat_list = list(it.chain.from_iterable(player.houses_captured.values()))
            if flat_list.count(i) == 3:
                self.victory = True

    
    # logica de chacagem para condições de vitória


# falta colocar limite na tabela para nao permitid jogadas fora do escopo dela
        
def play(player: Players, board: Board):
    valid_play = False
    while valid_play == False:
        print('escolha uma casa')
        row_column = input()
        
        row = row_column[0]
        column = int(row_column[1])
        
        def invalid_play():
            valid_play = False
            print("essa não é uma escolha válida!")
        #check if is valid play

        try:
            if board.board.get(row).get(column) == 0: 
                valid_play = True
                player.houses_captured[row].append(column)
                board.update(row_column, player.mark)
                return row_column
            else:
                invalid_play()   
        except AttributeError:
                invalid_play()

def game_start():
    board = Board()
    game_state = GameState()
    player_1 = Players("Joao", "X")
    player_2 = Players("Guilherme", "O")
    player = player_1
    round_count = 0

    while game_state.on:
        board.print_board()
        if round_count % 2 == 0:
            player = player_1
        else:
            player = player_2
        play(player, board)
        round_count += 1
        game_state.check_game_state(player)


game_start()

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



