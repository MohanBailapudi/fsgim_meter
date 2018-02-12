import unittest
from fsgim_meter.measurements.item_base_type import ItemBaseType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType

class TestMeasurement(unittest.TestCase):

    def test_item_class_type(self):
        item = ItemBaseType()

    def test_item_class_type(self):
        self.test_description = "ActivePower"
        self.test_itemunit = "in"
        self.test_siscale = 'G'
        item = MeasurementMetadataType(self.test_description,self.test_itemunit,self.test_siscale)