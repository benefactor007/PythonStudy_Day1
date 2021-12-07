# coding=utf-8

# s = raw_input('You find >>>>')

"""
python的open函数的第二个参数为打开的模式，如rb，rt，这包括两部分，前一个字母表示以只读模式打开（r=read），第二个字母表示将内容识别成什么数据。b表示是2进制数据，t表示是文本数据。t是默认参数，不指定就是t，所以你的打开模式就是rt，只读的文本模式。文本模式一般需要指定编码方式。传入encoding=编码方式。
例如：
f=open('source.txt','r',encoding='utf8')
"""
import fileinput

"""
w+与r+区别：

r+：可读可写，若文件不存在，报错；w+: 可读可写，若文件不存在，创建

4. 记得close()关闭

当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

"""


# result = find_target_Line(s, 'workday.txt', 'rb')
# print "the type of func(\"find_target_Line\"):", type(result)

def find_all_target_lines(str):  # input str; return the list L
    L = []
    lineNum = 0
    while True:
        lineNum = find_target_Line(str, 'workday.txt', 'rb', lineNum)
        print("the lineNum is", lineNum)
        if lineNum == "Not found!":
            print("Done!")
            break
        L.append(lineNum)
    print("The list L is", L)
    return L


# find_all_target_lines("tester")

"""
def replace_file_data(file_path: str, data: str) -> None:
   
    在第一行插入数据
    :param file_path: file 路径
    :param data: 插入的数据
    :return:
    
    with fileinput.input(files=file_path, inplace=True) as fp:
        for d in fp:
            if fp.filelineno() == 1:
                # 如果行数为 1 则进行插入
                print(data)
            print(d, end="")

"""


def replace_file_data(file_path: str, data):
    # format_file_path = str(file_path)
    # format_data = str(data)
    # with fileinput.input(files=format_file_path, inplace=True) as fp:
    fp = fileinput.input(files=file_path, inplace=True)
    for d in fp:
        if fp.filelineno() == 1:
            # 如果行数为 1 则进行插入
            print(data)
        print(d.strip())
    fp.close()


def fileInfo_to_list(file_path: str) -> list:
    tempList = []
    for line in fileinput.input(files=file_path, inplace=False, backup='.bak'):
        if line.strip() != '':
            tempList.append(line.strip())
    return tempList


def overwriteFile(file_path: str, message: list):
    # for line, i in zip(fileinput.input(files=file_path, inplace=False, backup='.bak'), message):
    #     print(i)
    fp = fileinput.input(files=file_path, inplace=True, backup='.bak')
    for line in fp:
        if fileinput.isfirstline():
            for i in message:
                print(i)
    fp.close()


def find_target_Line(search: str, file_name: str, method: str, startPoint=0) -> int:
    # f = open(file_name,method).readlines()
    with open(file_name, method) as f:
        data = f.readlines()
        # print "Show the data as below\n", data
        print("The type of f is:", type(data))
        for i in range(startPoint, len(data)):
            if search in data[i]:
                print('The target line is', i + 1)
                return i + 1
                break
        else:
            return "Not found!"


"""
如果函数参数既要设定初始值（默认形参），又要进行注释，注释应该放在":“号与”=“号之间；如果要注释返回值，注释放在”)“与”:“之间，并加上”->"。
"""


def insert_message_to_file(file_path: str, message: list = [], lineNum: int = 0, search: str = "",
                           test: bool = True) -> bool:
    if search == '' and lineNum == 0:
        print('At least one of search and lineNum should be given')
        return False
    elif search != '' and lineNum != 0:
        print('Duplicate info as given...mess up!!! ')
        return False
    else:
        for line in fileinput.input(files=file_path, inplace=test, backup='.bak'):
            if search != '':
                # print(line.strip())
                if search in line:
                    # line = line.replace(search, "")
                    for i in message:
                        print(i)
                        # line = i
            # elif lineNum != 0:
            else:
                if fileinput.lineno() == lineNum:
                    for i in message:
                        print(i)
            print(line.strip())
        fileinput.close()
        return True


def insert_message_to_file_v2(file_path: str, message: str = '', lineNum: int = 0, search: str = "",
                           test: bool = True) -> bool:
    if search == '' and lineNum == 0:
        print('At least one of search and lineNum should be given')
        return False
    elif search != '' and lineNum != 0:
        print('Duplicate info as given...mess up!!! ')
        return False
    else:
        for line in fileinput.input(files=file_path, inplace=test, backup='.bak'):
            print(line.strip())             # put code over here, let insert info after search
            if search != '':
                # print(line.strip())
                if search in line:
                    # line = line.replace(search, "")
                    # line = message        # <- replace the search with message (option2)
                    print(message)          # <- just insert the message (option1)
                    # line = i
            # elif lineNum != 0:
            else:
                if fileinput.lineno() == lineNum:
                    for i in message:
                        print(i)
            # print(line.strip())  # put code over here, let insert info before search
        fileinput.close()
        return True


def test_insert_message_to_file():
    insert_message_to_file('workday.txt', search="According to", message=['Who are you?', "I'm your father"],
                           test=False)
    # insert_message_to_file('workday.txt', lineNum=16, message=['Who are you?', "I'm your father"], test=False)
    # insert_message_to_file('workday.txt', lineNum=16, message=['Who are you?', "I'm your father"],
    #                        search="According to", test=False)
    # try:
    #     insert_message_to_file(test=False)
    # except TypeError as error:
    #     print(error)


def main():
    # replace_file_data('workday.txt', 'fuckyou')
    # print(fileInfo_to_list("workday.txt"))
    # # overwriteFile("workday.txt", temp("workday.txt"))
    # print(find_target_Line("picture", "workday.txt", "rt"))
    # insert_message_to_file('workday.txt', search="According to",message=['Who are you?', "I'm your father"])
    # insert_message_to_file('workday.txt', lineNum=16, message=['Who are you?', "I'm your father"])
    # insert_message_to_file('workday.txt', lineNum=16, message=['Who are you?', "I'm your father"],search="According to")
    # test_insert_message_to_file()
    # insert_message_to_file('main.mnf', search='"MuVersion": "0665",', message=['"MuVersion": "C665",'],
    #                        test=False)
    # insert_message_to_file('main.mnf', search=' "SupportedTrains": [',
    #                        message=['', '"DevelopmentFlags": {', '  "SkipCheckManifestChecksum": true,',
    #                                 '  "SkipCheckInstallerChecksum": true,', '  "SkipCheckVariant": true', ' },', ''],
    #                        test=False)

    # insert_message_to_file_v2('main.mnf', search='"MuVersion": "0665",', message='"MuVersion": "C665"',
    #                        test=False)

    # insert_message_to_file_v2('main.mnf', search=' "SupportedTrains": [',
    #                        message='"DevelopmentFlags": {\n "SkipCheckManifestChecksum": true,'
    #                                '\n "SkipCheckInstallerChecksum": true,\n "SkipCheckVariant": true\n},',
    #                        test=False)
    insert_message_to_file_v2('main.mnf', search='"MuVersion": "0665",', message='"MuVersion": "C665"',
                           test=False)


if __name__ == '__main__':
    main()
