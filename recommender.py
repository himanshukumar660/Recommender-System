_data_r  = open("../input/ratings.csv", "r");
_data_m  = open("../input/movies.csv", "r");

entries_m = _data_m.readlines();
movie_dict = {}

number_of_films = 100#int(entries_m[-1].split(",")[0])

skip = 1
for each in entries_m:
	if skip==1:
		skip=0
		continue
	idx = each.split(",")[0]
	name = each.split(",")[1]
	movie_dict[idx] = name

entries = _data_r.readlines();

ratings = []
skip = 1

number_of_users = int(entries[-1].split(",")[0])

for i,each in enumerate(entries):
	if i>number_of_users:
		break

	if skip:
		skip = 0
		continue
	data = each[:-2].split(",")
	data[0] = int(data[0])
	data[1] = int(data[1])
	data[2] = float(data[2])
	data[3] = int(data[3])
	ratings.append(data)

rMatrix = []

for j in range(1, number_of_users+2):
	ind_data = []
	for i in range(1, number_of_films+2):
		ind_data.append("null")
	#print(len(ind_data))
	rMatrix.append(ind_data)

for each in ratings:
	if len(rMatrix)<each[0] or len(rMatrix[0])<each[1]:
		continue
		#print(len(rMatrix),len(rMatrix[0]), each[0],each[1])
	else:
		rMatrix[each[0]][each[1]] = float(each[2]) 

my_dict = {}
for i in range(1, number_of_users+1):
	for j in range(1,number_of_films+1):
		for k in range(j+1, number_of_films+1):
			if rMatrix[i][j]!="null" and rMatrix[i][k]!="null":
				temp = 0
				temp2 = 0
				if (j,k) in my_dict.keys():
					temp = my_dict[(j,k)][0]
					temp2 = my_dict[(j,k)][1]
					my_dict[(j,k)][0] = temp*temp2+ rMatrix[i][j] - rMatrix[i][k]
					my_dict[(j,k)][1] = temp2+1;
				else:
					my_dict[(j,k)] = [0,0]
					my_dict[(j,k)][0] = temp*temp2+ rMatrix[i][j] - rMatrix[i][k]
					my_dict[(j,k)][1] = 1;

temp_dict = {}

for i in range(1, number_of_users+1):
	for j in range(1, number_of_films+1):
#		print("Checking")
		if rMatrix[i][j]=="null":
			idx = j
			aggr_r = 0
			total = 0
			found = 0

			for each in my_dict:
				if each[0]==idx or each[1]==idx:
					found=1
					avg = float(float(my_dict[each][0])/my_dict[each][1])
					total = total + my_dict[each][1]

					if each[0]==idx:
						aggr_r = aggr_r +\
									((float(0) if rMatrix[i][each[1]]=="null" else float(rMatrix[i][each[1]])) + \
									avg)*my_dict[each][1]
					
					else:
						aggr_r = aggr_r + \
									((float(0) if rMatrix[i][each[0]]=="null" else float(rMatrix[i][each[0]])) - \
									avg)*my_dict[each][1]

				#	print ((float(0) if rMatrix[i][each[1]]=="null" else float(rMatrix[i][each[1]])), idx, avg, each, aggr_r, total)

			if found:
				temp_dict[(i,j)] = float(aggr_r/total)

for i in range(0, number_of_users+1):
	for j in range(0,number_of_films+1):
	    if rMatrix[i][j]=="null":
	        rMatrix[i][j] = float(0)
	    else:
	        continue

for each in movie_dict:
    print(movie_dict[each])
    
for i in range(1):
    rcmd = [b[0]+1 for b in sorted(enumerate(rMatrix[i]),key=lambda i:i[1])]
    for i, each in enumerate(rcmd):
        if i>10:
            break
        print(movie_dict[each])



