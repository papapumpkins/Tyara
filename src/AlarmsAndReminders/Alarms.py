def setAlarms(dialog):

    alarm_time_dialog = extract_alarm_time(dialog)
    return "An Alarm has been set for " + alarm_time_dialog

def extract_alarm_time(dialog):
    return "0700 hours"