"""
Defines PowerReactiveType class
"""
from fsgim_meter.measurements.power_measurements.power_item_type import PowerItemType
from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType
from fsgim_meter.common_classes_enums.enumerations.enumerations import UnitSymbolKind


class PowerReactiveType(PowerItemType):


    @MeasurementMetadataType.item_description.setter
    def item_description(self, val):
        self._item_description = "ReactivePower"

    @MeasurementMetadataType.item_units.setter
    def item_units(self, val):
        self._item_units = UnitSymbolKind.get_code('var')