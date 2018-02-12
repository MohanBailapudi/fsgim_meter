"""
Defines MeasurementmetadataType class
"""

from fsgim_meter.measurements.item_base_type import ItemBaseType


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
        self.item_units = item_units
        self.si_scale_Code = si_scale_code
        self.accumulation_characteristic = accumulation_characteristic
        self.data_qualifier = data_qualifier
        self.description = description
        self.measurement_quality = measurement_quality
        self.resolution = resolution


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