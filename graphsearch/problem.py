class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.state = self.initial_state

    def initial(self):
        return self.actions(self.initial_state)

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        pass

    def step_cost(self, state, action, next_state):
        pass

    def path_cost(self, states):
        pass