"""
Interpreter Codes 
-1: No Relevant Command
0 :
1 : Gmail Data
2 : Weather Current Temperature
3 : Weather Full Data
4 : Book a Cab from Home to Work
5 : Book a Cab from Work to Home
6 : Set an Alarm
7 : Classes Today
8 : Date
9 : Time
10: Lock Down the Speech Recognition
11: Unlock the Speech Recognition
12: Send Emergency Signal

"""

def Interpret_Text(command):
    code=-1
    command = command.lower()
    if(command.find("gmail")):
        code = 1
    if (command.find("weather")):
        if((command.find("now"))|(command.find("outside"))):
            code = 2
        if((command.find("report"))|(command.find("forecast"))):
            code =3
    if ((command.find("taxi"))|(command.find("cab")|(command.find("ride")))):
        if(command.find("home to work")):
            code = 4
        if(command.find("work to home")):
            code = 5
        else:
            code = 0
    if (command.find("alarm")):
        code = 6
    if (command.find("class")&command.find("today")):
        code = 7
    if (command.find("date")):
        code = 8
    if (command.find("time")):
        code = 9
    if (command.find("lock")&command.find("speech")):
        code = 10
    #if (command.find("unlock")&command.find("speech")):
    #    code = 11

    print(code)

    return code