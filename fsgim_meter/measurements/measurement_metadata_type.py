"""
Defines MeasurementmetadataType class
"""

from fsgim_meter.measurements.item_base_type import ItemBaseType
from fsgim_meter.common_classes_enums.enums import UnitSymbolKind
from fsgim_meter.common_classes_enums.enums import SiScaleCodeType


class MeasurementMetadataType(ItemBaseType):
    """
    Defines Metadata associated with a measurement.
    """
    def __init__(self, item_description, item_units, si_scale_code, accumulation_characteristic="", data_qualifier="",
                 description="", measurement_quality="", resolution=""):
        """

        :param itemDescription:
        :param item_units:
        :param si_scale_code:
        :param accumulation_characteristic:
        :param data_qualifier:
        :param description:
        :param measurement_quality:
        :param resolution:
        """
        self.item_description = item_description
        self.item_units = UnitSymbolKind.get_code(item_units)
        self.si_scale_Code = SiScaleCodeType.get_code(si_scale_code)
        self.accumulation_characteristic = accumulation_characteristic
        self.data_qualifier = data_qualifier
        self.description = description
        self.measurement_quality = measurement_quality
        self.resolution = resolution

    @property
    def item_description(self):
        return self._item_description

    @item_description.setter
    def item_description(self, val):
        self._item_description = val

    @property
    def item_units(self):
        return self._item_units

    @item_units.setter
    def item_units(self, val):
        self._item_units = val

    def serialize(self):
        """
        serializes MeasurementMetadataType
        :return: MeasurementMetadataType dictionary
        """
        return {
            "itemDescription" : self.item_description,
            "itemUnits" : self.item_units,
            "siScaleCode" : self.si_scale_Code,
            "accumulationCharacteristic" : self.accumulation_characteristic,
            "dataQualifier" : self.data_qualifier,
            "measurementQuality" : self.measurement_quality,
            "resolution" : self.resolution
        }