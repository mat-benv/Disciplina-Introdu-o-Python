# Universidade do Vale do Itajaí - Campus Kobrasol
# Escola Politécnica
# Disciplina - Introdução a Python
# Professor: Evandro
# Trabalho para M2, Batalha Naval
# Entrega em 29/10/2024

import random
import time

# Initializes player's and computer's board
tabuleiro_player = [
    ["~" for _ in range(10)] for _ in range(10)
]
tabuleiro_pc_vw = [
    ["~" for _ in range(10)] for _ in range(10)
]  # Visible computer board
tabuleiro_pc_hf = [
    ["~" for _ in range(10)] for _ in range(10)
]  # Reference computer board

# Dictionary to monitor player's ships

navios_player = {
    "PA": {'nome': 'porta-aviões', "tamanho": 5, "coordenadas": [], "simbolo": "P"},
    "NT1": {'nome': 'navio tanque',"tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "NT2": {'nome': 'navio tanque', "tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "CT1": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CT2": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CP3": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "S1": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S2": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S3": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S4": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"}
}

# Monitors computer's ships

navios_pc = {
    "PA": {'nome': 'porta-aviões', "tamanho": 5, "coordenadas": [], "simbolo": "P"},
    "NT1": {'nome': 'navio tanque',"tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "NT2": {'nome': 'navio tanque', "tamanho": 4, "coordenadas": [], "simbolo": "N"},
    "CT1": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CT2": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "CP3": {'nome': 'contratopedeiro', "tamanho": 3, "coordenadas": [], "simbolo": "C"},
    "S1": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S2": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S3": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"},
    "S4": {'nome': 'submarino', "tamanho": 2, "coordenadas": [], "simbolo": "S"}
}


# Changes player's char inputs to int
posicoes = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
}

# Does the reverse
posicoes_inverso = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J'
}

# Game functions

def exibir_tabuleiro(tabuleiro, nome_tabuleiro):
    '''Shows selected board.
        Args: 
            tabuleiro(list[list[str]]): Computer or player's board.
            nome_tabuleiro[str]: Board name'''
    print(f"\n{nome_tabuleiro}")
    # Shows column numbers on top
    numeros_colunas = "   " + " ".join([str(i) for i in range(10)])
    print(numeros_colunas)
    # Shows lines with letters and board
    for letra_linha, linha in zip(posicoes.keys(), tabuleiro):
        print(f"{letra_linha}  " + " ".join(linha))


def exibir_tabuleiros():
    '''Shows both visible boards'''
    exibir_tabuleiro(tabuleiro_player, "Your board:")
    exibir_tabuleiro(tabuleiro_pc_vw, "Computer's board:")


def posicionar_navios():
    '''Asks the player to position their ships.
    Positions ships on the board.
    Fills each ship position in the dictionary.
    '''
    print('Position your ships. ')
    for sigla, navios in navios_player.items(): # Iterates on each ship in the dictionary
        exibir_tabuleiro(tabuleiro_player, 'Your board:') # Shows board each time a position is set
        if navios['tamanho'] == 5: # As there's only one aircraft carrier, this line it o show apropriate text
            print('Position your aircraft carrier (5 spaces): ')
        else: # sigla [-1:] pega o último digito da sigla de cada navio para mostrar qual deles é
            print(f'Position your {sigla[-1:]}º {navios['nome']} ({navios['tamanho']} spaces): ')
        while True:
            orientacao = input('Vertical or horizontal orientation? V/H ').strip().upper()
            if orientacao == 'V':
                print(f'The {navios['nome']} will be positioned from top to bottom.')
                break
            elif orientacao == 'H':
                print(f'The {navios['nome']} will be positioned from right to left.')
                break
            else:
                continue
        while True:
            posicao_inicial = input(f"Input the {navios['nome']}'s first spot position (Ex.: A1, D7): ").upper().strip()
            try:
                # Prepares the coordinates
                x, y = posicao_inicial[0], posicao_inicial[1]
                y = int(y)
                x = posicoes[x]
                if orientacao == 'H':
                    # Verifies if adjecent spaces are empty and if the full length of the ship will fit on the board
                    # Identical for vertical position
                    posicao_valida = all(
                        all(
                            tabuleiro_player[m][n] == '~'
                            for m in range(x-1, x+2)
                            for n in range(b-1, b+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= b < 10 and 0 <= x < 10
                    for b in range(y, y+navios['tamanho'])
                    )
                    if posicao_valida:
                        for b in range(y, y + navios['tamanho']):
                            tabuleiro_player[x][b] = navios['simbolo'] # Draws on the board
                            coord = f'{posicao_inicial[0]}{b}'
                            navios['coordenadas'].append(coord) # Saves coordinates in dictionary 
                    else:
                        print("Invalid position. Your ship is touching another or is going out the board.")
                        continue                    
                elif orientacao == 'V':
                    posicao_valida = all(
                        all(
                            tabuleiro_player[m][n] == '~'
                            for m in range(a-1, a+2)
                            for n in range(y-1, y+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= y < 10 and 0 <= a < 10
                    for a in range(x, x+navios['tamanho'])
                    )
                    if posicao_valida:
                        for a in range(x, x + navios['tamanho']):
                            tabuleiro_player[a][y] = navios['simbolo']
                            coord = f'{posicoes_inverso[a]}{y}'
                            navios['coordenadas'].append(coord)
                    else:
                        print("Invalid position. Your ship is touching another or is going out the board.")
                        continue
            except Exception:
                print('Invalid position.')
                continue
            break

def gerar_posicoes_pc(): # Pretty much identical to posicionar_navios(), but using random and with no messages.
    '''Randomly generates the computer's ship's positions.
    Marks on the computer's reference board.
    Fills the position list in the dictionary'''
    for navios in navios_pc.values():
        orientacao = random.randint(0, 1)
        while True:
            try:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if orientacao == 0:
                    posicao_valida = all(
                        all(
                            tabuleiro_pc_hf[m][n] == '~'
                            for m in range(x-1, x+2)
                            for n in range(b-1, b+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= b < 10 and 0 <= x < 10
                    for b in range(y, y+navios['tamanho'])
                    )
                    if posicao_valida:
                        for b in range(y, y + navios['tamanho']):
                            tabuleiro_pc_hf[x][b] = navios['simbolo']
                            coord = f'{posicoes_inverso[x]}{b}'
                            navios['coordenadas'].append(coord)
                    else:
                        continue                    
                elif orientacao == 1:
                    posicao_valida = all(
                        all(
                            tabuleiro_pc_hf[m][n] == '~'
                            for m in range(a-1, a+2)
                            for n in range(y-1, y+2)
                            if 0 <= m < 10 and 0 <= n < 10   
                        ) and 0 <= y < 10 and 0 <= a < 10
                    for a in range(x, x+navios['tamanho'])
                    )
                    if posicao_valida:
                        for a in range(x, x + navios['tamanho']):
                            tabuleiro_pc_hf[a][y] = navios['simbolo']
                            coord = f'{posicoes_inverso[a]}{y}'
                            navios['coordenadas'].append(coord)
                    else:
                        continue
            except Exception:
                continue
            break


def atingiu_player(coordenada: int):
    '''Checks if the player hit and if they sank a computer's ship.
    Functions are separate due to the message to be displayed.
        Args:
            navios_pc(dict): Computer's ship dictionary.
            coordenada(str): Player's move coordinates.'''
    for navio in navios_pc.values():
        if coordenada in navio["coordenadas"]:
            print(f'You hit a {navio['nome']}!')
            time.sleep(2)
            navio["coordenadas"].remove(coordenada)  # Removes the hit coordinates from the apropriate list
            if not navio["coordenadas"]:  # Checks if the list is empty
                print(f"The {navio['nome']} was sank!")
                time.sleep(2)

def atingiu_pc(coordenada: int):
    '''Checks if the computer hit and if they sank a player's ship.
    Functions are separate due to the message to be displayed.
        Args:
            navios_player(dict): Player's ship dictionary.
            coordenada(str): Computer's move coordinates'''
    for navio in navios_player.values():
        if coordenada in navio["coordenadas"]:
            print(f'The computer hit a {navio['nome']}!')
            time.sleep(2)
            navio["coordenadas"].remove(coordenada)
            if not navio["coordenadas"]: 
                print(f"Your {navio['nome']} was sank!")
                time.sleep(2)

def verificar_vitoria(navios:dict) -> bool:
    '''Checks if every coordinate list in the dictionary are empty.
    Args:
        navios(dict): Player or computer ship information.
    Return: 
        bool: If won.'''
    return all(not navio["coordenadas"] for navio in navios.values())


def jogada_humano():
    while True:
        try:
            coordenada = input("Input a position (Eg.: A1, B4): ").upper().strip()
            x, y = coordenada[0], coordenada[1]  # Separates letter and number
            y = int(y)
            x = posicoes[x]  # Converts letter to the corresponding integer
            if tabuleiro_pc_vw[x][y] == "~":  # Checking if user chose an empty spot
                if tabuleiro_pc_hf[x][y] == "~":  # Checking if missed
                    print("You missed!")
                    tabuleiro_pc_vw[x][y] = "O"  # Marks miss
                    time.sleep(2)
                    break
                if tabuleiro_pc_hf[x][y] != "~":  # Checks if hit
                    tabuleiro_pc_vw[x][y] = 'X'
                    atingiu_player(coordenada)
                    if verificar_vitoria(navios_pc):
                        break
                    exibir_tabuleiros()
                    print("Play again.")
                    continue
            else:
                print("Invalid move. Try again.")
        except Exception:
            print("Invalid move. Try again.")


def jogada_pc():
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        coordenada = f'{posicoes_inverso[x]}{y}'
        if tabuleiro_player[x][y] == "O" or tabuleiro_player[x][y] == "X": #So the computer doesn't chose an occupied spot
            continue
        else:
            print(f'The computer chose {coordenada}.')
            time.sleep(2)
            if tabuleiro_player[x][y] == "~":
                print("The computer missed!")
                tabuleiro_player[x][y] = "O"
                time.sleep(2)
                break
            else:
                tabuleiro_player[x][y] = "X"
                atingiu_pc(coordenada)
                if verificar_vitoria(navios_player):
                    break
                exibir_tabuleiros()
                print("It will play again...")
                time.sleep(2)
                continue


if __name__ == '__main__':
    while True:
        gerar_posicoes_pc()
        posicionar_navios()
        # Main game
        while True:
            exibir_tabuleiros()  # Shows both boards after every move
            jogada_humano()  # Players move
            if verificar_vitoria(navios_pc):
                print('Congratulations! You won!')
                input()
                break
            exibir_tabuleiros()  # Shows boards again
            jogada_pc()  # Computer's move
            if verificar_vitoria(navios_player):
                print('What a shame! The computer won.')
                input()
                break
