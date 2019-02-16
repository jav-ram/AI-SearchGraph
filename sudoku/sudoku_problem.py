import math
from graphsearch.problem import Problem


class sudoku_problem(Problem):

    def __init__(self, size, initial):
        self.size = size
        self.square_root = int(round(self.size ** (1 / 2.0)))
        self.acceptable_numbers = set([x for x in range(1, self.size + 1)])

        Problem.__init__(self=self, initial_state=initial)

    # Actions
    def actions(self, state):
        return self.__get_all_possibles(state)

    def __get_empties(self, state):
        result = []
        for i in range(0, len(state)):
            if state[i] == 0:
                point = {}
                point['y'] = int(i / self.size)
                point['x'] = i % self.size
                result.append(point)
        return result

    def __get_all_possibles(self, state):
        empties = self.__get_empties(state)
        result = []
        for empty in empties:
            possibles = self.__possibles(state, empty['x'], empty['y'])
            for possible in possibles:
                result.append({
                    'position': (empty['y'] * self.size + empty['x']),
                    'value': possible
                });

        return result

    def __not_possibles(self, state, x, y):

        result = []
        # get numbers in rows
        for i in range(4):
            number = state[y*self.size + i]
            if number != 0:
                result.append(number)

        # get numbers in cols
        for j in range(4):
            number = state[j * self.size + x]
            if number != 0:
                result.append(number)

        # get numbers inside square
        xm = math.floor(x / self.square_root)
        ym = math.floor(y / self.square_root)

        for j in range(ym*self.square_root, ym*self.square_root+self.square_root):
            for i in range(xm*self.square_root, xm*self.square_root+self.square_root):
                number = state[j * self.size + i]
                if number != 0:
                    result.append(number)

        return set(result)

    def __possibles(self, state, x, y):
        if state[y*self.size + x] != 0:
            return []

        return list(self.acceptable_numbers - self.__not_possibles(state, x, y))

    # RESULT
    def result(self, state, action):
        return self.__put(state, action['position'], action['value'])

    def __put(self, state, position, value):
        new_state = state.copy()
        new_state[position] = value

        return new_state

    # GOAL TEST
    def goal_test(self, state):
        # checkea todas las posiciones y verifica que la cantidad de Numeros que NO se pueden poner sea == width
        for j in range(0, self.size):
            for i in range(0, self.size):
                if len(self.__not_possibles(state, i, j)) != self.size:
                    return False
        return True

    # COST
    def step_cost(self, state, action):
        y = int(action['position'] / self.size)
        x = action['position'] % self.size
        cant = self.__possibles(state, x, y)
        return (len(cant) / self.size)

    def states_to_action(self, state_1, state_2):
        for i in range(0, len(state_1)):
            if state_1[i] != state_2[i]:
                return {
                    'position': i,
                    'value': state_2[i]
                }

    # PATH COST
    def path_cost(self, states):
        total_cost = 0
        for i in range(0, len(states) - 1):
            action = self.states_to_action(states[i], states[i+1])
            total_cost += self.step_cost(states[i], action)
        return total_cost

    # HEURISTIC
    def heuristic(self, state, action):
        new_state = self.result(state, action)
        empties = self.__get_empties(new_state)
        return len(empties)



