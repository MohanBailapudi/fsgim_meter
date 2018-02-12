import unittest
from fsgim_meter.common_classes_enums.enums import AccumulationKind

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