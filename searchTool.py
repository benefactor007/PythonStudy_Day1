import binascii
import re


def hexStr_to_str(hex_info):
    return binascii.unhexlify(hex_info.encode('utf-8')).decode('utf-8', 'ignore')


def isHex(str):
    if len(str) == 2:
        if re.match('[0-9a-fA-f]', str) is not None:
            return True
    else:
        return False


class AttrDisplay:
    """
    Provides an inheritable(inˈherədəb(ə)l) display overload method that shows instance with their class
    names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its
    class). Can be mixed into any class, and will work on any instance
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


class HU(AttrDisplay):
    def __init__(self,l_num, s_num, f_id, hw_v, sw_v, p_187, p_191):
        # def __init__(self,s_num, f_id, hw_v, sw_v, p_187, p_191):
        """
        # :param l_num: local num
        :param s_num: serial num
        :param f_id: fazit id
        :param hw_v: hardware version
        :param sw_v: software version
        :param p_187: partnum F187
        :param p_191: partnum F191
        """
        self.l_num = l_num
        self.s_num = s_num
        self.f_id = f_id
        self.hw_v = hw_v
        self.sw_v = sw_v
        self.p_187 = p_187
        self.p_191 = p_191


"""
9/periscope.log.20:123:load: ns: 3000000 key: 61836 slot: 0 status: 0 data: 56 57 58 39 47 41 30 32 34 31 33 35 39 20 20 20 20 20 20 20 
9/periscope.log.20-124-load: ns: 3000000 key: 61820 slot: 0 status: 0 data: 58 39 47 2d 31 30 32 31 36 2e 30 33 2e 32 32 39 30 30 31 30 32 30 34 
9/periscope.log.20-125-load: ns: 3000000 key: 61859 slot: 0 status: 0 data: 48 31 34 
9/periscope.log.20-126-load: ns: 3000000 key: 61833 slot: 0 status: 0 data: 30 34 32 31 
9/periscope.log.20-127-load: ns: 3000000 key: 61831 slot: 0 status: 0 data: 33 47 42 30 33 35 38 36 36 41 20 
9/periscope.log.20-128-load: ns: 3000000 key: 61841 slot: 0 status: 0 data: 33 47 42 30 33 35 38 36 36 41 20 
"""

# def raw_data_filter(str):
#     L = [0,0,0,0,0,0]
#     key = re.search('6[0-9]{4}', str).group()
#     if key == 61836:
#         L[]

# l_num ,s_num, f_id, hw_v, sw_v, p_187, p_191

# keyDict = {61836: "s_num", 61820:"f_id", 61859: "hw_v", 61833: "sw_v", 61831: "p_187",
#            61841: "p_191"}
keyDict = {'61836': "s_num", '61820': "f_id", '61859': "hw_v", '61833': "sw_v", '61831': "p_187",
           '61841': "p_191"}

GP_dict = {}

def get_info_from_rawData(str, l_num=None):
    if l_num == '':
        l_num = str[:str.index("/")]
        print("ID:", l_num)
        keyDict['id'] = l_num
    else:
        assert str[:str.index("/")] == l_num
    key = re.search('6[0-9]{4}', str)
    if key is not None:
        key = key.group()
        if key in keyDict.keys():
            print(keyDict[key])
            keyDict[key] = hexStr_to_str(str[str.rindex(':') + 2:].replace(" ", '')).strip()
            print(keyDict[key])
            # print(keyDict)
            print("current l_num is", l_num)
        return l_num
    else:
        print("Key:", key, "\nCan not search key info in this line!!!")
        return l_num


def printLines(file_name: str, method: str):
    # f = open(file_name,method).readlines()
    with open(file_name, method) as f:
        data = f.readlines()
    temp_store_list = []
    global GP_dict
    l_num = ''
    for line in data:
        if line.startswith("--") is not True:
            l_num = get_info_from_rawData(line.strip(), l_num)
        else:
            print("Done! Finished")
            print(keyDict)
            """
                    # :param l_num: local num
                    :param s_num: serial num
                    :param f_id: fazit id
                    :param hw_v: hardware version
                    :param sw_v: software version
                    :param p_187: partnum F187
                    :param p_191: partnum F191
                    """
            # machine_id = "hu" + "_" + l_num
            # GP_dict[machine_id] = HU(keyDict['61836'], keyDict['61820'], keyDict['61859'],
            #                          keyDict['61833'], keyDict['61831'], keyDict['61841'], l_num=l_num)
            temp_store_list.append(l_num)
            l_num = HU(l_num, keyDict['61836'], keyDict['61820'], keyDict['61859'],
                                     keyDict['61833'], keyDict['61831'], keyDict['61841'])
            l_num = ''
            # print(GP_dict[machine_id])
            # temp_store_list.append(line.strip())
    return temp_store_list


if __name__ == '__main__':
    list = printLines("raw_data_1.txt", "r")
    print(list)

    # import shelve
    # db = shelve.open('gp_db')
    # for obj in list:
    #     db[obj.s_num] = obj
    # db.close()

