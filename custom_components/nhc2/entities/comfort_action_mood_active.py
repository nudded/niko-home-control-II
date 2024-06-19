from homeassistant.components.binary_sensor import BinarySensorEntity

from ..nhccoco.devices.comfort_action import CocoComfortAction
from .nhc_entity import NHCBaseEntity


class Nhc2ComfortActionMoodActiveEntity(NHCBaseEntity, BinarySensorEntity):
    _attr_has_entity_name = True

    def __init__(self, device_instance: CocoComfortAction, hub, gateway):
        """Initialize a binary sensor."""
        super().__init__(device_instance, hub, gateway)

        self._attr_unique_id = device_instance.uuid + '_mood_active'

        self._attr_state = self._device.is_mood_active

    @property
    def name(self) -> str:
        return 'Start Active'

    @property
    def is_on(self) -> bool:
        return self._device.is_mood_active
