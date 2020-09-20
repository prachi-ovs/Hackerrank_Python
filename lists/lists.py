def insertFunction(l,i):    # l is the list and  i is the index of operation
    l.insert(int(instr[i][0]),int(instr[i][1]))
    return l

def printFunction(l):
    print(l)
    return l

def removeFunction(l,elm):
    l.remove(elm)
    return l

def appendFunction(l,elm):
    l.append(elm)
    return l

def sortFunction(l):
    l.sort()
    return l

def popFunction(l):
    l.pop()
    return l

def reverseFunction(l):
    l.reverse()
    return l

if __name__ == '__main__':
    initial_list= []
    instr=[]
    operations = []
    N = int(input())
    for _ in range(N):
        operation, *line = input().split()  # * operator next to line indicates unassigned/mulitple number of variables to store the split values in
        operations.append(operation)
        instr_for_operation=  list(line)
        instr.append(instr_for_operation)
    print(operations)
    print(instr)
    #print(int(instr[1][0]))
    for pos,op in enumerate(operations):
        if op == 'insert':
            insertFunction(initial_list, pos)
        elif op == 'print':
            printFunction(initial_list)
        elif op == 'remove':
            removeFunction(initial_list, int(instr[pos][0]))
    #print(initial_list)
        elif op == 'append':
            appendFunction(initial_list, int(instr[pos][0]))
        elif op == "sort":
            sortFunction(initial_list)
        elif op == "pop":
            popFunction(initial_list)
        else:
            reverseFunction(initial_list)





