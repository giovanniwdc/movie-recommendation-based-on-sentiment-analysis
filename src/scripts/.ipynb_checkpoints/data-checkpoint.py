data_reveiws = open('../../data/combined_data_1.txt')
data_films = open('../../data/movie_titles.csv')

line = data_reveiws.readline()
film = ''

file = 1
data_file = 1
film_id = 0

n_reviews = 0

out = open(f'../../data/processed_{file}/data{data_file}.txt','w')

while line:

	if line == f"{film_id+1}:\n":
		
		film_id += 1
		film = data_films.readline()	

	else:
		line = line.replace("\n","")
		out.write(f'{line},{film}')

		n_reviews += 1

		if n_reviews == 1000:

			n_reviews = 0
			data_file += 1

			out.close()
			out = open(f'../../data/processed_{file}/data{data_file}.txt','w')

	line = data_reveiws.readline()

	if not line and file < 4:

		file += 1
		data_file = 1
		data_reveiws = open(f'../../data/combined_data_{file}.txt')

		out.close()
		out = open(f'../../data/processed_{file}/data{data_file}.txt','w')



		print(f'pasta: {file}\n arquivo: {data_file}')

		line = data_reveiws.readline()
	












