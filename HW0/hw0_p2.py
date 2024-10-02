#read the file 
file_name = "IMDB-Movie-Data.csv"
myfile = open(file_name,"r")
headers = next(myfile) #skip the title 

data = []
for row in myfile:
    # 去除行尾的換行符號，然後以逗號分隔
    values = row.strip('\n').split(',')
    data.append(values)

#change the sort by tuple
def change(diction):
	compare_list = [] 
	for key, value in diction.items():
		a = (value,key)
		compare_list.append(a)
	compare_list.sort(reverse = True) #從大到小排順序
	return compare_list

#Q1 3 highest rating movies
dict = {}
for i in data:
    if i[5]=='2016': #2016year
        dict[i[1]] = float(i[7])
compare_list = change(dict)
print("A1:", compare_list[0][1],',', compare_list[1][1],',',compare_list[2][1]) #top 3 high-rate

#Q2 the highest average revenue
answer = {}
for i in range(len(data)): #分別將評分和演員明分別取出
	actor = data[i][4].split("|") #分隔線後還有一格，這樣才能取出完整的名稱
	for j in range(len(actor)):
		actor[j] = actor[j].strip()

	if data[i][9] != '':  
		revenue = float(data[i][9])  
		
	for j in actor:
		if answer.get(j) is None and revenue:
			answer[j] = [revenue] #如果還沒有被收進answer裡，就創一個
		elif revenue:		
			answer[j] += [revenue] #如果有了，就加上去

for i in answer:
	answer[i] = sum(answer[i])/len(answer[i])

compare_list = change(answer)
print('A2:',compare_list[0][1])

#Q3 average rating of Emma Watson’s movies
answer = {}
for i in range(len(data)): #分別將評分和演員明分別取出
	actor = data[i][4].split("|") #分隔線後還有一格，這樣才能取出完整的名稱
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	rating = float(data[i][7])
	for j in actor:
		if answer.get(j) is None:
			answer[j] = [rating] #如果還沒有被收進answer裡，就創一個
		else:		
			answer[j] += [rating] #如果有了，就加上去
average_raing_of_Emma = sum(answer["Emma Watson"])/len(answer["Emma Watson"])
print("the answer of Q3:", average_raing_of_Emma)

#Q4 Top-3 directors 
collab={}
for i in range(len(data)): #分別將演員和電影明分別取出
	director = data[i][3]
	actor = data[i][4].split("|")
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	for j in actor:
		if collab.get(director) is None:
			collab[director] = [j] #如果還沒有被收進collab裡，就創一個
		else:		
			collab[director] += [j]#如果有了，就加上去 
for key ,value in collab.items(): #和導演合作的演員有可能重複，但題目要的是與不同演員合作的次數，所以重複的不能計算
	tempt = collab[key] 
	tempt.sort()
	i = 0
	while True:
		count = 1
		while i+1 <len(tempt):
			if tempt[i] != tempt[i+1]: #如果前一個和下一個相同，就代表名子重複
				count +=1
			i +=1
		collab[key] =count #次數可能相同會覆蓋掉其他導演，但導演名稱不會重複
		break
compare_list = change(collab)
top3collab = []
for i in range(4):#第三名與第四名同分
	top3collab += [compare_list[i][1]]
print("the answer of Q4:", ", ".join(top3collab))

#Q5 Top-2 actors playing in the most genres of movies
pairs={}
for i in range(len(data)): #分別將類型和演員分別取出
	genre = data[i][2].split("|")
	for j in range(len(genre)):
		genre[j] = genre[j].strip()
	actor = data[i][4].split("|")
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	for j in actor:
		for k in genre:
			if pairs.get(j) is None:
				pairs[j] = [k]
			else:		
				pairs[j] += [k]
for key ,value in pairs.items():#類型可能會重複，但題目要的是不同類型的次數
	tempt = pairs[key]
	tempt.sort()
	i = 0
	while True:
		count = 1
		while i+1 <len(tempt):
			if tempt[i] != tempt[i+1]: #如果前一個和下一個相同，就代表名子重複
				count +=1
			i +=1
		pairs[key] =count #次數可能相同會覆蓋掉其他導演，但導演名稱不會重複
		break
compare_list = change(pairs)
top6actors = []
for i in range(6): #第二名至第六名同分
	top6actors += [compare_list[i][1]]
print("the answer of Q5:", ", ".join(top6actors))

#Q6 MAX GAP YEAR actors
pairs={}
for i in range(len(data)): #分別將年分和電影明分別取出
	year = int(data[i][5])
	actor = data[i][4].split("|")
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	for j in actor:
		if pairs.get(j) is None:
			pairs[j] = [year]
		else:		
			pairs[j] += [year]
for key ,value in pairs.items():
	tempt = pairs[key]
	tempt.sort()
	gap = tempt[len(tempt)-1] - tempt [0]
	pairs[key] =gap
compare_list = change(pairs)
ans9 = []
for i in range(len(compare_list)):
	if compare_list[i][0] == 10:
		ans9.append(compare_list[i][1])
print("the answer of Q6:",", ".join(ans9))

#Q7 
johnny = []
for i in range(len(data)): #分別將評分和演員明分別取出
	actor = data[i][4].split("|") #分隔線後還有一格，這樣才能取出完整的名稱
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	
	if 'Johnny Depp' in actor:
		for i in actor:
			if i == 'Johnny Depp' or i in johnny:
				pass
			else:
				johnny.append(i)

for i in range(len(data)): #分別將評分和演員明分別取出
	actor = data[i][4].split("|") #分隔線後還有一格，這樣才能取出完整的名稱
	for j in range(len(actor)):
		actor[j] = actor[j].strip()
	
	for k in johnny:
		if k in actor:
			if k == 'Johnny Depp' or k in johnny:
				pass
			else:
				johnny.append(i)

print('A7:',johnny)