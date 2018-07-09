_data_r  = open("./data/ml-latest-small/ratings.csv", "r");
_data_m  = open("./data/ml-latest-small/movies.csv", "r");

entries_m = _data_m.readlines();

number_of_films = 1000#int(entries_m[-1].split(",")[0])

entries = _data_r.readlines();

ratings = []
skip = 1

number_of_users = 50 #int(entries[-1].split(",")[0])

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

number_of_users = 3
number_of_films = 3

rMatrix = [
	[5,3,2],
	[3,4,"null"],
	["null", 2,5]
]

my_dict = {}


for i in range(0, number_of_users):
	for j in range(0,number_of_films):
		for k in range(j+1, number_of_films):
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

for each in my_dict:
	print each, my_dict[each]

for i in range(0, number_of_users):
	for j in range(0,number_of_films):
#		print("Checking")
		if rMatrix[i][j]=="null":
			idx = j
			aggr_r = 0
			total = 0
			found = 0

			for each in my_dict:
				if each[0]==idx or each[1]==idx:
					found=1
					if each[0]==idx:
						aggr_r = aggr_r+\
									((float(0) if rMatrix[i][each[1]] else float(rMatrix[i][each[0]])) + \
									float(my_dict[each][0]))*my_dict[each][1]
						total = total+my_dict[each][1]
						aggr_r = aggr_r//total
					else:
						aggr_r = aggr_r+\
								((float(0) if rMatrix[i][each[0]]=="null" else float(rMatrix[i][each[0]])) - \
								float(my_dict[each][0]))*my_dict[each][0]
						total = my_dict[each][1]
			if found:
				rMatrix[i][j] = aggr_r//total
		else:
			continue

for i in rMatrix:
	print i










