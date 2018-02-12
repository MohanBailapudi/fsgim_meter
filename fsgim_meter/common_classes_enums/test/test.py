import unittest
from fsgim_meter.common_classes_enums.enums import AccumulationKind
from fsgim_meter.common_classes_enums.enums import DataQualifierKind
class TestEnums(unittest.TestCase):

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
        test_accumulation_kind_object = DataQualifierKind[test_val]


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