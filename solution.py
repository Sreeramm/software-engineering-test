import datetime as dt
from prettytable import PrettyTable # Added PrettyTable for printing purpose

from seed import res


# TimeRange model used to store the consecutive start, end and length
class TimeRange:
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
        self.length = (end - start).days + 1 if start is not None and end is not None else 0

    def __repr__(self):
        return "Start={start}   End={end}   Length={length}".format(start=self.start, end=self.end, length=self.length)


# LongestTimeRangeAnalytics class to calculate the longest time logins
class LongestTimeRangeAnalytics:

    def __init__(self, login_timestamps=None):
        self.time_format = "%Y-%m-%d %H:%M:%S"
        self.login_timestamps = self._prepare_timestamps(login_timestamps)
        self.results = []

    # convert string based input to timestamp
    def _prepare_timestamps(self, login_timestamps):
        timestamps = []
        for date in login_timestamps:
            timestamps.append(dt.datetime.strptime(date, self.time_format).date())
        return timestamps

    # calculate the longest period(days) of consecutive login done based on the login_timestamps
    def calculate(self):

        if self.login_timestamps is not None and len(self.login_timestamps) > 0:
            start_time = self.login_timestamps[0]
            end_time = self.login_timestamps[0]
            count = 1

            for index in range(1, len(self.login_timestamps) - 1):  # O(n)
                diff_days = (self.login_timestamps[index] - end_time).days
                if diff_days == 0 or diff_days == 1:  # checks diff of current and prev date to find consecutive or not
                    count += 1  # increase the count to find the number of login in a date range
                else:
                    self.results.append(TimeRange(start_time, end_time, count))
                    start_time = self.login_timestamps[index]  # reset the start time to find next date range
                    count = 1  # reset count to 1, restart the consecutive date range
                end_time = self.login_timestamps[index]
            self.results.append(TimeRange(start_time, end_time, count))

    # display the calculated result based on longest period
    def display_results(self):
        self.results.sort(key=lambda rs: rs.length, reverse=True)  # rearrange the results based on longest period
        t = PrettyTable(['Start', 'End', 'Length'])
        for result in self.results:
            t.add_row([result.start, result.end, result.length])
        print(t)


if __name__ == "__main__":
    sorted_timestamp = sorted(res)
    longest_time_range = LongestTimeRangeAnalytics(sorted_timestamp)
    longest_time_range.calculate()
    longest_time_range.display_results()
