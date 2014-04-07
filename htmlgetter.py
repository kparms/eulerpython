import re
from urllib.request import urlopen


url = "http://www.recommind.com/"
page = urlopen(url).read()

clean = re.sub('<[^<]+?>', '', str(page))
clean = clean.replace('&nbsp', '')
clean = clean.replace('\r', '')

every_word = []
for x in clean.strip().split(' '):
    x = x.rstrip('\r\n')
    if len(x) > 5:
        every_word.append(x)

word_list = {}

for word in every_word:
    if word.lower() not in word_list.keys():
        word_list[word.lower()] = 1
    else:
        word_list[word.lower()] += 1


for word in word_list:
    if word_list[word] > 2:
        print(word + ' ' + str(word_list[word]))
