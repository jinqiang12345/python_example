import os
import codecs

def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir)
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file, target)
            os.chdir(os.pardir)
start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
video_list = []

search_file(start_dir, target)

f = codecs.open(program_dir + os.sep + 'videoList.txt', 'w', 'utf8')
f.writelines(video_list)
f.close