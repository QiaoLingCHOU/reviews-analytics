data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
sum_len = 0
for d in data:
	sum_len += len(d)
print('The average of the reviews is', sum_len/len(data))
new = []
for d in data: 
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'reviews less than 100 words.')
good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
good = [d for d in data if 'good' in d] #list comprehension (清單快寫法)
print('There are', len(good), 'reviews mentioned of good.')
print('The first review mentioned the world "good" :',good[0])
bad = ['bad'in d for d in data] #bad清單裡會有一萬筆的 True or flase
print(bad)
print(len(bad))