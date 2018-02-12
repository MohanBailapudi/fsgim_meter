import unittest
from fsgim_meter.common_classes_enums.enums import AccumulationKind
from fsgim_meter.common_classes_enums.enums import DataQualifierKind
from fsgim_meter.common_classes_enums.enums import QualityOfReading
from fsgim_meter.common_classes_enums.enums import UnitSymbolKind
from fsgim_meter.common_classes_enums.enums import SiScaleCodeType
class TestEnums(unittest.TestCase):
    """
    Tests all enum classes
    """
    def test_create_accumulation_kind(self):
        test_val = 'none'
        test_accumulation_kind_object = AccumulationKind[test_val]


    def test_accumulation_kind_for_val(self):
        test_val = 'none'
        self.assertEqual(1, AccumulationKind.get_code(test_val))

    def test_accumulation_kind_for_none(self):
        test_val = ''
        self.assertEqual('', AccumulationKind.get_code(test_val))

    def test_accumulation_kind_raise_value_error(self):
        test_val = 'sum'
        with self.assertRaises(ValueError):
            AccumulationKind.get_code(test_val)

    def test_create_data_qualifier_kind(self):
        test_val = 'average'
        test_data_qualifier_kind_object = DataQualifierKind[test_val]


    def test_data_qualifier_kind_for_val(self):
        test_val = 'average'
        self.assertEqual(2, DataQualifierKind.get_code(test_val))

    def test_data_qualifier_kind_for_none(self):
        test_val = ''
        self.assertEqual('', DataQualifierKind.get_code(test_val))

    def test_data_qualifier_kind_raise_value_error(self):
        test_val = 'wrong'
        with self.assertRaises(ValueError):
            DataQualifierKind.get_code(test_val)

    def test_create_quality_of_reading(self):
        test_val = 'estimated'
        test_create_quality_of_reading_object = QualityOfReading[test_val]


    def test_dataquality_of_reading_for_val(self):
        test_val = 'estimated'
        self.assertEqual(0, QualityOfReading.get_code(test_val))

    def test_quality_of_reading_for_none(self):
        test_val = ''
        self.assertEqual('', QualityOfReading.get_code(test_val))

    def test_quality_of_reading_raise_value_error(self):
        test_val = 'wrong'
        with self.assertRaises(ValueError):
            QualityOfReading.get_code(test_val)

    def test_create_unit_symbol_kind(self):
        test_val = 'VA'
        test_unit_symbol_kind_object = UnitSymbolKind[test_val]


    def test_unit_symbol_kind_for_val(self):
        test_val = 'VA'
        self.assertEqual(3, UnitSymbolKind.get_code(test_val))

    def test_unit_symbol_kind_for_none(self):
        test_val = ''
        self.assertEqual('', UnitSymbolKind.get_code(test_val))

    def test_unit_symbol_kind_raise_value_error(self):
        test_val = 'wrong'
        with self.assertRaises(ValueError):
            UnitSymbolKind.get_code(test_val)

    def test_unit_symbol_kind_for_inch(self):
        test_val = 'in'
        self.assertEqual(91, UnitSymbolKind.get_code(test_val))

    def test_siscale_code_type(self):
        test_val = 'G'
        test_siscale_code_type_object = SiScaleCodeType[test_val]


    def test_siscale_code_type_for_val(self):
        test_val = 'G'
        self.assertEqual(0, SiScaleCodeType.get_code(test_val))

    def test_siscale_code_type_for_none(self):
        test_val = ''
        self.assertEqual('', SiScaleCodeType.get_code(test_val))

    def test_siscale_code_type_raise_value_error(self):
        test_val = 'wrong'
        with self.assertRaises(ValueError):
            SiScaleCodeType.get_code(test_val)
