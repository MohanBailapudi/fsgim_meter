"""
Defines UTCDateTimeInterval class
"""
import re
from fsgim_meter.common_classes_enums.time.datetime_interval import DateTimeInterval


class ValidateUTC():

    def validateutc(utcdatetime):
        """

        :return:
        """
        if utcdatetime == "":
            return ""
        RE = re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$')
        if bool(RE.search(utcdatetime)) == True:
            return utcdatetime
        else:
            raise ValueError("enter in UTC date Time format")



class UTCDateTimeInterval(DateTimeInterval,ValidateUTC):


    def __init__(self,duration = '',end = '',start = ''):

        """

        :param duration:
        :param end:
        :param start:
        """
        self.duration = duration
        self.end = ValidateUTC.validateutc(end)
        self.start = ValidateUTC.validateutc(start)

    def serialize(self):

        """

        :return:
        """
        return {
            "duration" : self.duration,
            "end" : self.end,
            "start" : self.start
        }






