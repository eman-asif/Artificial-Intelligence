class Minimax:
    def __init__(self, game_state):
        self.game_state = game_state
        self.counter = 0

    def is_terminal(self, state):#This method checks if the game has reached a terminal state, which could be a win
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]  # diagnoals
        ]
        for combo in winning_combinations:
            if state[combo[0]] == state[combo[1]] == state[combo[2]] and state[combo[0]] != " ":
                return True
        return " " not in state

    def utility(self, state):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if state[combo[0]] == state[combo[1]] == state[combo[2]]:
                if state[combo[0]] == "X":
                    return 1
                elif state[combo[0]] == "O":
                    return -1
        return 0

    def minimax(self, state, depth, maximizing_player):
        self.counter += 1

        if self.is_terminal(state) or depth == 0:
            return self.utility(state)

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(len(state)):
                if state[i] == " ":
                    state[i] = "X"
                    eval = self.minimax(state, depth - 1, False)
                    state[i] = " "
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(len(state)):
                if state[i] == " ":
                    state[i] = "O"
                    eval = self.minimax(state, depth - 1, True)
                    state[i] = " "
                    min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, state):
        best_val = float('-inf')
        best_move = -1

        for i in range(len(state)):
            if state[i] == " ":

                state[i] = "X"
                move_val = self.minimax(state,  3, False)
                state[i] = " "

                if move_val > best_val:
                    best_val = move_val
                    best_move = i

        return best_move


def main():
    game_state = ["X", "O", " ",
                  " ", " ", " ",
                  "O", " ", " "]

    m = Minimax(game_state)
    print(m.best_move(game_state))
    print(m.counter)
main()