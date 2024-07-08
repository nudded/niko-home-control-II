from homeassistant.components.sensor import SensorEntity, SensorDeviceClass

from ..nhccoco.devices.easee_chargingstation import CocoEaseeChargingstation
from .nhc_entity import NHCBaseEntity


class Nhc2EaseeChargingstationEvStatusEntity(NHCBaseEntity, SensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoEaseeChargingstation, hub, gateway):
        """Initialize a sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_ev_status'

        self._attr_device_class = SensorDeviceClass.ENUM
        self._attr_options = self._device.possible_ev_status
        self._attr_native_value = self._device.ev_status

    @property
    def name(self) -> str:
        return 'EV Status'

    @property
    def state(self) -> str:
        return self._device.ev_status
