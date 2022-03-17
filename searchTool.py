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
    def __init__(self, l_num ,s_num, f_id, hw_v, sw_v, p_187, p_191):
        """
        :param l_num: local num
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





def printLines(file_name: str, method: str):
    # f = open(file_name,method).readlines()
    with open(file_name, method) as f:
        data = f.readlines()
    for line in data:
        data = ('','','','','','','')
        l_num, s_num, f_id, hw_v, sw_v, p_187, p_191 = data
        # Get the local num from 1 to 200
        l_num = line[:line.index('/')]
        # former = line[:line.rindex(':') + 2]
        # Get the key
        key = re.search('6[0-9]{4}', line).group()
        latter = line[line.rindex(':') + 2:]
        latter_list = latter.split()
        for index in range(len(latter_list)):
            if isHex(latter_list[index]) == True:
                latter_list[index] = hexStr_to_str(latter_list[index])
        latter = "".join(latter_list)
        print(latter)
        # for element in list:
            # if isHex(element) == True
        a = line.strip()[-8:].replace(" ", "")
        print(hexStr_to_str(a))
        # # print "Show the data as below\n", data
        # print("The type of f is:", type(data))
        # for i in range(startPoint, len(data)):
        #     if search in data[i]:
        #         print('The target line is', i + 1)
        #         return i + 1
        #         break
        # else:
        #     return "Not found!"


if __name__ == '__main__':
    printLines("part1.txt", "r")
    # printLines("part2.txt", "r")
    # print(hexStr_to_str("31"))
    # a = "4x"
    # print(isHex(a))
    # list = ['12342','adf','232']
    # for i in range(len(list)):
    #     list[i] = 'XXXX'
    # print(list)
