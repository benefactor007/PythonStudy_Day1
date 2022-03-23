# rec_bisection_squareRoot

def rec_bisection_squareRoot(x, epsilon, low=None, high=None):
    if low == None:
        low = 0.0
    if high == None:
        high = x
    midPoint = (low + high) / 2
    if abs(midPoint ** 2 - x) < epsilon or midPoint > x:
        return midPoint
    else:
        if abs(midPoint ** 2) < x:  # it's too small, should find the target from midPoint to high
            print "Step1, the current midPoint is", midPoint
            return rec_bisection_squareRoot(x, epsilon, midPoint, high)
        elif abs(midPoint ** 2) > x:  # it's too big, should find the target from low to midPoint
            print "Step2, the current midPoint is", midPoint
            return rec_bisection_squareRoot(x, epsilon, low, midPoint)


def testCase_rec_bisection_squareRoot():
    print "test the Square root of 25 should be expected as 5, the func. calls %f" % (
        rec_bisection_squareRoot(25, 0.01))


def binarySearch(L, e, low=None, high=None):  # arguments as follows, List, element, low's index, high's index)
    global numCalls  # global variable should define before we call the func. binarySearch
    numCalls += 1  # record how many times it counts
    if low == None:
        low = 0
    if high == None:
        high = len(L) - 1  # because array index as starting from 0 to len(L) - 1

    if high - low < 2:
        return L[high] == e or L[low] == e

    # mid = low + int((high - low) / 2)
    mid = (low + high) // 2

    if L[mid] == e:  # L[mid] meas the position of mid value, not mid value itself.
        return True
    if L[mid] > e:
        return binarySearch(L, e, low, mid - 1)
    else:
        return binarySearch(L, e, mid + 1, high)


def testCase_binarySearch():
    List = [1, 2, 3, 4, 12, 24, 34, 45, 56, 67, 89, 90, 123, 234, 345, 456, 567, 678, 789, 1234, 234234, 534532,
            99999999999]
    # numberCalls = 0
    # global numCalls
    global numCalls
    print "The element, 1234 ,is in the List, the func. checks the result is", binarySearch(List, 1234)
    print "The total numberCalls is", numCalls
    numCalls = 0
    print "The element, 34 ,is in the List, the func. checks the result is", binarySearch(List, 888)
    print "The total numberCalls is", numCalls


def merge(left, right, lt):
    """Assume left and right are sorted lists,
    It defines an ordering on the elements of the lists.
    Returns a new sorted(by lt) list containing the same elements
    as (left + right) would contain.
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):               # Left[i] < right[j]
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def sort(L, lt=lambda x, y: x < y):
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]  # copy not aliasing
    else:
        # middle = int(len(L)/2)
        middle = len(L) // 2
        left = sort(L[:middle],lt)
        right = sort(L[middle:],lt)
        print 'About to merge', left, 'and', right
        return merge(left,right,lt)

def binary_search(L, e, low, high):
    if high >= low:
        mid = (high + low) // 2
        print L[mid]
        if L[mid] == e:
            return mid
        elif L[mid] > e:
            return binary_search(L,e,low,mid-1)
        else:
            return binary_search(L,e,mid+1,high)
    else:
        return -1


def main():
    # global numberCalls
    print binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 4)
    print numCalls
    # testCase_binarySearch()
    unsortedList = [5,6,2,34,5,62,424,432,6]
    print sort(unsortedList)



if __name__ == '__main__':
    numCalls = 0
    main()
    numCalls = 0
    testCase_binarySearch()
    L1 = [1,23,45,356,34534,5464645]
    print binary_search(L1,88,0,len(L1)-1)
    print binary_search(L1,34534,0,len(L1)-1)

