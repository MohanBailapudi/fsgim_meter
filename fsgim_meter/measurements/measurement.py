"""
Defines Measurement Class
"""

from fsgim_meter.common_classes_enums.time.utc_datetime_interval import UTCDateTimeInterval

class Measurement:

    def __init__(self,duration,end,start):
        self.timeReference = UTCDateTimeInterval(duration,end,start)