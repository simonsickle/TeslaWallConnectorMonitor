from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LifetimeResponse")


@attr.s(auto_attribs=True)
class LifetimeResponse:
    """
    Attributes:
        contactor_cycles (Union[Unset, int]):
        contactor_cycles_loaded (Union[Unset, int]):
        alert_count (Union[Unset, int]):
        thermal_foldbacks (Union[Unset, int]):
        avg_startup_temp (Union[Unset, float]):
        charge_starts (Union[Unset, int]):
        energy_wh (Union[Unset, int]):
        connector_cycles (Union[Unset, int]):
        uptime_s (Union[Unset, int]):
        charging_time_s (Union[Unset, int]):
    """

    contactor_cycles: Union[Unset, int] = UNSET
    contactor_cycles_loaded: Union[Unset, int] = UNSET
    alert_count: Union[Unset, int] = UNSET
    thermal_foldbacks: Union[Unset, int] = UNSET
    avg_startup_temp: Union[Unset, float] = UNSET
    charge_starts: Union[Unset, int] = UNSET
    energy_wh: Union[Unset, int] = UNSET
    connector_cycles: Union[Unset, int] = UNSET
    uptime_s: Union[Unset, int] = UNSET
    charging_time_s: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contactor_cycles = self.contactor_cycles
        contactor_cycles_loaded = self.contactor_cycles_loaded
        alert_count = self.alert_count
        thermal_foldbacks = self.thermal_foldbacks
        avg_startup_temp = self.avg_startup_temp
        charge_starts = self.charge_starts
        energy_wh = self.energy_wh
        connector_cycles = self.connector_cycles
        uptime_s = self.uptime_s
        charging_time_s = self.charging_time_s

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contactor_cycles is not UNSET:
            field_dict["contactor_cycles"] = contactor_cycles
        if contactor_cycles_loaded is not UNSET:
            field_dict["contactor_cycles_loaded"] = contactor_cycles_loaded
        if alert_count is not UNSET:
            field_dict["alert_count"] = alert_count
        if thermal_foldbacks is not UNSET:
            field_dict["thermal_foldbacks"] = thermal_foldbacks
        if avg_startup_temp is not UNSET:
            field_dict["avg_startup_temp"] = avg_startup_temp
        if charge_starts is not UNSET:
            field_dict["charge_starts"] = charge_starts
        if energy_wh is not UNSET:
            field_dict["energy_wh"] = energy_wh
        if connector_cycles is not UNSET:
            field_dict["connector_cycles"] = connector_cycles
        if uptime_s is not UNSET:
            field_dict["uptime_s"] = uptime_s
        if charging_time_s is not UNSET:
            field_dict["charging_time_s"] = charging_time_s

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contactor_cycles = d.pop("contactor_cycles", UNSET)

        contactor_cycles_loaded = d.pop("contactor_cycles_loaded", UNSET)

        alert_count = d.pop("alert_count", UNSET)

        thermal_foldbacks = d.pop("thermal_foldbacks", UNSET)

        avg_startup_temp = d.pop("avg_startup_temp", UNSET)

        charge_starts = d.pop("charge_starts", UNSET)

        energy_wh = d.pop("energy_wh", UNSET)

        connector_cycles = d.pop("connector_cycles", UNSET)

        uptime_s = d.pop("uptime_s", UNSET)

        charging_time_s = d.pop("charging_time_s", UNSET)

        lifetime_response = cls(
            contactor_cycles=contactor_cycles,
            contactor_cycles_loaded=contactor_cycles_loaded,
            alert_count=alert_count,
            thermal_foldbacks=thermal_foldbacks,
            avg_startup_temp=avg_startup_temp,
            charge_starts=charge_starts,
            energy_wh=energy_wh,
            connector_cycles=connector_cycles,
            uptime_s=uptime_s,
            charging_time_s=charging_time_s,
        )

        lifetime_response.additional_properties = d
        return lifetime_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
