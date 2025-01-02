class AlphaBetaPruning:
    def __init__(self, game_state,depth,player): # Initialize the depth, current game state, and player (maximizer or minimizer)

        self.game_state = game_state
        self.depth = depth
        self.player = player
        self.counter = 0

    def is_terminal(self, state):
        win = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6] 
        ]
        for combo in win:
            if state[combo[0]] == state[combo[1]] == state[combo[2]] and state[combo[0]] != " ":
                return True
        return " " not in state
        # w = [[0,1,2] , [3,4,5] , [6,7,8], [0,3,6],[0,4,8], [2,4,6],[1,4,7],[2,5,8]]
        # for i in w:
        #     # print((state[i[0]])[0])
        #     if (state[i[0]])[0] == (state[i[1]])[1] == (state[i[2]])[2] and state[i[0]] != ' ':
        #         return True
        # return Fals

    def utility(self, state):
        win = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win:
            if state[combo[0]] == state[combo[1]] == state[combo[2]]:
                if state[combo[0]] == "X":
                    return 1
                elif state[combo[0]] == "O":
                    return -1
        return 0
        
                
        # return 0
    def alphabeta(self, state,alpha,beta, depth, maximizing_player):
        self.counter += 1

        if self.is_terminal(state) or depth == 0:
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(len(state)):
                if state[i] == " ":
                    state[i] = "X"
                    eval = self.alphabeta(state, alpha,beta,depth - 1, False)
                    state[i] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break 
                    
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(len(state)):
                if state[i] == " ":
                    state[i] = "O"
                    eval = self.alphabeta(state,alpha,beta, depth - 1, True)
                    state[i] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval
    
    def best_move(self, state):
        best_val = float('-inf')
        best_move = -1
        alpha=float('-inf')
        beta=float('inf')
        for i in range(len(state)):
            if state[i] == " ":
                
                state[i] = "X"
                move_val = self.alphabeta(state,alpha,beta , 3, False)
                state[i] = " "

                if move_val > best_val:
                    best_val = move_val
                    best_move = i

        return best_move


def main():
    game_state = ["X", "O", " ",
                  " ", " ", " ",
                  "O", " ", " "]

    m = AlphaBetaPruning(game_state,3,True)
    print(m.best_move(game_state))
    print(m.counter)
main()
# def main():
#     game = [["X","O"," "],[" "," "," "],["O"," "," "]]
#     g = AlphaBetaPruning(game ,3, True)
#     # g1 = AlphaBetaPruning(game , 3, True)
#     gg = g.best_move(game)
#     # gg1 = g1.best_move(game)
#     # print(g1.counter)
#     print(g.counter)
# main()
# def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
    #     # print("hello")
    #     self.counter += 1
    #     if depth == 0 or self.is_terminal(state):
    #         # print('yes')
    #         return self.utility(state)

    #     if maximizing_player:
    #         max_eval = float('-inf')
    #         for child in self.get_children(state):
    #             eval = self.alphabeta(child, self.depth - 1, alpha, beta, False)
    #             max_eval = max(max_eval, eval)
    #             alpha = max(alpha, eval)
    #             if beta <= alpha:
    #                 break  
    #         return max_eval
    #     else:
    #         min_eval = float('inf')
    #         for child in self.get_children(state):
    #             eval = self.alphabeta(child, self.depth - 1, alpha, beta, True)
    #             min_eval = min(min_eval, eval)
    #             beta = min(beta, eval)
    #             if beta <= alpha:
    #                 break 
    #         return min_eval
        # best_val = float('-inf')
        # best_move = None
        # for move in self.get_available_moves(state):
        #     alpha=float('-inf')
        #     beta=float('inf')
        #     move_val = self.alphabeta(move, self.depth, alpha, beta, self.player)
        #     if move_val > best_val:
        #         best_val = move_val
        #         best_move = move
        # return best_move

    # def get_available_moves(self,state):
        
    #     children = []
    #     for i in range(3):
    #         for j in range(3):
    #             if self.game_state[i][j] == ' ':
    #                 dummy = self.generate_state(state)
    #                 if self.player:
    #                     dummy[i][j] = "X"
    #                 else:
    #                     dummy[i][j] = "O" 
    #                 children.append(dummy)
    #     # print(children)
    #     return children
            
    # def generate_state(self,state):
    #     l = [i for i in state]
    #     return  l

# w = [[0,1,2] , [3,4,5] , [6,7,8], [0,3,6],[0,4,8], [2,4,6],[1,4,7]]
        # for i in w:
        #     # print((state[i[0]])[0])
        #     if (state[i[0]])[0] == (state[i[1]])[1] == (state[i[2]])[2]:
        #         if (state[i[0]])[0] == "O":
        #             return 1
        #         elif (state[i[0]])[0] == "X":
        #             return -1 