# coding:utf-8
'''
把舊的測試檔案加上 min & max 語法

Created on 2020年3月4日
@author: rocky.wang
'''

def main():
    for i in range(150):
        filename = f"query{str(i).zfill(3)}.txt"
        processFile(filename)

            
def processFile(filename):
    print(filename)
    lines = list(open(filename))
    newlist = []
    for line in lines:
        line = line.strip()
        line = line.replace('format=productSearch', 'format=json')
        line = line[0 : len(line)-1]
        line = line + '%20all(group(PRC)%20max(1)%20order(avg(PRC))%20each(output(count())))%20all(group(PRC_CLONE)%20max(1)%20order(-avg(PRC_CLONE))%20each(output(count()))))'
        newlist.append(line)
        
    newfilename = filename.replace('query', 'new')
    with open(newfilename, 'w') as f1:
        for line in newlist:
            f1.write(line+"\n")

if __name__ == '__main__':
    main()

