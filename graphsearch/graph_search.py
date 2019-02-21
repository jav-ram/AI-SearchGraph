

def graph_search(problem, criteria):
    frontier = [[problem.initial()]]
    explored = []

    while True:
        if len(frontier):
            path = criteria(frontier, problem)
            s = path[-1].copy()
            explored.append(s)

            if problem.goal_test(s):
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)

                if not is_explored(path.copy(), result, explored):
                    new_path = []
                    new_path = path.copy()
                    new_path.append(result)
                    frontier.append(new_path)

        else:
            return False


def gen_criteria(condition):
    def criteria(frontier, problem):
        target = 0
        if len(frontier) == 1:
            target = frontier[0].copy()
            frontier.remove(target)
            return target

        for f in frontier:
            target = condition(f, target, problem)

        frontier.remove(target)

        return target

    return criteria


def a_star(frontier, target, problem):
    frontier_action = problem.states_to_action(frontier[-2], frontier[-1])
    frontier_total = problem.path_cost(frontier) + problem.heuristic(frontier[-2], frontier_action)

    if target == 0:
        return frontier

    target_action = problem.states_to_action(target[-2], target[-1])
    target_total = problem.path_cost(target) + problem.heuristic(target[-2], target_action)

    if frontier_total < target_total:
        return frontier

    else:
        return target


def is_explored(path, result, explored):
    for e in explored:
        if e == result:
            return True

    return False
