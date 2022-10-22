"""
Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar
and your coworker's calendar (both of which contain your respective meetings for the day, in the form of
[startTime, endTime] ), as well as both of your daily bounds (i.e., the earliest and latest times at which you're
available for meetings every day, in the form of [earliestTime, latestTime]).

Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily
bounds, and the duration of the meeting that you want to schedule, and that returns a list of all the time blocks
(in the form of [startTime, endTime] ) during which you could schedule the meeting, ordered from earliest time block
to latest.

Note that times will be given and should be returned in military time. For example: 8:30, 9:01, and 23:56.
Also note that the given calendar times will be sorted by start time in ascending order, as you would expect them
to appear in a calendar application like Google Calendar.

calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30

expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]

"""


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Time = Space = O(c1 + c2)
    """
    Logic:
    Step1: We will update the given calendars with unavailable time starting from 00 till daily bounds start,
    and from daily bounds ends till 23:59 which will help us view all the unavailable times for 24 hours format.
    We will also convert the start and end times into minutes.

    Step2: We will merge both the calendars together by start time, so that we may know the complete unavailable
    time whether its for person1 or person2.

    Step3: We will now merge the common intervals of the time to reduce the redundant start, end time which can
    be fully consumed by the previous time slots.

    Step4: Lastly, at this point will have all the unavailable time in the array, so we will get all the time slots
    which fall in between two time slots in the array and if that duration is greater than the meetings duration,
    we will add it to the result array.
    """

    # Step 1:
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    # Step: 2
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    # Step: 3
    flattenedCalendar = flattenCalendar(mergedCalendar)
    # Step: 4
    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)


def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:]
    # Inserting the unavailable time at the start of the day
    updatedCalendar.insert(0, ['0:00', dailyBounds[0]])
    # Inserting the unavailable time at the end of the day
    updatedCalendar.append([dailyBounds[1], '23:59'])
    # Converting the time to minutes
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))


def mergeCalendars(calendar1, calendar2):
    # Merging of the calendar1 and calendar2 by start time.
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    # Left over items from calendar 1
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    # Left over items from calendar 2
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged


def flattenCalendar(calendar):
    flattened = [calendar[0][:]]
    # We will merge the overlapping intervals
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        previousMeeting = flattened[-1]
        # Getting start and end times of current and previous meeting
        currentStart, currentEnd = currentMeeting
        previousStart, previousEnd = previousMeeting
        # If overlapping, then we merge
        if previousEnd >= currentStart:
            # Since we had merged the calendars by start time, so the start time will remain same,
            # but the end time will be the max of two end's.
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            # Updating the previous meeting after merging
            flattened[-1] = newPreviousMeeting
        else:
            # if not overlapping, then just add the current meeting.
            flattened.append(currentMeeting[:])
    return flattened


def getMatchingAvailabilities(calendar, meetingDuration):
    # Getting the blocks of available time from the unavailable time array
    matchingAvailabilities = []
    for i in range(1, len(calendar)):
        # Previous meetings end time is the start of the time.
        # Current meetings start time is the end of the time
        start = calendar[i - 1][1]
        end = calendar[i][0]
        # Total available time in minutes
        availabilityDuration = end - start
        # If the availability duration is greater than the meeting duration.
        if availabilityDuration >= meetingDuration:
            # We will append the start and end times to the result.
            matchingAvailabilities.append([start, end])
    # Converting the minutes to proper time format and returning the result.
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))


def timeToMinutes(time):
    # Converting time to minutes, extracting hour and minutes from the string, "11:30"
    hours, minutes = list(map(int, time.split(':')))
    # Converting hours to minutes and adding the extra minutes.
    return hours * 60 + minutes


def minutesToTime(minutes):
    # Converting minutes to hh:mm
    # Getting the hours present in the total minutes
    hours = minutes // 60
    # The remainder will give the extra minutes
    mins = minutes % 60
    # Converting to string.
    hoursString = str(hours)
    # Adding extra 0 to the minutes if its less than 10
    minutesString = "0" + str(mins) if mins < 10 else str(mins)
    # returning in hh:mm format.
    return hoursString + ':' + minutesString
