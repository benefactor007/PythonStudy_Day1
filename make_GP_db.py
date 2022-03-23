if __name__ == '__main__':
    import shelve
    db = shelve.open('gp_db')
    print(len(db))
    print(list(db.keys()))
    print(db['VWX9GA0241359'])
    # for key in db:
    #     print(key, '=>', db[key])
    import glob