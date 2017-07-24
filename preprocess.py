import csv

TEST_p = 0.2  #percent
TRAIN_p = 0.8  #percent

data = list(csv.reader(open("data.csv")))

data_p = 0
data_n = 0


for x in range(len(data)):
	for y in range(len(data[x])):
		if y == len(data[x])-1:
			if(data[x][y] == 'positive'):
				data[x][y] = 1
				data_p = data_p + 1
			elif(data[x][y] == 'negative'):
				data[x][y] = 0
				data_n = data_n + 1
		else:
			data[x][y] = ord(data[x][y])

data_posetives = data[0:data_p-1] 
data_negatives = data[data_p : data_p+data_n-1]

PER_p = int(len(data_posetives)*TEST_p)
PER_n = int(len(data_negatives)*TEST_p)

data_posetives_train = data_posetives[0:len(data_posetives)- PER_p]
data_posetives_test = data_posetives[len(data_posetives)-(PER_p) : len(data_posetives)]

data_neg_train = data_negatives[0:len(data_negatives)-PER_n]
data_neg_test = data_negatives[len(data_negatives)-PER_n : len(data_negatives)]

writer = csv.writer(open("train.csv", 'w'))
writer.writerows(data_posetives_train)
writer.writerows(data_neg_train)


writer2 = csv.writer(open("test.csv", 'w'))
writer2.writerows(data_posetives_test)
writer2.writerows(data_neg_test)
