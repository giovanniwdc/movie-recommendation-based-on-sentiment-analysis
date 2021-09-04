import numpy as np
import pandas as pd
import csv

id_paste = 1
id_file = 1

CHUNK_SIZE = 50000

output_file = "../../data/output.csv"
log = "../../data/log.txt"

first_one = True

while True:

	try:
		if not first_one: # if it is not the first csv file then skip the header row (row 0) of that file
			skip_row = [0]
		else:
			skip_row = []

		chunk_container = pd.read_csv(f'../../data/ordered_{id_paste}/data{id_file}.txt', usecols = [i for i in range(5)], skiprows = skip_row)

		chunk_container.to_csv(output_file, mode="a", index=False)
		
		first_one = False

		id_file += 1
			
	except:
		with open(log, 'w') as f:

			inp = input(f'tenta o próximo: paste {id_paste}, file {id_file}?')

			if inp == 's':
				id_file += 1

				f.write(f'paste {id_paste}, file {id_file}')
			
			elif id_paste < 4:
			
				id_paste += 1
				id_file = 1

			else:
				break

		