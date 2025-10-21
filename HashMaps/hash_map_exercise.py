'''
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

'''

import string


temp = []
weather_data = {}

with open('HashMaps/nyc_weather.csv', 'r') as weather:
    for id, line in enumerate(weather):
        if id == 0 :
            continue
        op = line.split(',')
        weather_data[op[0]]=int(op[1])
        temp.append(int(op[1]))


print(temp)
print(f'Average temp in first week of Jan: {sum(temp[:7])/len(temp[0:7])}')
print(max(temp[0:10]))

'''
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?

'''
print(f'temp on Jan 9: {weather_data['Jan 9']}')
print(f'temp on Jan 4: {weather_data['Jan 4']}')


'''
poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in python and print every word and its count as show below. 
Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

'diverged': 2,
'in': 3,
'I': 8

'''
word_count = {}
translator = str.maketrans('', '', string.punctuation)

with open('HashMaps/poem.txt','r') as poems:
    for poem in poems:
        poem = poem.strip()
        op = poem.split(' ')
        # print(f'op: {op}')
        for word in op:
            word = word.translate(translator)
            if word not in word_count:
                word_count[word] = 1

            elif (word and word_count[word]):
                word_count[word]+=1
            
print(word_count)    