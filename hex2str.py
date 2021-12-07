import binascii


def str_to_hexStr(str_info):
    return binascii.hexlify(str_info.encode('utf-8')).decode('utf-8')


def hexStr_to_str(hex_info):
    return binascii.unhexlify(hex_info.encode('utf-8')).decode('utf-8')


def main():
    3#5HG035866     #HH08S0342#*009X9G-10109.04.2199990011*=VWX9GY0148242

    print(str_to_hexStr("X9G-10109.04.2199990011"))
    hex_fazit = "0x" + str_to_hexStr("X9G-10109.04.2199990011")
    print(hex_fazit)
    print(hexStr_to_str("583947"))


if __name__ == '__main__':
    main()
