from datetime import datetime   
from playsound import playsound 
alarm_time = input("Enter the time of alarm(12 hr Format) to be set in HH:MM:SS:(AM/PM) format : \n")
alarm_msg=input('Enter message to be displayed with Alarm:')
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

if int(alarm_hour)<0 or int(alarm_hour)>11:
    print('Inavlid hour paramater')
    exit()

if int(alarm_minute)<0 or int(alarm_minute)>59:
    print('Inavlid minutes paramater')
    exit()

if int(alarm_seconds)<0 or int(alarm_seconds)>66:
    print('Inavlid seconds paramater')
    exit()

if alarm_period=='':
    print('Inavlid period')
    exit()

print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print(alarm_msg)
                    playsound('audio.mp3',True)
                    break