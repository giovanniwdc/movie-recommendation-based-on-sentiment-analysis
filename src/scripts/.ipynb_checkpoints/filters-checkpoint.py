import csv

def filter_rows(input_file_name, output_file_name, filtr, n = 1000):

	with open(input_file_name, 'r') as inpt:

		line = inpt.readline()

		with open(output_file_name, 'w') as out:

			line = [l for l in line.replace('\n', '').split(',')]

			writer = csv.writer(out)
			
			writer.writerow(line)

			count = 0

			while count < 1000:

				line = inpt.readline()

				if line:

					try:

						line = [l for l in line.replace('\n', '').split(',')]

						if filtr(line):
							writer.writerow(line)

					except:

						if line '\n':

							print(f'Error in the line: {count}\ndata: {line}\n')

				else:

					break

				count += 1

			print(f'Your file was filtered with success!\nNumber of lines: {count}')