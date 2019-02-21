import os
import argparse
from sudoku.sudoku_problem import sudoku_problem
from graphsearch.graph_search import gen_criteria, graph_search, a_star
from graphsearch.list_to_table import get_sudoku_table

# get sudoku
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--data", required=True,
    help="ingrese información sobre el estado inicial del sudoku")

args = vars(ap.parse_args())
data = args["data"]

if len(data) != 16:
    print("Hay información de más o de menos")
    exit()

sudoku = list(data)
sudoku = list(map(lambda x: 0 if x == '.' else int(x), sudoku))

sudoku_problem = sudoku_problem(4, sudoku)

a_star_criteria = gen_criteria(a_star)

explored = [[]]

result = graph_search(sudoku_problem, a_star_criteria)

get_sudoku_table(result, 4)










