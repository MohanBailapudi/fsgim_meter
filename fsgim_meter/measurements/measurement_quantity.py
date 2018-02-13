"""
Defines MeasuremnetQuantity class
"""

from fsgim_meter.measurements.measurement import Measurement

class MeasurementQuantity(Measurement):

    def __init__(self,uncertainity,value,time_reference = ''):
        super().__init__(time_reference)
        self.uncertainity = uncertainity
        self.value = value
