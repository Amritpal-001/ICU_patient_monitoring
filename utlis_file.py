
import time


def seconds_to_hours(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def time_tracking_function(starttime):
    Screen_time = time.time() - starttime
    Screen_time = round(Screen_time , 3)
    Screen_time = seconds_to_hours(Screen_time)
    return(Screen_time)

def current_date_variable():
    current_time = time.localtime()
    name =  str(current_time.tm_year)+ '-' + str(current_time.tm_mon)  + '-' +\
            str(current_time.tm_mday)
    return(name)

def current_time_variable():
    current_time = time.localtime()
    name = str(current_time.tm_hour) + ':' + str(current_time.tm_min)
    return(name)


#Does tweeter private option avialable???????????????????/
def tweet_alarm( tweet_bot_list , message):
    message = message
    for mail_id in email_list:
        send_email(mail_id , message)

def Mail_alarm(email_list , message):
    message = message
    for mail_id in email_list:
        send_email(mail_id , message)