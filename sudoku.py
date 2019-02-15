import argparse
import sudoku.rules as sr

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

rule = sr.Rules(4)

for r in rule.get_all_possibles(sudoku):
    print (r)








