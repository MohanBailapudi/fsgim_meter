"""
Defines Measurement Class
"""


class Measurement:

    def __init__(self,time_reference = ''):
        """

        :param timeReference:
        """
        self.time_reference = time_reference

    @property
    def time_reference(self):
        return self.timeReference

    @time_reference.setter
    def time_reference(self, val):
        if val == "":
            return ""
        if val.__class__.__name__ == 'UTCDateTimeInterval':
            self._time_reference =  val
        else:
            raise TypeError("enter object of UTCDateTimeInterval classes")
