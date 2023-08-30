import itertools as it

class Board:
    # cria a board 3x3
    letters = ['A','B','C']
    board = {i: {j+1: 0 for j in range(3)} for i in letters}
    # vai atualizar as casa com X ou O
    def update(self, key, players_mark):
        row = key[0]
        column = int(key[1])
        
        new_play = {column: players_mark}
        self.board[row].update(new_play)

    def print_board(self):
        table = [str(self.letters)]
        for values in self.board.values():
            buffer = []
            for value in values.values():
                if value == 0:
                    buffer.append(" ")
                else:
                    buffer.append(value)
            table.append(buffer)
        enum = 0
        
        for i in table:
            if enum == 0:
                print("    1----2----3")
            else:
                print(self.letters[enum-1], i)
            enum += 1

class Players(Board):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

        self.houses_captured = {}
        for l in self.letters:
            self.houses_captured[l] = []

class GameState(Board):
    def __init__(self):
        self.on = True
        self.victory = False

    def check_game_state(self, player: Players):
        #checa se ganhou por colunas
        for key in player.houses_captured.keys():
            if len(player.houses_captured[key]) == 3:
                self.victory = True
        
        #checa se ganhou por linhas
        for i in range(len(player.houses_captured)):
            flat_list = list(it.chain.from_iterable(player.houses_captured.values()))
            if flat_list.count(i) == 3:
                self.victory = True
        
        #checa se ganhou por diagonais
        diagonal_check = 0
        diagonal_check_2 = 0
        enum = 1
        for key in player.houses_captured.keys():
            if enum in player.houses_captured[key]:
                diagonal_check += 1
            if (enum * -1) + (len(player.houses_captured)+1) in player.houses_captured[key]:
                diagonal_check_2 += 1
            enum += 1
        if diagonal_check == len(player.houses_captured) or diagonal_check_2 == len(player.houses_captured):
            self.victory = True
        
        #Finaliza o game
        if self.victory:
            self.on = False
            self.print_board()
            print(f"{player.name} ganhou!")

def play(player: Players, board: Board):
    valid_play = False
    while valid_play == False:
        print(f'{player.name}, escolha uma casa')
        row_column = input().upper()
                
        def invalid_play():
            valid_play = False
            print("essa não é uma escolha válida!")

        try:
            row = row_column[0]
            column = int(row_column[1])
            if board.board.get(row).get(column) == 0: #checks if the cell is not taken yet
                valid_play = True
                player.houses_captured[row].append(column)
                board.update(row_column, player.mark)
                return row_column
            else:
                invalid_play()   
        except:
                invalid_play()

def game_start():
    board = Board()
    game_state = GameState()
    print("Nome do jogador X: ")
    player_1 = Players(input(), "X")
    print("Nome do jogador O: ")
    player_2 = Players(input(), "O")
    
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