import unittest
from fsgim_meter.measurements.item_base_type import ItemBaseType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType
from fsgim_meter.measurements.measurement import Measurement
from fsgim_meter.common_classes_enums.time.utc_datetime_interval import UTCDateTimeInterval


class TestMeasurement(unittest.TestCase):


    ###Test cases for ItemBaseType###
    def test_item_base_type(self):
        item = ItemBaseType()


    ###Test cases for MeasurementMetadataType###
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

    ###Test cases for Measurement###

    def test_measurement_argumnet_type(self):
        val = ItemBaseType()
        test = Measurement(val)

    def test_measurement_argumnet_type(self):
        val = UTCDateTimeInterval()
        test = Measurement(val)

    def test_measurement_blank_argumnet_type(self):
        val = ""
        test = Measurement(val)