import unittest

from solution import LongestTimeRangeAnalytics


class LongestTimeRangeAnalyticsTest(unittest.TestCase):

    def test_calculate(self):
        timestamps = [
            '2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05',
            '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05',
            '2021-03-18 15:13:05'
        ]
        longest_timerange = LongestTimeRangeAnalytics(timestamps)
        longest_timerange.calculate()
        self.assertEqual(len(longest_timerange.results), 2)
        self.assertEqual(str(longest_timerange.results[0]), "Start=2021-03-13   End=2021-03-13   Length=1")
        self.assertEqual(str(longest_timerange.results[1]), "Start=2021-03-16   End=2021-03-18   Length=3")

    def test_display_results(self):
        timestamps = [
            '2021-03-13 15:13:05', '2021-03-13 23:13:05', '2021-03-16 15:13:05', '2021-03-16 23:13:05',
            '2021-03-17 07:13:05', '2021-03-17 15:13:05', '2021-03-17 23:13:05', '2021-03-18 07:13:05',
            '2021-03-18 15:13:05'
        ]
        longest_timerange = LongestTimeRangeAnalytics(timestamps)
        longest_timerange.calculate()
        longest_timerange.display_results()
        self.assertEqual(len(longest_timerange.results), 2)
        self.assertEqual(str(longest_timerange.results[0]), "Start=2021-03-16   End=2021-03-18   Length=3")
        self.assertEqual(str(longest_timerange.results[1]), "Start=2021-03-13   End=2021-03-13   Length=1")

