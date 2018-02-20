"""
Defines PowerReactiveQuantity class
"""

from fsgim_meter.measurements.power_measurements.power_quantity_type import PowerQauantityType
from fsgim_meter.measurements.measurement_quantity import MeasurementQuantity

class PowerReactiveQuantity(PowerQauantityType):

    @MeasurementQuantity.measurement_metadata_type.setter
    def measurement_metadata_type(self, val):
        if val.__class__.__name__ == 'PowerReactiveType':
            self._measurement_metadata_type = val
        else:
            raise TypeError("enter object of PowerReactiveType class")