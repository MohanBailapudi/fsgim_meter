"""
Defines PowerRealType class
"""
from fsgim_meter.measurements.power_measurements.power_item_type import PowerItemType
from FSGIM.Mesaurements.enums import UnitSymbolKind


class PowerRealType(PowerItemType):

    def __init__(self,item_description, item_units, si_scale_code, accumulation_characteristic="", data_qualifier="",description="", measurement_quality="", resolution=""):

        super().__init__(item_description, item_units, si_scale_code, accumulation_characteristic, data_qualifier,description, measurement_quality, resolution)

    @PowerItemType.item_description.setter
    def item_description(self, val):
        self._itemDescription = "RealPower"

    @PowerItemType.item_units.setter
    def item_units(self, val):
        self._item_units =