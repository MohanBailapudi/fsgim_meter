"""
Defines PowerItemType class
"""

from fsgim_meter.measurements.measurement_metadata_type import MeasurementMetadataType

class PowerItemType(MeasurementMetadataType):

    def __init__(self):
        pass

    @property
    def item_description(self):
        return self.item_description

    @item_description.setter
    def item_description(self, val):
        self._itemDescription = val

    @property
    def item_units(self):
        return self.item_description

    @item_units.setter
    def item_units(self, val):
        self._item_units = val