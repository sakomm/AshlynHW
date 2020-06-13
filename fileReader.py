output = []
file = open('test.txt')
fileReader = file.read()
fileReader = fileReader.strip().split()
# at this point all the words in the file are split based open an empty space char 
# aka spacebar and any unessecary space crap is gone


#print(fileReader) test 
keyWords = ["poop"]
# append values to compare

for words in fileReader:
    for key in keyWords:
        if words == key:
            output.append(words)

print (output)

