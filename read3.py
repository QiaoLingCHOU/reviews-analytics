data = []
count = 0
with open('reviews.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了!, 總共有', len(data), '筆資料')

wc = {} #words_count
for d in data:
    words = d.split() #split本來功能就是用來去掉空白鍵,不管多少空白鍵都會去掉
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #add new key into the dictionary
for word in wc:
    if wc[word] > 1000:
        print(word, wc[word])

while True:
    word = input('Plese enter the word you would like to search:')
    if word == 'q':
        break
    if word in wc:
        print('The', word, 'appeared:', wc[word], 'times.')
    else:
        print('The word you search does not exit in the comment.')
print('Thank you for using the searching device.')
