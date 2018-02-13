"""
Defines Measurement Class
"""


class Measurement:

    def __init__(self,timeReference):
        """

        :param timeReference:
        """
        self.timeReference = timeReference

    @property
    def timeReference(self):
        return self.timeReference

    @timeReference.setter
    def timeReference(self, val):
        if val.__class__.__name__ == 'UTCDateTimeInterval':
            self._timeReference =  val
        else:
            raise TypeError("enter object of UTCDateTimeInterval class")
