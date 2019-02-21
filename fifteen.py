import time
import argparse
from fifteen.fifteen_problem import fifteen_problem
from graphsearch.graph_search import gen_criteria, graph_search, a_star

# get sudoku
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True,
    help="ingrese información sobre el estado inicial del sudoku")

args = vars(ap.parse_args())
data = args["data"]

if len(data) != 16:
    print("Hay información de más o de menos")
    exit()

board = list(data)
board = list(map(lambda x: x if x != '.' else '0', board))

fifteen_problem = fifteen_problem(board)

a_star_criteria = gen_criteria(a_star)


start = time.time()
result = graph_search(fifteen_problem, a_star_criteria)
end = time.time()


print(result)
print(end - start)
