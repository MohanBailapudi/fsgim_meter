"""
Defines PowerMeasurementSet class
"""

from fsgim_meter.measurements.measurement_set import MeasurementSet
from fsgim_meter.measurements.power_measurements.power_real_quantity import PowerRealQuantity
from fsgim_meter.measurements.power_measurements.power_reactive_quantity import PowerReactiveQuantity
from fsgim_meter.measurements.power_measurements.power_apparent_quantity import PowerApparentQuantity
from fsgim_meter.measurements.power_measurements.power_real_type import PowerRealType
from fsgim_meter.measurements.power_measurements.power_reactive_type import PowerReactiveType
from fsgim_meter.measurements.power_measurements.power_apparent_type import PowerApparentType


class PowerMeasurementSet(MeasurementSet):
    def __init__(self,uncertainty,value,item_description,item_unit,si_scale_code):
        """

        """
        self.uncertainty = uncertainty
        self.value = value
        self.item_description = item_description
        self.item_unit = item_unit
        self.si_scale_code = si_scale_code


    def power_real_quantity(self):
        measurement_metadata_type = PowerRealType(self.item_description, self.item_unit, self.si_scale_code)
        return PowerRealQuantity(self.uncertainty, self.value, measurement_metadata_type).serialize()
    def power_reactive_quantity(self):
        measurement_metadata_type = PowerReactiveType(self.item_description, self.item_unit, self.si_scale_code)
        return PowerReactiveQuantity(self.uncertainty, self.value, measurement_metadata_type).serialize()
    def power_apparent_quantity(self):
        measurement_metadata_type = PowerApparentType(self.item_description, self.item_unit, self.si_scale_code)
        return PowerApparentQuantity(self.uncertainty, self.value, measurement_metadata_type).serialize()
