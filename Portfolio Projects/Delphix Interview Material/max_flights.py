"""
===== Preface =====

Feel free to use whatever language you like, but this question
is difficult in C and C++, where there is insufficient library
support to answer it in an hour. If you prefer to program in one
of those languages, please ask us to provide you with a question
designed for those languages instead!

Choose the language you want to code in from the menu
labeled "Plain Text" in the top right corner of the
screen. You will see a "Run" button appear on the top
left -- clicking this will send your code to a Linux
server and compile / run it. Output will appear on the
right side of the screen.

For information about what libraries are available for
your chosen language, see:

    https://coderpad.io/languages


===== Prompt =====

Given a schedule of flight departure times and arrival times, 
write a program which determines the maximum number of flights 
in the air at any one time.

In this contrived scenario, you run an airport and are responsible 
for hiring pilots to manage incoming and outgoing flights. There is
a strict requirement that you must have at least one pilot on your
staff for each flight concurrently in the air.

You can find the input file at "./data/flight_schedule.txt" or in the Files
tab to view the contents.

In order to reduce formatting troubles, the Flight Schedule is listed in
epoch time (the number of seconds that have elapsed since the Unix epoch,
00:00:00 UTC on 1 January 1970) e.g 

Departures   Arrivals
1588112239   1588120699

Which corresponds to

Departures                                Arrivals
Tuesday, April 28, 2020 10:17:19 PM GMT   Wednesday, April 29, 2020 12:38:19 AM GMT


===== Example =====

For Simplicity sake, lets look at a simple example in regular human time:

Flight A takes off at 9AM and lands at 11AM, 
Flight B takes off at 10AM and lands at 1PM, 
Flight C takes off a 3PM and lands at 5PM 

Flight | Departures | Arrivals
------------------------------
A      | 09:00      | 11:00
B      | 10:00      | 13:00
C      | 15:00      | 17:00

From the hours of 9AM-10AM one flight will be in the air, from 
10AM-11AM two flights will be in the air, from 11AM-1PM one flight
will be in the air, from 1PM-3PM no flights will be in the air, and
from 3PM-5PM one flight will be in the air.

For this set of flights, you would therefore need to hire at least 2
distinct pilots to satisfy the requirement that each flight in progress
is managed by its own pilot.

More generally, given a text file which contains a list of flight
schedules (where a flight schedule consists of a departure time and
an arrival time) our goal is to determine the minimum number of pilots
we must hire to ensure that each flight in progress is managed by a
distinct pilot. The program should take the flight schedule file as
input and return the minimum number of pilots necessary to service
those flights.
"""
# Author: Stefan DeWolfe
# Created April 2022
class MaxFlightCalculator(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.dataArray = self._initalizeData()

    def _initalizeData(self):
        rawData = self._readFile()
        return self._processData(rawData)

    def _readFile(self):
        f = open(self.filepath, "r")
        fileString = f.read()
        f.close()
        return fileString.split('\n')

    def _processData(self, rawData):
        dataArray = []
        for element in rawData:
            if element in [''] or "#" in element:
                continue
            datapoint = element.split('   ')
            dataArray.append( (int(datapoint[0]), True) )# Departure
            dataArray.append( (int(datapoint[1]), False) )# Arrival
        dataArray.sort()
        return dataArray

    def calculateMaxSimultaneousFlights(self):
        maxNumberOfPilots = 0
        currentFlights = 0
        for entry in self.dataArray:
            currentFlights += 1 if entry[1] else -1
            maxNumberOfPilots = max(currentFlights, maxNumberOfPilots)
        return maxNumberOfPilots

def main():
    filepath = "flight_schedule.txt"
    maxFlightCalculator = MaxFlightCalculator(filepath)
    result = maxFlightCalculator.calculateMaxSimultaneousFlights()
    print("max number of flights at once: result = {}".format(result))

main()