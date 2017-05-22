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
    code = -1
    command = command.lower()
    print(command)
    if (command.find("gmail") != -1):
        code = 1
    if (command.find("weather")):
        if ((command.find("now") != -1) | (command.find("outside")) != -1):
            code = 2
        if ((command.find("report")) != -1 | (command.find("forecast")) != -1):
            code = 3
    if (command.find("taxi") != -1) | (command.find("cab")) != -1 | (command.find("ride")) != -1:
        if (command.find("home to work")):
            code = 4
        elif (command.find("work to home") != -1):
            code = 5
        else:
            code = 0
    if (command.find("alarm") != -1):
        code = 6
    if (command.find("class") != -1 & command.find("today") != -1):
        code = 7
    if (command.find("date") != -1):
        code = 8
    if (command.find("time") != -1):
        code = 9
    if (command.find("lock") != -1 & command.find("speech") != -1):
        code = 10
    if (command.find("unlock") != -1 & command.find("speech") != -1):
        code = 11

    print(code)

    return