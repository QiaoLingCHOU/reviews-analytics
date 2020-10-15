data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('總用有',len(data), '筆留言')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總用有', len(new), '筆留言的字數小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print(good[0])
