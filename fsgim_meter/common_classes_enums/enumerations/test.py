import unittest
from fsgim_meter.common_classes_enums.enumerations.enumerations import MeasurementsEnum
from fsgim_meter.common_classes_enums.enumerations.enumerations import AccumulationKind
from fsgim_meter.common_classes_enums.enumerations.enumerations import DataQualifierKind
from fsgim_meter.common_classes_enums.enumerations.enumerations import QualityOfReading
from fsgim_meter.common_classes_enums.enumerations.enumerations import SiScaleCodeType
from fsgim_meter.common_classes_enums.enumerations.enumerations import UnitSymbolKind


class TestEnums(unittest.TestCase):

    def test_accumulationkind(self):
        test = AccumulationKind['bulkQuantity']

    def test_dataqualifierkind(self):
        test = DataQualifierKind['average']

    def test_qualityofreading(self):
        test = QualityOfReading['estimated']