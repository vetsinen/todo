def filterByChar(line: str):
    line = line.lower()
    dividers = (',', ',', ':', '/', '\\')
    for c in dividers:
        line = line.replace(c, ' ')

    stopList = ('\n', "'", '.', "?")
    for c in stopList:
        line = line.replace(c, '')
    return line

def getFrequencyDict(lines: list):
    line: str
    word: str
    frequencyDict: dict = {}
    stopWords = {'to','on','in','and','for','how','by','what','improve','try','etc','as','of','or'}

    for line in lines:
        words = line.split()
        for word in words:
            if word not in stopWords:
                if word not in frequencyDict.keys():
                    frequencyDict[word] = 1
                else:
                    frequencyDict[word] += 1

    frequencyDict = {k: v for k, v in sorted(frequencyDict.items(), reverse=True, key=lambda item: item[1])}
    return frequencyDict


file = open('todo.txt', 'r')
c: int = 0
taskList: list = []
for line in file:
    line = filterByChar(line)
    taskList.append(line)
    c = c + 1
print(c)
file.close()
print(getFrequencyDict(taskList))
