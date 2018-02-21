import unittest
from fsgim_meter.measurements.power_measurements.power_item_type import PowerItemType
from fsgim_meter.measurements.power_measurements.power_real_type import PowerRealType
from fsgim_meter.measurements.power_measurements.power_reactive_type import PowerReactiveType
from fsgim_meter.measurements.power_measurements.power_apparent_type import PowerApparentType
from fsgim_meter.measurements.power_measurements.power_quantity_type import PowerQauantityType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType
from fsgim_meter.measurements.power_measurements.power_real_quantity import PowerRealQuantity
from fsgim_meter.measurements.power_measurements.power_reactive_quantity import PowerReactiveQuantity
from fsgim_meter.measurements.power_measurements.power_apparent_quantity import PowerApparentQuantity


class TestPowerMeasurements(unittest.TestCase):


    ### Test PowerItemType class ###

    def test_power_item_type(self):
        """

        """
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerItemType(self.test_description, self.test_item_unit, self.test_si_scale_code)

    def test_power_real_type(self):
        """

        """
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerRealType(self.test_description, self.test_item_unit, self.test_si_scale_code)


    def test_power_reactive_type(self):
        """

        """
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerReactiveType(self.test_description, self.test_item_unit, self.test_si_scale_code)

    def test_power_apparent_type(self):
        """

        """
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerApparentType(self.test_description, self.test_item_unit, self.test_si_scale_code)


    ### Test PowerQuantityType ###


    def test_power_quantity_type(self):
        """

        """
        test_uncertainity = 250
        test_value = 250
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = MeasurementMetadataType(self.test_description, self.test_item_unit, self.test_si_scale_code)
        test = PowerQauantityType(test_uncertainity, test_value, item)


    def test_power_real_quantity(self):
        """

        """
        test_uncertainity = 250
        test_value = 250
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerRealType(self.test_description, self.test_item_unit, self.test_si_scale_code)
        test = PowerRealQuantity(test_uncertainity, test_value, item).serialize()
        print(test)
    def test_power_reactive_quantity(self):
        """

        """
        test_uncertainity = 250
        test_value = 250
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerReactiveType(self.test_description, self.test_item_unit, self.test_si_scale_code)
        test = PowerReactiveQuantity(test_uncertainity, test_value, item)


    def test_power_apparent_quantity(self):
        """

        """
        test_uncertainity = 250
        test_value = 250
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        item = PowerApparentType(self.test_description, self.test_item_unit, self.test_si_scale_code)
        test = PowerApparentQuantity(test_uncertainity, test_value, item)