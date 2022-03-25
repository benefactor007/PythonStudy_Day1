#!/usr/bin/env python3.5
# coding=utf-8

import shelve

from searchTool import HU
import glob

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
        # print('About to merge', left, 'and', right)
        return merge(left,right,lt)


def read_shelve_db(filename):
    with shelve.open(filename) as db:
        print(len(db))
        print(sort(list(db.keys())))
        for key in db:
            # print(key, '\t=>\t', db[key])
            print('%-3s=>%s' % (key, db[key]))

def greenFont(str):
    return "\033[32m" + str + "\033[0m"

def redFont(str):
    return "\033[31m" + str + "\033[0m"


def check_duplicate(filename):
    with shelve.open(filename) as db:
        print(len(db))
        print(sort(list(db.keys())))
        tempList = []
        for key in db:
            # print(key, '\t=>\t', db[key])
            assert db[key].hw_v == "H14"
            print('%-3s=>%s' % (key, db[key]))
            tempList.append(db[key].f_id)
            # print(db[key].f_id)
        # print(tempList)
        # -----------------Test--------------------
        # tempList.append('X9G-10222.03.2290011635')
        # print(tempList[2])
        # tempList[2] = 'X9G-10222.03.2290011635'
        # print(tempList[2])
        # -----------------Test--------------------
        tmpDic = {}.fromkeys(tempList)
        if len(tmpDic) == len(tempList):
            print(greenFont("It's fine! Everything is unique."))
            return len(db)
        else:
            print(redFont("There is a duplicate item, Please check it!"))
            return False

if __name__ == '__main__':

    import shelve
    db_list = ['H14_1_to_100','H14_101_to_200',"H14_201_to_250","H14_251_to_300","H14_351_to_400","H14_301_to_350",]
    db_list_0324 = ['H14_401_to_450','H14_451_to_500','H14_601_to_650']
    db_list_0324_chaoyuan = ['H14_501_to_600','H14_651_to_750']
    db_list_0325 = ['H14_751_to_800']
    sum = 0
    for i in (db_list + db_list_0324 + db_list_0324_chaoyuan + db_list_0325):
        # read_shelve_db(i)
        sum += check_duplicate(i)
    print("The total qty of HU is", str(sum))
    #
    # check_duplicate("H14_351_to_400")
    #
    # read_shelve_db("H14_351_to_400")
    # read_shelve_db("H14_301_to_350")
    # read_shelve_db("H14_251_to_300")
    # read_shelve_db("H14_201_to_250")


    # print(glob.glob('gpdb*'))
    # print(open('gpdb.dir').read())