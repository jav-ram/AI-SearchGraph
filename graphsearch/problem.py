class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def initial(self):
        return self.initial_state

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        pass

    def step_cost(self, state, action, result):
        pass

    def heuristic(self, state, action):
        pass

    def path_cost(self, states):
        pass

    def states_to_action(self, state_1, state_2):
        pass