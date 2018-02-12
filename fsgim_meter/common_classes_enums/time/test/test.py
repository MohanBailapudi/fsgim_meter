import unittest
from fsgim_meter.common_classes_enums.time.utc_datetime_interval import UTCDateTimeInterval

class TestDateTime(unittest.TestCase):

    def test_utc_date_time(self):
        self.duration = 5
        self.end = '2018-02-12 14:00:00+00:00'
        self.start = '2018-02-11 14:00:00+00:00'
        test = UTCDateTimeInterval(self.duration,self.end,self.start)