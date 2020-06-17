Lines = []

file = input('Enter the name of the file:')
search = input('Enter the search term: ')
#search1 = str(search)

#print('Alice' == 'alice')

FileHandler = open(file)
FileOut = open('Output.txt','w')
Lines = FileHandler.readline()
count = 1
while Lines:
    if search.lower() in Lines.lower():
        FileOut.write(("{} : {} \n".format(count, Lines.strip())))

    Lines = FileHandler.readline()
    count += 1
#Lines.strip()
#print(Lines)

'''

    for i in f:
        lines.append(i,rstrip('\n'))
        
for index, i in enumerate(lines):
    if search.lower() in i.lower():
        newlines.append(f'{index+1}: {i}')

        print(index+1, i)

with open('output.txt', 'w') as f:
    for i in newlines:
        f.write(i+'\n')
'''