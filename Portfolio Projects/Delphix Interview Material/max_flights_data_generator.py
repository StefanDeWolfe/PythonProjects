# Author: Stefan DeWolfe
# Created April 2022
import os
import random
import sys
import time
import typing


class FlightGenerator():
    def __init__(
        self,
        num_flights: int = 1000
        ):
        """
        This class generates flights for the max_flights.py problem to solve.

        :param num_flights: This is the number of flights it will create.
        """
        self.num_flights = num_flights
    def generate(
        self
        ) -> typing.List[str]:
        """
        This method generates flights, noted in epoch time, format below.
        departure   arrival
        """
        flights = []
        current_epoch_time = int(round(time.time(), 0 ))
        for i in range(self.num_flights):
            start_time = current_epoch_time + random.randint(0, 1000000)
            end_time = start_time + random.randint(0, 100000)
            flights.append(f"{start_time}   {end_time}")
        return flights


class FileWriter():
    def __init__(
        self, 
        file_path: str = "flight_schedule.txt"
        ):
        """
        This class writes to a file.
        :param output_file: The name of the output file
        """
        self.file_path = file_path
    def write(
        self,
        new_lines: typing.List[str], 
        ) -> None:
        """
        This method writes data to a file.
        :param new_lines: The list of strings that contain the data to write to the file
        """
        f = open(self.file_path, "w")
        print("writing to output file")
        for line in new_lines:
            f.write(line+"\n")
        f.close()
        print("New output file created")

def main(argv):
    """
    This will create a file called flight_schedule.txt
    that contains the data needed for max_flights.py to run properly
    """
    writer = FileWriter("flight_schedule.txt")
    fg = FlightGenerator(1000)
    data = fg.generate()
    writer.write(data)

if __name__ == "__main__":
    main(sys.argv[1:])
    print("")