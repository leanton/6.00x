def sort1(lst):
    swapFlag = True
    iteration = 0
    n=0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                temp = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = temp
                swapFlag = True
        n+=1
        # the questions below refer to this point, assuming we set L = lst[:] here
        
        print 'Iteration', iteration
        print lst
        iteration += 1
    print n
    
    return lst

def sort2(lst):
    itr = 0
    n=0
    print 'Unsorted: ', lst
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
            n+=1
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp
        # the questions below refer to this point, assuming we set L = lst[:] here
        print "Iteration", itr
        print lst
        itr +=1
    print 'N', n
    return lst

def sort3(lst):
    itr = 0
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)
        # the questions below refer to this point, assuming we set L = out[:] here
        print "Iteration", itr
        print out
        itr +=1
    return out

def sort4(lst):
    itr = 0
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])
        # the questions below refer to this point, assuming we set L = lst[:] here
        print "Iteration", itr
        print front, back
        itr +=1

        return unite(front, back)

li = [6, 0, 50, 2, 1]
sort4(li)