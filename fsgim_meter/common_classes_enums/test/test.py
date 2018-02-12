import unittest
from fsgim_meter.common_classes_enums.enums import AccumulationKind

class TestEnums(unittest.TestCase):

    def test_create_accumulation_kind(self):
        test_val = 'none'
        test_accumulation_kind_object = AccumulationKind[test_val]
