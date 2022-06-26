import sys
from func_timeout import func_set_timeout, FunctionTimedOut
import msvcrt

File_name = ''
@func_set_timeout(0.1)
def get_input_file(pre_str=''):
    global File_name
    File_name = pre_str
    while True:
        File_name += msvcrt.getwch()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('请拖入需要转换的文件')
        first_chr = msvcrt.getwch()
        try:
            get_input_file(first_chr)
        except FunctionTimedOut:
            File_name.strip('"')
    else:
        sys.argv[1]
        
File_name=File_name.replace('& ', '')
File_name=File_name.replace('\'', '')
File_name=File_name.strip('"')
f = open(File_name, 'r',encoding="utf-8")
newf = open('tradingview.txt', 'w',encoding="utf-8")
text = f.read()
# print(text)

t1=["CLOSE","OPEN","EMA","VOL","HIGH","LOW",":=","HHV","LLV","IF","{","MAX","SUM","ABS","AND","OR","NOT","CROSS","MIN"]
t2=["close", "open", "ta.ema", "volume", "high", "low", "=","ta.highest","ta.lowest","if","//{","math.max","math.sum","math.abs","and","or","!","ta.crossover","math.min"]

for i in range(len(t1)):
    text = text.replace(t1[i],t2[i])
text = text.replace(':=', '=')
text = text.replace(':', '=')
text = text.replace(';', '')

#replace REF: REF\((.+?),(.+?)\) > $1[$2]
#replace if : if\((.+?),(.+?),(.+?)\) > $1?$2:$3

# print(text)
newf.write(text)
f.close()
newf.close()