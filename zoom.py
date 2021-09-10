import time
import csv
import datetime
import pyautogui
import os
import keyboard

Days={'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6}
Links={}
#Links contains all the subject's names and their corresponding zoom links
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
    
     #Records attendance if needed
    Chat=pyautogui.locateCenterOnScreen("Chat.png")
    while(Chat==None):
        try:
            Chat=pyautogui.locateCenterOnScreen("Chat.png")
        except Exception as e:
            print(e)
    pyautogui.moveTo(Chat)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("YOUR NAME")
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
