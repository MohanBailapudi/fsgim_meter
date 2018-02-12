import unittest
from fsgim_meter.measurements.item_base_type import ItemBaseType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType


class TestMeasurement(unittest.TestCase):

    def test_item_base_type(self):
        item = ItemBaseType()

    def test_measurement_metadata_type(self):
        self.test_description = "ActivePower"
        self.test_item_unit = 'in'
        self.test_si_scale_code = 'G'
        test_dict = {
            "itemDescription" : self.test_description,
            "itemUnits" : 91,
            "siScaleCode" : 0,
            "accumulationCharacteristic" : "",
            "dataQualifier" : "",
            "measurementQuality" : "",
            "resolution" : ""
        }
        item = MeasurementMetadataType(self.test_description,self.test_item_unit,self.test_si_scale_code)
        self.assertEqual(test_dict,item.serialize())


    def test_measurement_metadata_type_with_fail(self):
        self.test_description = "ActivePower"
        self.test_item_unit = 'ini'
        self.test_si_scale_code = 'G'
        with self.assertRaises(ValueError):
            item = MeasurementMetadataType(self.test_description,self.test_item_unit,self.test_si_scale_code)


    def test_measurement_metadata_type_with_no_arguments(self):
        with self.assertRaises(TypeError):
            item = MeasurementMetadataType()