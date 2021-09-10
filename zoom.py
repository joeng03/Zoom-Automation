import time
import csv
import datetime
import pyautogui
import os
import keyboard

Days={'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6}
Links={
'班会' :
'https://meet.google.com/lookup/hdp5wisszo',

'华文': 
'https://zoom.us/j/9023624412?pwd=OWJ0Vzg0S3MxT0JMS3BSb1JBRjMzQT09',

'国文': 
'https://us04web.zoom.us/j/4040910191?pwd=eldNS2JTS3VJRE5YWWwyWFlwKyt4UT09',

'翻译' :
'https://us02web.zoom.us/j/4996908916?pwd=RjNCcG8wZTE4OEk5ak1xbDR6b05vdz09',

'英文' : 
'https://us04web.zoom.us/j/7893283784?pwd=T2JNSE5kRy81eXNiTkVKZVgxTlZOdz09',

'生物' : 
'https://us02web.zoom.us/j/6315330904?pwd=VXJPUFoxeTY1eDlPK09yeXRocXRJdz09',

'化学' : 
'https://zoom.us/j/93437785753?pwd=NFE0bmNabjRHckcxNGR1K2drZ29WZz09',

'物理' : 
'https://us02web.zoom.us/j/9448860199?pwd=MEQxOWdnVmtZS0RHVG5FVU9VUGdndz09',

'力学':
'https://us02web.zoom.us/j/3090185152?pwd=ODc4M2NqZmpBK290ZDBTQ0N2M1MwQT09',

'微积分': 
'https://us02web.zoom.us/j/5826591153?pwd=NTB1em1yNWNLOGJuRVo0OWZ5Zngwdz09',

'解几': 
'https://us02web.zoom.us/j/5826591153?pwd=NTB1em1yNWNLOGJuRVo0OWZ5Zngwdz09',

'美术': 
'https://zoom.us/j/9675511790?pwd=YkFYQUpVSzdFV2tQQnJjWGxmdVZJUT09',

'音乐':
'https://us04web.zoom.us/j/9629766341?pwd=S3dxVFBBNzYwU1RXRG1PelJmOXhBZz09',

'通识教育':
'https://us02web.zoom.us/j/8585858858?pwd=QUtFTGNSK283cnZjditWRkdqMmNtZz09',

'电脑':
'https://meet.google.com/ikj-qhgf-igc?authuser=4',

'体育':
'https://us04web.zoom.us/j/5524167302?pwd=OHdkNUFyYmNVY0J6VkhwVDlSdmhRUT09'
}
pyautogui.FAILSAFE=False
def signIn(meeting_id,password):
    os.startfile(r"C:\Users\user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom.lnk")
    joinbtn=pyautogui.locateCenterOnScreen("joinameeting.png")
    while(joinbtn==None):
        try:
            joinbtn=pyautogui.locateCenterOnScreen("joinameeting.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(joinbtn)
    pyautogui.click()

    meetingidbtn=pyautogui.locateCenterOnScreen("meetingid.png")
    while(meetingidbtn==None):
        try:
            meetingidbtn=pyautogui.locateCenterOnScreen("meetingid.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(meetingidbtn)
    keyboard.write(meeting_id)
    pyautogui.press('enter')
    '''join=pyautogui.locateCenterOnScreen("join.png")
    while(join==None):
        try:
            join=pyautogui.locateCenterOnScreen("join.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(join)
    pyautogui.click()'''

    passcode=pyautogui.locateCenterOnScreen("meetingPasscode.png")
    while(passcode==None):
        passcode=pyautogui.locateCenterOnScreen("meetingPasscode.png")
    pyautogui.moveTo(passcode)
    keyboard.write(password)
    pyautogui.press('enter')

    maxbtn=pyautogui.locateCenterOnScreen("maximise.png")
    while(maxbtn==None):
        try:
            maxbtn=pyautogui.locateCenterOnScreen("maximise.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(maxbtn)
    pyautogui.click()
    Chat=pyautogui.locateCenterOnScreen("Chat.png")
    while(Chat==None):
        try:
            Chat=pyautogui.locateCenterOnScreen("Chat.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(Chat)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("Ng Yin Joe 65 160059")
    pyautogui.press('enter')
    return

def main():
    with open('zoom.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        timetable=list(csv_reader)
        now=datetime.datetime.now()
        day=now.strftime("%a")
        previous_class=""
        while True:
            now=datetime.datetime.now()
            start=now.strftime("%X")[0:5]
            i=0
            for class_start in timetable[0]:
                if(class_start==start):
                    break
                i+=1
            if(not i==11 and not previous_class==start):
                previous_class=start
                link=Links[timetable[Days[day]][i]]
                #print(timetable[Days[day]][i])
                if('https://meet.google.com' in link):
                    print('Use Google Meet:',link)
                else:
                    id=""
                    pwd=""
                    for c in range(0,len(link)):
                        if(link[c]=='j'):
                            c+=2
                            while(not link[c]=='?'):
                                id+=link[c]
                                c+=1
                            c+=5
                            while(c<len(link)):
                                pwd+=link[c]
                                c+=1
                            break
                    print(pwd)
                    signIn(id,pwd)
            time.sleep(20)
if __name__=="__main__":
    main()
