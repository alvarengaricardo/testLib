'''
esta lib tenta escrever arquivos de log
'''

def testAssert(ff, a, b, expected):
    received = ff(a, b)
    line = str(ff.__name__) + ' ' + str(a) + ' ' + str(b) + ' ' + str(expected) + ' ' + str(received)
    list1(line)
    if received == expected:
        line = line + ' Pass'
        list2(line)
        print(line)
    else:
        line = line + ' Fail'
        list3(line)
        print(line)

def init(file):
    global testList, testPass, testFail, filetot, filepass, filefail, ft, fp, ff
    global resultPass, resultFail
    testList = []
    testPass = []
    testFail = []
    filetot = file
    filepass = 'PASS_' + file
    filefail = 'FAIL_' + file
    ft = open(filetot, 'w')
    fp = open(filepass, 'w')
    ff = open(filefail, 'w')
 #   resultPass = []
 #   resultFail = []

def end():
    for i in testList:
        ft.write(testList[i], '\n')
        ft.write(f'{len(testList)} tests executed.')
        for o in testPass:
            fp.write(testPass[o], '\n')
        fp.write(f'{len(testPass)} tests passed.')
        for f in testFail:
            fp.write(testFail[f], '\n')
        fp.write(f'{len(testFail)}')
        ft.close()
        fp.close()
        ff.close()
        print('Finished.')

    # 1 -> faz append na lista total
    # 2 -> faz append na lista pass
    # 3 -> faz append na lista fail
    # 4 -> encerra as variáveis, gravando nos respectivos arquivos, fechando arquivos de logs

def list1(arg):
    nonlocal testList
    testList.append(arg)
        #increaseList(arg)

def list2(arg):
    testPass.append(arg)

def list3(arg):
    testFail.append(arg)

def record(command, arg):
    global testList, testPass, testFail, filetot, filepass, filefail, ft, fp, ff
    global resultPass, resultFail

    def start():
        nonlocal testList, testPass, testFail, filetot, filepass, filefail, ft, fp, ff, resultPass, resultFail
        testList = []
        testPass = []
        testFail = []
        filetot = arg
        filepass = 'PASS_' + arg
        filefail = 'FAIL_' + arg
        ft = open(filetot, 'w')
        fp = open(filepass, 'w')
        ff = open(filefail, 'w')
        resultPass = []
        resultFail = []

    if command == 0:
        start()
    elif command == 1:
        nonlocal testList
        testList.append(arg)
    elif command == 2:
        nonlocal testPass
        testPass.append(arg)
    elif command == 3:
        nonlocal testFail
        testFail.append(arg)

def testEqual(a, b):
    line = testLibAux.line(a, b)
    if a == b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)


def testFunc(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = testLibAux.line2(ff, a, b, expected, received)
    if received == expected:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)

def testNotFunc(ff, a, b, expected):
    if b != '':
        received = ff(a, b)
    else:
        received = ff(a)
    line = testLibAux.line2(ff, a, b, expected, received)
    if received != expected:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)



def testNotEqual(a, b):
    line = testLibAux.line(a, b)
    if a != b:
        line = line + 'Pass'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        fp = open('filepass.txt', 'a')
        fp.write(line + '\n')
        print(line)
    else:
        line = line + 'Fail'
        ft = open('filetot.txt', 'a')
        ft.write(line + '\n')
        ff = open('filefail.txt', 'a')
        ff.write(line + '\n')
        print(line)