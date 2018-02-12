import unittest


class TestEnums(unittest.TestCase):
    test_val = 'none'
    def test_create_accumulation_kind(self):
        test_accumulation_kind_object = AccumulationKind(test_val)
