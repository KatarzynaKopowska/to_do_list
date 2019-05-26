toDoList = []

def doList():
    if toDoList != []:
        print('Tasks to do: ')
        for task in range(len(toDoList)):
            if task == 0:
                print(' - ' + str((task) + 1) + ('st') + '. '  + toDoList[task])
            elif task == 1:
                print(' - ' + str((task) + 1) + ('nd') + '. '  + toDoList[task])
            elif task == 2:
                print(' - ' + str((task) + 1) + ('rd') + '. '  + toDoList[task])
            elif task >= 3:
                print(' - ' + str((task) + 1) + ('th') + '. '  + toDoList[task])
    else:
        print('Congratulations, you have done everything. Now you can grab some snacks and play video games all day long.')
suffixes = ['st', 'nd', 'rd']

while True:
    suffix = len(toDoList) < 3 and suffixes[len(toDoList)] or 'th'
    print('Enter ' + str(len(toDoList) + 1) + suffix + ' task you have to do today (leave empty place if list is done).')

    task = input()
    if task == '':
        break
    toDoList = toDoList + [task]

doList()
while toDoList != []:
    done = input('What have you done already? ' )
    if done in toDoList:
        toDoList.remove(done)
        doList()
        
    elif done not in toDoList:
        print(str(done) + ' is not on your list.')
        doList()
        continue
