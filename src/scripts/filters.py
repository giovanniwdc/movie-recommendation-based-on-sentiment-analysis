import csv

def filter_rows(input_path, output_path, filtr, n = 1000):

	with open(input_path, 'r') as inpt:

		line = inpt.readline()

		with open(output_path, 'w') as out:

			line = [l for l in line.replace('\n', '').split(',')]

			writer = csv.writer(out)
			
			writer.writerow(line)

			count = 0

			while count < n:

				line = inpt.readline()

				if line:

					try:

						line = [l for l in line.replace('\n', '').split(',')]

						if filtr(line):
							
							writer.writerow(line)
							count += 1

					except:

						if line != '\n':

							print(f'Error in the line: {count}\ndata: {line}\n')

				else:

					break

				

			print(f'Your file was filtered with success!\nNumber of lines: {count}')