# coding=utf-8
import binascii
import fileinput
import string


def str_to_hexStr(str_info):
    return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')


def hexStr_to_str(hex_info):
    return binascii.unhexlify(hex_info.encode('utf-8')).decode('utf-8', 'ignore')


# replace主要用于字符串的替换replace(old, new, count)
# str.replace(" ","")
# join为字符字符串合成传入一个字符串列表，split用于字符串分割可以按规则进行分割
#  a = " a b c "
#  "".join(a.split())

def remove_blank(original: str) -> str:
    return "".join(original.split())


def main():
    3  # 5HG035866     #HH08S0342#*009X9G-10109.04.2199990011*=VWX9GY0148242

    # print(str_to_hexStr("X9G-10109.04.2199990011"))
    # hex_fazit = "0x" + str_to_hexStr("X9G-10109.04.2199990011")
    # print(hex_fazit)
    fazit1 = "58 39 47 2d 31 30 32 30 34 2e 31 32 2e 32 31 39 30 30 31 30 35 35 30"
    print(remove_blank(fazit1))
    print(hexStr_to_str(remove_blank(fazit1)))
    raw_data = "/home/jpcc/Desktop/PeriscopeRecord/122720210005/periscope.log.20:215:load: ns: 3000000 key: 61820 " \
               "slot: 0 status: 0 data: 58 39 47 2d 31 30 32 30 34 2e 31 32 2e 32 31 39 30 30 31 30 35 "
    # raw_data ="/home/jpcc/Desktop/PeriscopeRecord/122720210005/periscope.log.20-222-store: ns: 80000008 key: 0 slot: 0 status: 0 data: e5 "
    print(raw_data.rindex(":"))  # return: 120
    # get hex fazit id after the last colon.
    print(raw_data[(raw_data.rindex(":") + 1):])
    print(hexStr_to_str(remove_blank(raw_data[(raw_data.rindex(":") + 1):])))
    dec_data = hexStr_to_str(remove_blank(raw_data[(raw_data.rindex(":") + 1):]))
    print(raw_data[:(raw_data.rindex(":") + 2)] + dec_data)
    print(hexStr_to_str(remove_blank("e5")))


# /home/jpcc/Desktop/PeriscopeRecord/122720210005/periscope.log.20:215:load: ns: 3000000 key: 61820 slot: 0 status: 0
# data: 58 39 47 2d 31 30 32 30 34 2e 31 32 2e 32 31 39 30 30 31 30 35

def main2():
    # os.system("grep -R \"61836\" -A 13 -nsr ~/Desktop/PeriscopeRecord |tee -a originalFile.txt")
    # warning: if it shows "grep binary file ... matches, please use -a as -a, --text equivalent to --binary-files=text
    # ，即让二进制文件等价于文本。
    for line in fileinput.input(files="12292021_raw.txt", inplace=True, backup='.bak'):
        # convert hex(Fazit-id) to dec(Fazit-id)
        if "ns: 3000000" in line:
            convertPart = hexStr_to_str(remove_blank(line[(line.rindex(":") + 1):]))
            print(line[:(line.rindex(":") + 2)] + convertPart)
            line = line[:(line.rindex(":") + 2)] + convertPart
        print(line.strip())


def formatStyle1(hint: str, value: str):
    """hint:     value"""
    return "%-25s%-s\n" % (hint, value)


"""To create HU base-identification"""


class HU(object):
    def __init__(self, fazit, serialNum, sw, hw, partnum, ECUnum):
        self.fazit = fazit
        self.serialNum = serialNum
        self.sw = sw
        self.hw = hw
        self.partnum = partnum
        self.ECUnum = ECUnum

    def getSW(self):
        return "Fazit-ID: " + self.fazit + "\t" + "Software Version: " + self.sw

    def __str__(self):
        # return "This is HU's base-identification: \n" \
        #        "Fazit Id: " + self.fazit + "\n" \
        #        "Serial Num: " + self.serialNum + "\n" \
        #        "Software Version: "  + self.sw + "\n" \
        #        "Hardware Version: "  + self.hw + "\n" \
        #        "Spare Part Num: " + self.partnum + "\n" \
        #        "ECU Part Num: " + self.ECUnum + "\n"
        return formatStyle1("This is HU's base-identification:", "") + \
               formatStyle1("Fazit-ID:", self.fazit) + formatStyle1("Serial Num:", self.serialNum) + \
               formatStyle1("Software Version:", self.sw) + formatStyle1("Hardware Version:", self.hw) + \
               formatStyle1("Spare Part Num:", self.partnum) + formatStyle1("ECU Part Num: ", self.ECUnum)


def main3():
    sample0 = HU("X9G-10222.11.2190020319", "VWX9GY0562391", "0420", "H14", "3GB035866A", "3GB035866A")
    sample1 = HU("X9G-10204.12.2190010548", "VWX9GY0598174", "0420", "H12", "3GB035866A", "3GB035866A")
    L = []
    L.append(sample0)
    L.append(sample1)
    for i in L:
        # print(i.getSW())
        print(i)


if __name__ == '__main__':
    # main3()
    main2()
