class Minimax: 
    def __init__(self, game_state): 
    # Initialize with the current game state
        self.game_state = game_state
        self.counter = 0 
         
    def is_terminal(self, state): 
        w = [[0,1,2] , [3,4,5] , [6,7,8], [0,3,6],[0,4,8], [2,4,6],[1,4,7]]
        for i in w:
            if state[i[0]] == state[i[1]] == state[i[2]] and state[i[0]] != ' ':
                return True
        return False
             
    # Check if the game has reached a terminal state (win/lose/draw) 
    def utility(self, state): 
        w = [[0,1,2] , [3,4,5] , [6,7,8], [0,3,6],[0,4,8], [2,4,6],[1,4,7]]
        for i in w:
            if state[i[0]] == state[i[1]] == state[i[2]]:
                if state[i[0]] == "O":
                    return 1
                elif state[i[0]] == "X":
                    return -1
                
        return 0

    def minimax(self, state, depth, maximizing_player):
        if self.is_terminal(state) or depth == 0:
            return self.utility(state)
    
        if maximizing_player:
            max_eval = float("-inf")
            for action in self.get_available_moves(state):
                eval = self.minmax(action, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for action in self.get_available_moves(state):
                eval = self.minmax(action, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval 
        
    def best_move(self, state): 
    # Determine the best move using Minimax 
        
            best_val = float("-inf")
            best_move = None
            for action in self.get_available_moves(state):
                new_state = state.copy()
                new_state[action] = "O"  
                move_val = self.minimax(new_state, depth=5, maximizing_player=False)
                if move_val > best_val:
                    best_val = move_val
                    best_move = action
            return best_move
    def get_available_moves(self, state):
        return [i for i, spot in enumerate(state) if spot == ' ']
def main():
    game = [["X","O"," "],[" "," ","O"],["X","O"," "]]
    g = Minimax(game)
    # g1 = AlphaBetaPruning(game , 3, True)
    gg = g.best_move(game)
    # gg1 = g1.best_move(game)
    # print(g1.counter)
    # print(g.counter)
main()