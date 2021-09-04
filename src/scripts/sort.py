import numpy as np
import csv

# dtype = [('id_user', int), ('reting', 'S10'), ('data', 'S10'), ('id_film','S10'), ('year','S10'), ('film_name', 'S10')]


def convert_index(v):
	v[0] = int(v[0])
	return v

def order_file_by_index(file):

	lines = [convert_index(line.replace('\n','').split(',')) for line in file.readlines()]

	return sorted(lines, key = lambda line: line[0])


id_paste = 1
id_file = 1

while True:

	try:

		inpt = open(f'../../data/processed_{id_paste}/data{id_file}.txt','r')

		new_lines = order_file_by_index(inpt)
		inpt.close()
		
		with open(f'../../data/ordered_{id_paste}/data{id_file}.txt', 'w') as f:
			filds = ['id_user', 'rating', 'deta', 'id_film', 'year', 'name'] 
			write = csv.writer(f)
		      
			write.writerow(filds)
			write.writerows(new_lines)

			id_file += 1

	except:
		print('oi')
		if id_paste < 4:
			
			id_paste += 1
			id_file = 1

		else:
			break


  
# data_reveiws = open('../../data/combined_data_1.txt')
# data_films = open('../../data/movie_titles.csv')

# open(f'../../data/processed_{file}/data{data_file}.txt','w')