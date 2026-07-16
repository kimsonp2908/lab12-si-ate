"""
Tic-Tac-Toe game with Minimax AI.
El agente usa Minimax para elegir la mejor jugada.
"""

import math
import random
from typing import Optional, Tuple, List

# Constantes del juego
PLAYER_X = 'X'  # Jugador humano
PLAYER_O = 'O'  # Agente IA
EMPTY = ' '

class TicTacToe:
    """Clase principal del juego Tres en Raya."""
    
    def __init__(self):
        """Inicializa el tablero vacio."""
        self.board = [EMPTY] * 9  # 3x3 representado como lista de 9 elementos
        self.current_winner = None
    
    def display_board(self):
        """Muestra el tablero en consola."""
        print("\n")
        for i in range(0, 9, 3):
            row = self.board[i:i+3]
            print(" " + " | ".join(row))
            if i < 6:
                print("---+---+---")
        print("\n")
    
    def make_move(self, position: int, player: str) -> bool:
        """
        Realiza un movimiento en el tablero.
        
        Args:
            position: Posicion (0-8)
            player: 'X' o 'O'
        
        Returns:
            True si el movimiento fue valido, False en caso contrario.
        """
        if position < 0 or position > 8:
            return False
        if self.board[position] != EMPTY:
            return False
        
        self.board[position] = player
        
        # Verificar si este movimiento gano
        if self.check_winner():
            self.current_winner = player
        
        return True
    
    def check_winner(self) -> bool:
        """
        Verifica si hay un ganador en el tablero actual.
        
        Returns:
            True si hay un ganador, False en caso contrario.
        """
        # Combinaciones ganadoras (filas, columnas, diagonales)
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] != EMPTY and
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                return True
        return False
    
    def is_board_full(self) -> bool:
        """Verifica si el tablero esta lleno (empate)."""
        return EMPTY not in self.board
    
    def get_available_moves(self) -> List[int]:
        """Retorna lista de posiciones disponibles."""
        return [i for i, cell in enumerate(self.board) if cell == EMPTY]
    
    def evaluate(self) -> int:
        """
        Evalua el tablero desde la perspectiva de la IA (O).
        
        Returns:
            10 si gana O, -10 si gana X, 0 si empate.
        """
        if self.current_winner == PLAYER_O:
            return 10
        elif self.current_winner == PLAYER_X:
            return -10
        else:
            return 0
    
    def minimax(self, depth: int, is_maximizing: bool, alpha: float = -math.inf, beta: float = math.inf) -> Tuple[int, Optional[int]]:
        """
        Implementacion de Minimax con Poda Alfa-Beta.
        
        Args:
            depth: Profundidad actual en el arbol
            is_maximizing: True si es turno de MAX (IA), False si es MIN (humano)
            alpha: Valor alfa para poda
            beta: Valor beta para poda
        
        Returns:
            Tuple (puntaje, mejor_posicion)
        """
        # Caso base: si hay ganador o empate
        if self.current_winner == PLAYER_O:
            return 10 - depth, None  # Priorizar victorias mas rapidas
        elif self.current_winner == PLAYER_X:
            return -10 + depth, None  # Priorizar derrotas mas lentas
        elif self.is_board_full():
            return 0, None
        
        available_moves = self.get_available_moves()
        
        if is_maximizing:
            # Jugador MAX (IA - O)
            best_score = -math.inf
            best_move = available_moves[0]
            
            for move in available_moves:
                # Simular movimiento
                self.make_move(move, PLAYER_O)
                
                # Llamada recursiva
                score, _ = self.minimax(depth + 1, False, alpha, beta)
                
                # Deshacer movimiento
                self.board[move] = EMPTY
                self.current_winner = None
                
                # Actualizar mejor puntaje
                if score > best_score:
                    best_score = score
                    best_move = move
                
                # Poda Alfa-Beta
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            
            return best_score, best_move
        
        else:
            # Jugador MIN (Humano - X)
            best_score = math.inf
            best_move = available_moves[0]
            
            for move in available_moves:
                # Simular movimiento
                self.make_move(move, PLAYER_X)
                
                # Llamada recursiva
                score, _ = self.minimax(depth + 1, True, alpha, beta)
                
                # Deshacer movimiento
                self.board[move] = EMPTY
                self.current_winner = None
                
                # Actualizar mejor puntaje
                if score < best_score:
                    best_score = score
                    best_move = move
                
                # Poda Alfa-Beta
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            
            return best_score, best_move
    
    def get_ai_move(self) -> Optional[int]:
        """
        Obtiene la mejor jugada para la IA usando Minimax.
        
        Returns:
            Posicion (0-8) de la mejor jugada.
        """
        if len(self.get_available_moves()) == 0:
            return None
        
        # Si es el primer movimiento, elegir aleatorio (optimizacion)
        if self.board.count(EMPTY) == 9:
            return random.choice([0, 2, 4, 6, 8])  # Esquinas o centro
        
        _, best_move = self.minimax(0, True)
        return best_move
    
    def reset(self):
        """Reinicia el tablero."""
        self.board = [EMPTY] * 9
        self.current_winner = None


def play_game():
    """Funcion principal para jugar contra la IA."""
    game = TicTacToe()
    
    print("=" * 50)
    print("BIENVENIDO AL TRES EN RAYA")
    print("=" * 50)
    print("\nTu eres X, la IA es O")
    print("Posiciones del tablero:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
    print("\nElige un numero (0-8) para jugar!\n")
    
    # Decidir quien empieza
    start = input("Quieres empezar tu? (s/n): ").lower()
    player_turn = start == 's'
    
    while True:
        game.display_board()
        
        # Verificar ganador
        if game.current_winner:
            if game.current_winner == PLAYER_O:
                print("La IA ha ganado!")
            else:
                print("Felicidades! Has ganado.")
            break
        
        if game.is_board_full():
            print("Empate!")
            break
        
        if player_turn:
            # Turno del jugador
            print("Es tu turno (X)")
            try:
                move = int(input("Posicion (0-8): "))
                if not game.make_move(move, PLAYER_X):
                    print("Movimiento invalido. Intenta de nuevo.")
                    continue
            except ValueError:
                print("Por favor, ingresa un numero valido.")
                continue
        else:
            # Turno de la IA
            print("La IA esta pensando...")
            move = game.get_ai_move()
            if move is not None:
                game.make_move(move, PLAYER_O)
                print(f"La IA jugo en la posicion {move}")
        
        # Cambiar turno
        player_turn = not player_turn
    
    # Mostrar tablero final
    game.display_board()
    
    # Preguntar si quiere jugar de nuevo
    play_again = input("\nQuieres jugar de nuevo? (s/n): ").lower()
    if play_again == 's':
        play_game()
    else:
        print("Gracias por jugar!")


if __name__ == "__main__":
    play_game()