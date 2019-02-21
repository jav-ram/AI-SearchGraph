import os

def get_table_sudoku(data, row_length):
    table = '<table>'
    counter = 0
    for element in data:
        if counter % row_length == 0:
            table += '<tr>'
        if element == 0 or element == '0':
            table += '<td class="empty">%s</td>' % element
        else:
            table += '<td>%s</td>' % element
        counter += 1
        if counter % row_length == 0:
            table += '</tr>'
    if counter % row_length != 0:
        for i in range(0, row_length - counter % row_length):
            table += '<td>&nbsp;</td>'
        table += '</tr>'
    table += '</table>'
    return table


def get_sudoku_table(states, size, name):
    html = '<!DOCTYPE html>' \
           '<html>' \
           '<head> \
                <link rel="stylesheet" type="text/css" href="sudoku.css"> \
            </head>' \
           '<body>'

    for step in states:
        html += get_table_sudoku(step, size)

    html += '</body></html>'

    with open(os.path.join('./', name), "w") as file:
        file.write(html)
    return 0


def get_fifteen_table(states, size, name):
    html = '<!DOCTYPE html>' \
           '<html>' \
           '<head> \
                <link rel="stylesheet" type="text/css" href="fifteen.css"> \
            </head>' \
           '<body>'

    for step in states:
        html += get_table_sudoku(step, size)

    html += '</body></html>'

    with open(os.path.join('./', name), "w") as file:
        file.write(html)
    return 0

