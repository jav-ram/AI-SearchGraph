import math
from graphsearch.problem import Problem

TOP = '0'
RIGHT = '1'
BOTTOM = '2'
LEFT = '3'

COMPLETED = [
    '1','2','3','4',
    '5','6','7','8',
    '9','A','B','C',
    'D','E','F','0'
]

class fifteen_problem(Problem):

    def __init__(self, initial):
        self.size = 4
        Problem.__init__(self=self, initial_state=initial)

    # Actions
    def actions(self, state):
        return self.__moves(state)

    def __get_position(self, state):
        for i in range(0, len(state)):
            if state[i] == '0':
                return i

    def __neighbors(self, state):
        position = self.__get_position(state)
        possibles = [True, True, True, True]

        # se encuentra en la parte superior o inferior
        if position < 4:
            possibles[0] = False
        elif position > 11:
            possibles[2] = False

        # se encuentra en el extremo derecho o izquierdo
        if (position + 1) % self.size == 0:
            possibles[1] = False
        elif position % self.size == 0:
            possibles[3] = False

        return possibles

    def __moves(self, state):
        neighbors = self.__neighbors(state)
        moves = []

        if neighbors[0]:
            moves.append(TOP)
        if neighbors[1]:
            moves.append(RIGHT)
        if neighbors[2]:
            moves.append(BOTTOM)
        if neighbors[3]:
            moves.append(LEFT)

        return moves

    # Result
    def result(self, state, action):
        position = self.__get_position(state)
        new_state = state.copy()

        if action == TOP:
            to_change_position = position - self.size
            to_change = new_state[to_change_position]
            new_state[to_change_position] = '0'
            new_state[position] = to_change
            return new_state
        elif action == RIGHT:
            to_change_position = position + 1
            to_change = new_state[to_change_position]
            new_state[to_change_position] = '0'
            new_state[position] = to_change
            return new_state
        elif action == BOTTOM:
            to_change_position = position + self.size
            to_change = new_state[to_change_position]
            new_state[to_change_position] = '0'
            new_state[position] = to_change
            return new_state
        elif action == LEFT:
            to_change_position = position - 1
            to_change = new_state[to_change_position]
            new_state[to_change_position] = '0'
            new_state[position] = to_change
            return new_state

    # GOAL TEST
    def goal_test(self, state):
        for i in range(0, len(state)):
            if not state[i] == COMPLETED[i]:
                return False


        return True

    # STEP COST
    def step_cost(self, state, action):
        return 0

    def __distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def states_to_action(self, state_1, state_2):
        position_1 = self.__get_position(state_1)
        position_2 = self.__get_position(state_2)
        dif = position_1 - position_2

        if dif == 4:
            return TOP
        elif dif == -4:
            return BOTTOM
        elif dif == -1:
            return RIGHT
        elif dif == 1:
            return LEFT


    # PATH COST
    def path_cost(self, states):
        #total_cost = 0
        #for i in range(0, len(states) - 1):
        #    action = self.states_to_action(states[i], states[i + 1])
        #    total_cost += self.step_cost(states[i], action)
        return 0

    # HEURISTIC
    def heuristic(self, state, action):
        new_state = self.result(state, action)
        result = 0

        for i in range(0, len(new_state)):
            if not new_state[i] == '0':
                correct_position = int(new_state[i], 16) - 1

                y1 = int(i / 4)
                x1 = i % 4

                y2 = int(correct_position / 4)
                x2 = correct_position % 4

                result += (self.__distance(x1, y1, x2, y2)) * (correct_position + 1)
        return result



