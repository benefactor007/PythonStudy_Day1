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


def find_target_Line(serach:str, file_name: str, method: str, startPoint=0):
    # f = open(file_name,method).readlines()
    with open(file_name, method) as f:
        data = f.readlines()
        # print "Show the data as below\n", data
        print("The type of f is:", type(data))
        for i in range(startPoint, len(data)):
            if serach in data[i]:
                print('The target line is', i + 1)
                return i + 1
                break
        else:
            return "Not found!"


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


def temp(file_path: str):
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



def main():
    # replace_file_data('workday.txt', 'fuckyou')
    print(temp("workday.txt"))
    # overwriteFile("workday.txt", temp("workday.txt"))
    print(find_target_Line("picture","workday.txt","rt"))


if __name__ == '__main__':
    main()
