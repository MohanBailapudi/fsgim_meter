from fsgim_meter.measurements.item_base_type import ItemBaseType
class MeasurementMetadataType(ItemBaseType):
    """
    Defines Metadata associated with a measurement.
    """
    def __init__(self, itemDescription, itemUnits, siScaleCode, accumulationCharacteristic="", dataQualifier="",
                 description="", measurementQuality="", resolution=""):
        self.itemDescription = itemDescription
        self.itemUnits = itemUnits
        self.siScaleCode = siScaleCode
        self.accumulationCharacteristic = accumulationCharacteristic
        self.dataQualifier = dataQualifier
        self.description = description
        self.measurementQuality = measurementQuality
        self.resolution = resolution