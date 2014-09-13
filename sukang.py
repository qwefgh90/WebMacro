#-*- encoding: ms949 -*-
import requests as rs
import time
import re
import random
_headers ={'Host': 'haksa.incheon.ac.kr:7790',
'Connection': 'keep-alive',
'Content-Length': 40,
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin': 'http://haksa.incheon.ac.kr:7790',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'DNT': 1,
'Referer': 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_list_basket.jsp',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'
#,'Cookie': 'JSESSIONID=BvBrrfWIdvtd22SY1ODm9qY3MaIP9YYxKaA2JYaMwE0uVHXKS9FRlexMGRfmgCQa.uitiwas1_servlet_sukang4;Path=/'
}



url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_result_list.jsp'

#payload={'par_type':'insert','par_subjectNo':'XAA1466002'}#���
#payload={'par_type':'insert','par_subjectNo':'XAA1375002'}#������
payload1={'par_type':'insert','par_subjectNo':'O810214001'}#��Ȱ ������ ���ؿ� ȸ��
payload2={'par_type':'insert','par_subjectNo':'O810233001'}#�ΰ� �ൿ�� �ǽ�
payload3={'par_type':'insert','par_subjectNo':'O820101001'}#ȸ����� ����

loginheaders={
    'Host': 'haksa.incheon.ac.kr:7790',
'Connection': 'keep-alive',
'Content-Length': 42,
'Cache-Control': 'max-age=0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin': 'http://haksa.incheon.ac.kr:7790',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'DNT': 1,
'Referer': 'http://haksa.incheon.ac.kr:7790/s_kang/sukang_main.html',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
'Cookie': '_ga=GA1.3.1162676313.1409157447; WMONID=s6C5jwO0OiU; NetFunnel_ID=5002%3A200%3Akey%3D0D0ECE3103503E60FC1429F3B9EFCAC912069A0B233763823248DAEDBC9A5F8B86DA9B62060D31630C72ECF811BBE5F3756E646566696E6564%26utime%3D1409158995%26ip%3D117.16.191.161%26port%3D8000'}
url_login='http://haksa.incheon.ac.kr:7790/ssukang/sinLogin_check.jsp'

#��Ű ����
def login(id,passwd):
    global _headers
    payload = {'as_hakbun':id, 'as_jumin_seq':passwd}
    r = rs.post(url_login,data=payload,headers=loginheaders)
   # print r.headers
    JESESSION = re.findall('JSESS.*;',r.headers['set-cookie'])[0]
  #  cookie = r.headers['set-cookie']
    _headers= loginheaders
    _headers['Cookie'] = JESESSION
   # print JESESSION
   # print r.text
    resp = rs.get(url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_frame.jsp'
                  ,headers={'Cookie':_headers['Cookie']})
    if(len(reobj_loginfail.findall(r.text.encode('ms949')))>=1):
        print '�α��� ����'
        return False
    else :
        print '�α��� ����'
        return True
    #print resp.text
   # resp = rs.get(url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_info.jsp'
   #             ,headers={'Cookie':_headers['Cookie']})
   # resp = rs.get(url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_menu.jsp'
   #             ,headers={'Cookie':_headers['Cookie']})
   # resp = rs.get(url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_list.jsp'
   #             ,headers={'Cookie':_headers['Cookie']})Q
   # resp = rs.get(url = 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_result_list.jsp?par_type=search&par_subjectNo=non'
   #             ,headers={'Cookie':_headers['Cookie']})
   # print resp.text
   # print headers

reobj_script = re.compile('<script>.*\'(.*)\'.*</script>')
reobj_loginfail = re.compile('Ʋ���ϴ�')
reobj_suc = re.compile('���� �Ϸ�')
reobj_already = re.compile('�̹� ��û')
reobj = re.compile('�����Ǿ����ϴ�')
def requestPost():
    responseText =''
    r = rs.post(url,data=payload,headers=headers)
    responseText = r.text.encode('ms949')
    print responseText
    if(len(reobj.findall(responseText))==0):
        print '������û ����...'
        with open('log/'+str(time.time())+'.html','w') as f:
            f.write(responseText)
        return True
    else:
        print '�����Ǿ����ϴ�...'
        return False
def requestPostParam(payloadParam):
    r = rs.post(url,data=payloadParam,headers=_headers)
    responseText = r.text.encode('ms949')
   # print responseText
    if(len(reobj_suc.findall(responseText))>=1):
        print '������û ����...'
        return True
    elif (len(reobj.findall(responseText))>=1):
        print '�ο��� ���� �����Ǿ����ϴ�...'
        return False 
    elif (len(reobj_already.findall(responseText))>=1):
        print '�̹� ���� �Ͽ����ϴ�... Ȩ���������� ������ �� Ȯ�����ּ���'
        return 'already'
    else :
        _list = reobj_script.findall(responseText)
        for i in _list:
            print i
        print '->',payloadParam['par_subjectNo']
        
        return 'already'


def dummy1():
    __headers={
    'Host': '117.16.191.161:8000',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
    'DNT': 1,
    'Referer': 'http://haksa.incheon.ac.kr:7790/s_kang/sukang_login.html',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'}
    url = 'http://117.16.191.161:8000/ts.wseq?opcode=5101&nfid=0&prefix=NetFunnel.gRtype=5101;&js=yes&1409103499846&uid=undefined&utid=undefined'
    rs.get(url,headers=__headers)

def dummy2():
    __headers={
    'Host': '117.16.191.161:8000',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
    'DNT': 1,
    'Referer': 'http://haksa.incheon.ac.kr:7790/ssukang/jsp/sinSukang_result_list.jsp',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4'}
    url = 'http://117.16.191.161:8000/ts.wseq?opcode=5004&key=0F4E4A1D66C96D0E92DC9DDEAF2CA2427B8DF6FC723654EF0C62F68210AC842A86DA9B62060D31630C72ECF811BBE5F3756E646566696E6564&nfid=0&prefix=NetFunnel.gRtype=5004;&js=yes&1409103820487'
    rs.get(url,headers=__headers)
    
flag1=False;
flag2=False;
flag3=False;

import sys
print 'by ChanG'
SLEEPTIME = 3

_id = raw_input('��Ż ���̵� : ')
_passwd = raw_input('��Ż ��� : ')
try:
    SLEEPTIME = int(raw_input('���ϴ� ����(��) : '))
except:
    print '�ð��� �ùٸ��� �Է����ּ���. (3��)'
    SLEEPTIME = 3
if len(_id)<=0 or len(_passwd)<=0:
    print '���̵�� / ����� �Է����ּ���'
    raw_input();
    sys.exit(0)
if(login(_id,_passwd) == False):
    sys.exit(0)

requestList = []
requestFlag = []
try:
    with open('setting.txt','r') as f:
        requestList = f.readlines()
        requestList = [value.strip('\r\n') for value in requestList];
        for i in requestList:
            requestFlag.append(False)
except:
    print 'setting.txt ������ �������� �ʽ��ϴ�. (������� �� �ٸ��� ���¹�ȣ�� �����ּ���)'
    raw_input();
    sys.exit(0)

if len(requestList)==0:
    print 'setting.txt�� ������� �� �ٸ��� ���¹�ȣ�� �����ּ���.'
    raw_input();
    sys.exit(0)
print '��û�� ��ȣ:',requestList
#print requestFlag
while(1):
    for index,idValue in enumerate(requestList):
        if requestFlag[index]==False:
            print '��û�ϴ� ��...',index,':',idValue
            requestPayload={'par_type':'insert','par_subjectNo':idValue}
            dummy1()
            if(requestPostParam(requestPayload)==True):
                requestFlag[index]=True
            sleeptime = int(random.random()*SLEEPTIME)+1
            time.sleep(sleeptime)
            dummy2()
        else:
            print '�̹� �����Ͽ����ϴ�...',index,':',idValue

    continue

    if(flag1==False):
        print '��û�ϴ� ��...1'
        dummy1()
        if(requestPostParam(payload1)==True):
            flag1=True
        sleeptime = int(random.random()*SLEEPTIME)+1
        time.sleep(sleeptime)
        dummy2()
    if(flag2==False):
        print '��û�ϴ� ��...2'
        dummy1()
        if(requestPostParam(payload2)==True):
            flag2=True
        sleeptime = int(random.random()*SLEEPTIME)+1
        time.sleep(sleeptime)
        dummy2()
    if(flag3==False):
        print '��û�ϴ� ��...3'
        dummy1()
        if(requestPostParam(payload3)==True):
            flag3=True
        sleeptime = int(random.random()*SLEEPTIME)+1
        time.sleep(sleeptime)
        dummy2()

