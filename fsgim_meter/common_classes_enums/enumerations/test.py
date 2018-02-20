import unittest
from fsgim_meter.common_classes_enums.enumerations.enumerations import MeasurementsEnum
from fsgim_meter.common_classes_enums.enumerations.enumerations import AccumulationKind
from fsgim_meter.common_classes_enums.enumerations.enumerations import DataQualifierKind
from fsgim_meter.common_classes_enums.enumerations.enumerations import QualityOfReading
from fsgim_meter.common_classes_enums.enumerations.enumerations import SiScaleCodeType
from fsgim_meter.common_classes_enums.enumerations.enumerations import UnitSymbolKind


class TestEnums(unittest.TestCase):

    def test_accumulationkind(self):
        test = AccumulationKind.get_code('bulkQuantity')
    def test_dataqualifierkind(self):
        test = DataQualifierKind.get_code('average')
    def test_qualityofreading(self):
        test = QualityOfReading.get_code('estimated')
    def test_siscalecodetype(self):
        test = SiScaleCodeType.get_code('G')
    def test_unitsymbolkind(self):
        test = UnitSymbolKind.get_code('in')

    def test_accumulationkind_wrong(self):
        try:
            test = AccumulationKind.get_code('wrong')
        except:
            raise ValueError("enter correct value")
    def test_dataqualifierkind_wrong(self):
        try:
            test = DataQualifierKind.get_code('wrong')
        except:
            raise ValueError("enter correct value")
    def test_qualityofreading_wrong(self):
        try:
            test = QualityOfReading.get_code('wrong')
        except:
            raise ValueError("enter correct value")
    def test_siscalecodetype_worng(self):
        try:
            test = SiScaleCodeType.get_code('wrong')
        except:
            raise ValueError("enter correct value")
    def test_unitsymbolkind_wrong(self):
        try:
            test = UnitSymbolKind.get_code('wrong')
        except:
            raise ValueError("enter correct value")