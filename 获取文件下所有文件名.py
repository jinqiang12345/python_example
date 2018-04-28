import os 
import os.path

l = []
def get_py(path, l):
    fileList = os.listdir(path)
    for filename in fileList:
        pathTmp = os.path.join(path, filename)
        if os.path.isdir(pathTmp):
            get_py(pathTmp, l)
        elif filename[-3:].upper() == '.PY':
            l.append(pathTmp)
path = input('请输入路径：').strip()
get_py(path, l)
print('在{0}目录及其子目录下找到{1}个py文件\n分别为：\n'.format(path, len(l)))
for filepath in l:
    print(filepath+'\n')