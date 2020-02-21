#Given a list of songs, write an efficient program to play them without repitition
#Asked by Amazion [EASY]


songs = ['Falling','Shape Of You','Without Me','Not Afraid','RapGod','The Real Slim Shady','Kings Never Die','Phenominal','Lose Yourself','Smooth Criminal','Natural']
played = []
for song in songs:
	if song not in played:
		print(song)
		played.append(song)
print('All songs played!')
			