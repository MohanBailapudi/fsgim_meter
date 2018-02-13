"""
Defines MeasuremnetQuantity class
"""

from fsgim_meter.measurements.measurement import Measurement
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType

class MeasurementQuantity(Measurement):

    def __init__(self,uncertainity,value,measurement_metadata_type,time_reference = ''):
        """

        :param uncertainity:
        :param value:
        :type measurement_metadata_type: MeasurementMetadataType
        :param time_reference:
        """
        super().__init__(time_reference)
        self.uncertainity = uncertainity
        self.value = value
        self.measurement_metadata_type = measurement_metadata_type

    @property
    def measurement_metadata_type(self):
        return self.measurement_metadata_type

    @measurement_metadata_type.setter
    def measurement_metadata_type(self, val):
        if val.__class__.__name__ == 'MeasurementMetadataType':
            self._measurement_metadata_type = val
        else:
            raise TypeError("enter object of MeasurementMetadataType class")

    def serialize(self):

        """

        :return:
        """
        return {
            "uncertainity" : self.duration,
            "value" : self.end,
            "timeReference" : self.time_reference,
            "measurement_metadata_type" : self.measurement_metadata_type.serialize()

        }