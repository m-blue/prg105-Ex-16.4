class Time():
    """attributes: hour, minute, second"""


def increment(time, seconds):
    ntime = Time()

    ntime.minutes, ntime.seconds = divmod(seconds, 60)
    ntime.hours, ntime.minutes = divmod(ntime.minutes, 60)
    ntime.days, ntime.hours = divmod(ntime.hours, 24)

    ntime.seconds += time.second

    if ntime.seconds >= 60:
        ntime.seconds -= 60
        ntime.minutes += 1

    ntime.minutes += time.minute

    if ntime.minutes >= 60:
        ntime.minutes -= 60
        ntime.hours += 1

    ntime.hours += time.hour

    if time.hour >= 24:
        time.hour -= 24
        time.day = 1

    ntime.days += time.day

    return ntime

time1 = Time()
time1.day = 0
time1.hour = 5
time1.minute = 00
time1.second = 00

sec_incr = 5000

print 'New Time object: %.2d:%.2d:%.2d:%.2d' % (increment(time1, sec_incr).days,increment(time1, sec_incr).hours,increment(time1, sec_incr).minutes,increment(time1, sec_incr).seconds)

print 'Previous Time object: %.2d:%.2d:%.2d:%.2d' % (time1.day, time1.hour, time1.minute, time1.second)


