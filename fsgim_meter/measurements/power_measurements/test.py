import unittest
from fsgim_meter.measurements.power_measurements.power_item_type import PowerItemType
from fsgim_meter.measurements.power_measurements.power_real_type import PowerRealType
from fsgim_meter.measurements.power_measurements.power_reactive_type import PowerReactiveType
from fsgim_meter.measurements.power_measurements.power_apparent_type import PowerApparentType
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