import camelot

tables = camelot.read_pdf('./tables.pdf', pages='1')
print(tables)

tables.export('tables.csv', f='csv', compress=True)
tables[0].to_csv('table.csv')