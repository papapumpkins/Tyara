import datetime

now = datetime.datetime.now()


def returnCurrentTime():
    #Retrun format is an integer array [hour,Min,sec]
    #print (str(now.hour) +":"+str(now.minute)+":"+str(now.second))
    return[str(now.hour),str(now.minute),str(now.second)]

def returnTodayData():
    #Returns today's date, Month & Day of Week as strings
    date= now.strftime("%d")
    month = now.strftime("%B")
    day = now.strftime("%A")
    #print(date+month+day)
    return [date,month,day]

#returnCurrentTime()
#returnTodayData()