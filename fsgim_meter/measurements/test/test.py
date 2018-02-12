import unittest
from fsgim_meter.measurements.item_base_type import ItemBaseType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType
from fsgim_meter.common_classes_enums.enums import UnitSymbolKind
from fsgim_meter.common_classes_enums.enums import SiScaleCodeType
class TestMeasurement(unittest.TestCase):

    def test_item_base_type(self):
        item = ItemBaseType()

    def test_measurement_metadata_type(self):
        self.test_description = "ActivePower"
        self.test_item_unit = UnitSymbolKind.get_code("in")
        self.test_si_scale_code = SiScaleCodeType.get_code("G")
        test_dict = {
            "itemDescription" : self.test_description,
            "itemUnits" : self.test_item_unit,
            "siScaleCode" : self.test_si_scale_code,
            "accumulationCharacteristic" : "",
            "dataQualifier" : "",
            "measurementQuality" : "",
            "resolution" : ""
        }
        item = MeasurementMetadataType(self.test_description,self.test_item_unit,self.test_si_scale_code)
        self.assertEquals(test_dict,item.serialize())


    def test_measurement_metadata_type_with_no_arguments(self):
        with self.assertRaises(TypeError):
            item = MeasurementMetadataType()