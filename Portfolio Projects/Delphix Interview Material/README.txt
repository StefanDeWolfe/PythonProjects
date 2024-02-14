Hello!

Here is an explanation of these previous take home coding problems.

All problems but the top_5_delayed_flights.py were done in an interview (30 min to an hour.)
The top_5_delayed_flights.py problem was a take-home, 
done in about 1-2 hours to make sure I got things right and that it looked good.


library_dependancies.py
    This is a example of a class that can take in a dependency map and given a library from that map, 
    it will return the order of installation for the given desired library.
    It will detect a circular dependency and return an error message stating so.

max_flights.py
    This class calculates the maximum of total simultaneous flights. 
    It requires a file for flight times of aircraft. 
    I'll include the data generator and the data in its own file.

max_flights_data_generator.py
    This is the data generation file for the above problem. 
    it outputs the file flight_schedule.txt, a list of epoch times for a plane's departure and arrival.
    This was NOT written as a part of the code examination, but done later because I don't have the original file.

sum_of_two.py
    Given an array (list) of numbers, and a target number, 
    this method will calculate which numbers in the array can sum to that number and return their indexes, none otherwise.

top_5_delayed_flights.py
    Requires requests pandas libraries, use the following to install them if you already have python 3 installed
    Open Command Prompt, then run
    pip3 install requests
    pip3 install pandas
    ============== or if those dont work, try ============
    pip install requests
    pip install pandas

    This may take a bit to run.
    This take-home problem is outlined in take-home-problem.txt:

    "Your goal is to write a small program that utilizes the OpenSky public API and 
    prints the 5 most varied flight duration data from flights that arrived in KSFO the past 3 days, 
    categorized by departure airport."


Enjoy! 
And thanks for your consideration!

Best regards,
~Stefan DeWolfe
