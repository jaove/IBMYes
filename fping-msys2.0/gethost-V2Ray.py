#!/usr/bin/python
import base64
import time


def ToBase64(file, txt):
    with open(file, 'rb') as fileObj:
        image_data = fileObj.read()
        base64_data = base64.b64encode(image_data)
        fout = open(txt, 'w')
        fout.write(base64_data.decode())
        fout.close()


def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()

#ToBase64("./desk.jpg",'desk_base64.txt')  # 文件转换为base64
#ToFile("./desk_base64.txt",'desk_cp_by_base64.jpg')  # base64编码转换为二进制文件



t=0
count = len(open('速度排名.txt','r',encoding='UTF-8', errors='ignore').readlines())
# f = open('../gui-config.json','w')
#f = open('Url_Vmess.txt','w',encoding='UTF-8', errors='ignore')
file_object = open('速度排名.txt','r',encoding='UTF-8', errors='ignore')

lineStr64=''
try: 
    for line in file_object:

        line=line.strip('\n')
        data=line.split('\t')
        
        lineStr='{\n'
        lineStr=lineStr+'  "v": "2",\n'
        lineStr=lineStr+'  "ps": "ibmyes-'+str(t+1)+'",\n'
        lineStr=lineStr+'  "add": "'+data[0]+'",\n'
        lineStr=lineStr+'  "port": "443",\n'
        lineStr=lineStr+'  "id": "ac9a9f82-4d88-44b0-8cbf-a53f79c02d19",\n'
        lineStr=lineStr+'  "aid": "4",\n'
        lineStr=lineStr+'  "net": "ws",\n'
        lineStr=lineStr+'  "type": "none",\n'
        lineStr=lineStr+'  "host": "throbbing-recipe-1f97.3158953.workers.dev",\n'
        lineStr=lineStr+'  "path": "QMNAkopT4cERb3lj",\n'
        lineStr=lineStr+'  "tls": "tls"\n'
        lineStr=lineStr+'}\n'
        
        lineStr64=lineStr64+'vmess://'+str(base64.b64encode(lineStr.encode("utf-8")), "utf-8")+'\n'
        #print (lineStr64)
        t=t+1
finally:



#    links_file = 'Url_Vmess_links_{}.txt'.format(time.strftime('%Y-%m-%d_%H-%M-%S'))
    links_file = 'Url_Vmess_links.txt'
    f = open(links_file,'w',encoding='UTF-8', errors='ignore')
    f.write(lineStr64)
    f.close()
    file_object.close()
    
#    ToBase64(links_file,'Base64_'+links_file)
    ToBase64(links_file,'base64_v2ray.txt')
