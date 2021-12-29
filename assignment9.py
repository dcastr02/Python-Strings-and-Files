################################
#      Diego Castro            # 
#       010873014              #
#        4/19/21               #
################################
import sys
import operator

n = len(sys.argv)
erasures = ['\n','\t','.','?','!',',',';',':','\'','\"']

#error checking for cl args
if n != 3:
    print("Please input only 2 arguments (story text file & skip-words text file).")
    exit()
else:
    storyFileName = sys.argv[1]
    skipFileName = sys.argv[2]

#open and store files into strings
with open(storyFileName, 'r') as storyFile:
    read_data = storyFile.read()

with open(skipFileName, 'r') as skipFile:
    skip_data = skipFile.read()

#lower case both
read_data = read_data.lower()
skip_data = skip_data.lower()

#format skip data
skip_data = skip_data.replace(',', ' ')
skip_data = skip_data.split()

#format read data
for x in erasures:
    read_data = read_data.replace(x, ' ')

#split the string into a list
read_data = read_data.split()
#remove last weird character
read_data.pop()

removed = []
#loop through each word, if its not found in the skip list append to new list
for x in read_data:
   if x not in skip_data:
       removed.append(x)


wordPairs = {}

#loop through removed array and add word pairs to dictionary
#if the wordpair already exists increment the value (count) plus 1
#if this is not the case, then the dictionary key does not exist and one is created
#with the initial value of 1
for x in range(len(removed) - 1):
    if removed[x] + ' ' + removed[x + 1] in wordPairs:
        wordPairs[removed[x] + ' ' + removed[x + 1]] += 1
    else:
        wordPairs[removed[x] + ' ' + removed[x + 1]] = 1

#sort wordPairs by the second item in the dictionary
#the second item is the count of times the word pair appears
var = sorted(wordPairs.items(), key=operator.itemgetter(1))


#Display information
print("Story file name: ", storyFileName)
print("Skip word file name: ", skipFileName)
print("Skip words: ", skip_data)
print("The five most frequently occuring word pairs are: ")
#since it is sorting them from lowest to greatest appearance, the range should be from -1 -> -6 to get the last 5 elements in the dictionary
#display last 5 elements in dictionary (the top 5 most occuring word pairs)
for x in range(-1, -6, -1):
    print(var[x])