# coding=utf-8
from searchTool import HU
import glob

if __name__ == '__main__':
    import shelve

    with shelve.open('gpdb') as db:
        print(len(db))
        print(list(db.keys()))
        for key in db:
            # print(key, '\t=>\t', db[key])
            print('%-3s=>%s' % (key, db[key]))
