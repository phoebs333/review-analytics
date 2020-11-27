data = []
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('Files finished reading, we have total', len(data),'reviews')

print(data[0])


sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('The average number of the reviews', sum_len/len(data)) 

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('We have total', len(new),'reviews less than 100 words!')
print(new[0])
print('-----------------')
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('We have', len(good), 'reviews mentioned about good')

#word count 
wc = {} #word_cuont
for d in data:
    words = d.split()
    for word in words: 
        if word in wc:
            wc[word] += 1 
        else:
            wc[word] = 1 #Adding new key into dictionary 

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))

while True:
    word = input('What word you would like to look up: ')
    if word == 'q':
        break
    if word in wc: 
        print(word, 'has shown up', wc[word], 'times!')
    else:
        print('Sorry! I have not seen this word in these reviews')
print('Thanks for using this function :)')
