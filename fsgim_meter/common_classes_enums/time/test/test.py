import unittest
from fsgim_meter.common_classes_enums.time.utc_datetime_interval import UTCDateTimeInterval

class TestDateTime(unittest.TestCase):

    def test_utc_date_time(self):
        """

        :return:
        """
        self.duration = 5
        self.end = '2018-02-12 14:00:00+00:00'
        self.start = '2018-02-11 14:00:00+00:00'
        test = UTCDateTimeInterval(self.duration,self.end,self.start)

    def test_utc_date_time_with_wrong_format(self):
        """

        :return:
        """
        self.duration = 5
        self.end = '2018-02-12 14:00:00+00:00'
        self.start = '2018-02 14:00:00+00:00'
        with self.assertRaises(ValueError):
            test = UTCDateTimeInterval(self.duration,self.end,self.start)

    def test_utc_date_time_with_no_input(self):
        """

        :return:
        """
        self.duration = ''
        self.end = ''
        self.start = ''
        test = UTCDateTimeInterval(self.duration,self.end,self.start)

    def test_utc_date_time_with_test_dict(self):
        """

        :return:
        """
        self.duration = 5
        self.end = '2018-02-12 14:00:00+00:00'
        self.start = '2018-02-11 14:00:00+00:00'
        test_dict =  {
            "duration" : self.duration,
            "end" : self.end,
            "start" : self.start
        }
        test = UTCDateTimeInterval(self.duration, self.end, self.start)
        self.assertEqual(test_dict,test.serialize())