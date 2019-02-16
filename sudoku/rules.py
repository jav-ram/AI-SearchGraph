import math


class sudoku_rules:
    def __init__(self, width):
        self.width = width
        self.square_root = int(round(self.width**(1/2.0)))
        self.acceptable_numbers = set([x for x in range(1, self.width+1)])

    def get_empties(self, state):
        result = []
        for i in range(0, len(state)):
            if state[i] == 0:
                point = {}
                point['y'] = int(i / self.width)
                point['x'] = i % self.width
                result.append(point)
        return result

    def get_all_possibles(self, state):
        empties = self.get_empties(state)
        result = []
        for empty in empties:
            possibles = self.possibles(state, empty['x'], empty['y'])
            for possible in possibles:
                result.append({
                    'position': (empty['y'] * self.width + empty['x']),
                    'value': possible
                });

        return result

    def not_possibles(self, state, x, y):

        result = []
        # get numbers in rows
        for i in range(4):
            number = state[y*self.width + i]
            if number != 0:
                result.append(number)

        # get numbers in cols
        for j in range(4):
            number = state[j * self.width + x]
            if number != 0:
                result.append(number)

        # get numbers inside square
        xm = math.floor(x / self.square_root)
        ym = math.floor(y / self.square_root)

        for j in range(ym*self.square_root, ym*self.square_root+self.square_root):
            for i in range(xm*self.square_root, xm*self.square_root+self.square_root):
                number = state[j * self.width + i]
                if number != 0:
                    result.append(number)

        return set(result)

    def possibles(self, state, x, y):
        if state[y*self.width + x] != 0:
            return []

        return list(self.acceptable_numbers - self.not_possibles(state, x, y))

    def goal_test(self, state):
        # checkea todas las posiciones y verifica que la cantidad de Numeros que NO se pueden poner sea == width
        for j in range(0, self.width):
            for i in range(0, self.width):
                if len(self.not_possibles(state, i, j)) != self.width:
                    return False
        return True

    def put(self, state, position, value):
        new_state = state
        new_state[position] = value

        return new_state

    def cost(self, state, action):
        return 1


