import math

def format_duration(seconds):
    date = ''
    if seconds >= 31536000:
        if seconds - math.floor(seconds / 31536000) * 31536000 >= 86400:
            date = str(math.floor(seconds/31536000))+' year, ' if seconds<63072000 else str(math.floor(seconds/31536000))+' years, '
            seconds -= math.floor(seconds/31536000)*31536000
        else:
            date = str(math.floor(seconds / 31536000)) + ' year' if seconds < 63072000 else str(math.floor(seconds / 31536000)) + ' years'
            seconds -= math.floor(seconds / 31536000) * 31536000
    if seconds >= 86400:
        if seconds - math.floor(seconds / 86400) * 86400 >= 3600 or seconds - math.floor(seconds / 86400) * 86400 >= 60:
            date += str(math.floor(seconds/86400))+' day, ' if seconds<172800 else str(math.floor(seconds/86400))+' days, '
            seconds -= math.floor(seconds / 86400) * 86400
        else:
            date += str(math.floor(seconds / 86400)) + ' day' if seconds < 172800 else str(math.floor(seconds / 86400)) + ' days'
            seconds -= math.floor(seconds / 86400) * 86400
    a = seconds%60
    if seconds >= 3600:
        if seconds-math.floor(seconds / 3600) * 3600 >= 60 and seconds%60 != 0:
            date += str(math.floor(seconds / 3600)) + ' hour, ' if seconds < 7200 else str(math.floor(seconds / 3600)) + ' hours, '
            seconds -= math.floor(seconds / 3600) * 3600
        else:
            date += str(math.floor(seconds / 3600)) + ' hour' if seconds < 7200 else str(math.floor(seconds / 3600)) + ' hours'
            seconds -= math.floor(seconds / 3600) * 3600
    if seconds >= 60:
        if seconds-math.floor(seconds / 60) * 60 == 0 and date != '':
            date += ' and ' + str(math.floor(seconds / 60)) + ' minute' if seconds < 120 else ' and ' + str(math.floor(seconds / 60)) + ' minutes'
            seconds -= math.floor(seconds / 60) * 60
        else:
            date += str(math.floor(seconds / 60)) + ' minute' if seconds < 120 else str(math.floor(seconds / 60)) + ' minutes'
            seconds -= math.floor(seconds / 60) * 60
    if seconds < 60 and seconds > 0:
        if date == '':
            date += str(seconds) + ' second' if seconds < 2 else str(seconds) + ' seconds'
        else:
            date += ' and ' + str(seconds) + ' second' if seconds < 2 else ' and ' + str(seconds) + ' seconds'
    if date == '':
        date = 'now'
    return date
#https://www.codewars.com/kata/52742f58faf5485cae000b9a