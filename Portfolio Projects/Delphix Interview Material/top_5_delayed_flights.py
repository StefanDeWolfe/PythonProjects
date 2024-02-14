# Author: Stefan DeWolfe
# Created April 2022
import requests
from datetime import datetime, timedelta
import pandas as pd

class TopFiveDelayedFlights(object):
    def __init__(self, airportICAO, startDate, endDate):
        self.airportICAO = airportICAO
        self.startDate = startDate
        self.endDate = endDate

    def _validateDates(self):
        return self.startDate < self.endDate and abs((self.endDate - self.startDate).days) <= 7

    def _printOutResults(self, df, numberOfRows = 5):
        print("---------------------------------------------------")
        print("Interval [{}, {}]".format(str(self.startDate.strftime("%Y-%m-%d %H:%M:%S")), str(self.endDate.strftime("%Y-%m-%d %H:%M:%S"))))
        print("---------------------------------------------------")
        print("Airport Code | (max - min flight duration)")
        print("---------------------------------------------------")
        for index, row in df.head(numberOfRows).iterrows():
            print("{0:<12} | {1}".format(index, str(timedelta(seconds = int(row["longestDelay"])))))

    def display(self):
        try:
            startTime = int(self.startDate.timestamp())
            endTime = int(self.endDate.timestamp())
            if (not self._validateDates()):
                raise ValueError
        except ValueError:
            if (abs((self.endDate - self.startDate).days) > 7):
                print("ERROR: start date and end date are greater than 7 days apart. Exiting.")
            elif (self.startDate > self.endDate):
                print("ERROR: start date is greater than end date. Exiting.")
            else:
                print("ERROR: Dates are invalid. Exiting.")
            exit(1)
        responseCode = 0
        response = None
        try:
            request = "https://opensky-network.org/api/flights/arrival?airport=" + self.airportICAO + "&begin=" + str(startTime) + "&end=" + str(endTime)
            response = requests.get(request)
            responseCode = response.status_code
            if(responseCode != 200):
                raise ValueError
            else:
                data = response.json()
                df = pd.json_normalize(data, max_level = 1)
                df["duration"] = df["lastSeen"] - df["firstSeen"]
                dfDurationGroup = df.groupby('estDepartureAirport')['duration'].agg(['max','min'])
                dfDurationGroup['longestDelay'] = dfDurationGroup['max'] - dfDurationGroup['min']
                dfLongestDelay = dfDurationGroup[['longestDelay']].sort_values(by = ['longestDelay'], ascending = False)
                self._printOutResults(dfLongestDelay)
        except ValueError:
            print("ERROR: got a {} response to the following request".format(responseCode))
            print(request)
            print(response)
            print("Params: \"{}\" | \"{}\" | \"{}\"".format(self.airportICAO, self.startDate.strftime("%Y-%m-%d %H:%M:%S"), self.endDate.strftime("%Y-%m-%d %H:%M:%S")))
            print("check the request for errors and parameters for correctness. Exiting.")
            exit(2)

def main():
    timeFrameInDays = 3
    airportICAO = "KSFO"
    startDate = datetime.today() - timedelta(days = timeFrameInDays)
    endDate = datetime.today()
    top5Delays = TopFiveDelayedFlights(airportICAO, startDate, endDate)
    top5Delays.display()

if __name__ == "__main__":
    main()