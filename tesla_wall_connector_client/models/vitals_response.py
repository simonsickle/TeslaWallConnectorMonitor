from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VitalsResponse")


@attr.s(auto_attribs=True)
class VitalsResponse:
    """
    Attributes:
        contactor_closed (Union[Unset, bool]):
        vehicle_connected (Union[Unset, bool]):
        session_s (Union[Unset, int]):  Example: 10718.
        grid_v (Union[Unset, float]):  Example: 236.4.
        grid_hz (Union[Unset, float]):  Example: 59.689.
        vehicle_current_a (Union[Unset, float]):  Example: 48.6.
        current_a_a (Union[Unset, float]):  Example: 22.3.
        current_b_a (Union[Unset, float]):  Example: 26.3.
        current_c_a (Union[Unset, float]):  Example: 25.9.
        current_n_a (Union[Unset, float]):  Example: 22.7.
        voltage_a_v (Union[Unset, float]):  Example: 240.5.
        voltage_b_v (Union[Unset, float]):  Example: 240.9.
        voltage_c_v (Union[Unset, float]):  Example: 118.6.
        relay_coil_v (Union[Unset, float]):  Example: 6.1.
        pcba_temp_c (Union[Unset, float]):  Example: 66.8.
        handle_temp_c (Union[Unset, float]):  Example: 39.1.
        mcu_temp_c (Union[Unset, float]):  Example: 52.8.
        uptime_s (Union[Unset, int]):
        input_thermopile_uv (Union[Unset, int]):  Example: -2005.
        prox_v (Union[Unset, float]):  Example: 1.5.
        pilot_high_v (Union[Unset, float]):
        pilot_low_v (Union[Unset, float]):
        session_energy_wh (Union[Unset, float]):
        config_status (Union[Unset, int]):
        evse_state (Union[Unset, int]):
        current_alerts (Union[Unset, List[str]]):
    """

    contactor_closed: Union[Unset, bool] = UNSET
    vehicle_connected: Union[Unset, bool] = UNSET
    session_s: Union[Unset, int] = UNSET
    grid_v: Union[Unset, float] = UNSET
    grid_hz: Union[Unset, float] = UNSET
    vehicle_current_a: Union[Unset, float] = UNSET
    current_a_a: Union[Unset, float] = UNSET
    current_b_a: Union[Unset, float] = UNSET
    current_c_a: Union[Unset, float] = UNSET
    current_n_a: Union[Unset, float] = UNSET
    voltage_a_v: Union[Unset, float] = UNSET
    voltage_b_v: Union[Unset, float] = UNSET
    voltage_c_v: Union[Unset, float] = UNSET
    relay_coil_v: Union[Unset, float] = UNSET
    pcba_temp_c: Union[Unset, float] = UNSET
    handle_temp_c: Union[Unset, float] = UNSET
    mcu_temp_c: Union[Unset, float] = UNSET
    uptime_s: Union[Unset, int] = UNSET
    input_thermopile_uv: Union[Unset, int] = UNSET
    prox_v: Union[Unset, float] = UNSET
    pilot_high_v: Union[Unset, float] = UNSET
    pilot_low_v: Union[Unset, float] = UNSET
    session_energy_wh: Union[Unset, float] = UNSET
    config_status: Union[Unset, int] = UNSET
    evse_state: Union[Unset, int] = UNSET
    current_alerts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contactor_closed = self.contactor_closed
        vehicle_connected = self.vehicle_connected
        session_s = self.session_s
        grid_v = self.grid_v
        grid_hz = self.grid_hz
        vehicle_current_a = self.vehicle_current_a
        current_a_a = self.current_a_a
        current_b_a = self.current_b_a
        current_c_a = self.current_c_a
        current_n_a = self.current_n_a
        voltage_a_v = self.voltage_a_v
        voltage_b_v = self.voltage_b_v
        voltage_c_v = self.voltage_c_v
        relay_coil_v = self.relay_coil_v
        pcba_temp_c = self.pcba_temp_c
        handle_temp_c = self.handle_temp_c
        mcu_temp_c = self.mcu_temp_c
        uptime_s = self.uptime_s
        input_thermopile_uv = self.input_thermopile_uv
        prox_v = self.prox_v
        pilot_high_v = self.pilot_high_v
        pilot_low_v = self.pilot_low_v
        session_energy_wh = self.session_energy_wh
        config_status = self.config_status
        evse_state = self.evse_state
        current_alerts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.current_alerts, Unset):
            current_alerts = self.current_alerts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contactor_closed is not UNSET:
            field_dict["contactor_closed"] = contactor_closed
        if vehicle_connected is not UNSET:
            field_dict["vehicle_connected"] = vehicle_connected
        if session_s is not UNSET:
            field_dict["session_s"] = session_s
        if grid_v is not UNSET:
            field_dict["grid_v"] = grid_v
        if grid_hz is not UNSET:
            field_dict["grid_hz"] = grid_hz
        if vehicle_current_a is not UNSET:
            field_dict["vehicle_current_a"] = vehicle_current_a
        if current_a_a is not UNSET:
            field_dict["currentA_a"] = current_a_a
        if current_b_a is not UNSET:
            field_dict["currentB_a"] = current_b_a
        if current_c_a is not UNSET:
            field_dict["currentC_a"] = current_c_a
        if current_n_a is not UNSET:
            field_dict["currentN_a"] = current_n_a
        if voltage_a_v is not UNSET:
            field_dict["voltageA_v"] = voltage_a_v
        if voltage_b_v is not UNSET:
            field_dict["voltageB_v"] = voltage_b_v
        if voltage_c_v is not UNSET:
            field_dict["voltageC_v"] = voltage_c_v
        if relay_coil_v is not UNSET:
            field_dict["relay_coil_v"] = relay_coil_v
        if pcba_temp_c is not UNSET:
            field_dict["pcba_temp_c"] = pcba_temp_c
        if handle_temp_c is not UNSET:
            field_dict["handle_temp_c"] = handle_temp_c
        if mcu_temp_c is not UNSET:
            field_dict["mcu_temp_c"] = mcu_temp_c
        if uptime_s is not UNSET:
            field_dict["uptime_s"] = uptime_s
        if input_thermopile_uv is not UNSET:
            field_dict["input_thermopile_uv"] = input_thermopile_uv
        if prox_v is not UNSET:
            field_dict["prox_v"] = prox_v
        if pilot_high_v is not UNSET:
            field_dict["pilot_high_v"] = pilot_high_v
        if pilot_low_v is not UNSET:
            field_dict["pilot_low_v"] = pilot_low_v
        if session_energy_wh is not UNSET:
            field_dict["session_energy_wh"] = session_energy_wh
        if config_status is not UNSET:
            field_dict["config_status"] = config_status
        if evse_state is not UNSET:
            field_dict["evse_state"] = evse_state
        if current_alerts is not UNSET:
            field_dict["current_alerts"] = current_alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contactor_closed = d.pop("contactor_closed", UNSET)

        vehicle_connected = d.pop("vehicle_connected", UNSET)

        session_s = d.pop("session_s", UNSET)

        grid_v = d.pop("grid_v", UNSET)

        grid_hz = d.pop("grid_hz", UNSET)

        vehicle_current_a = d.pop("vehicle_current_a", UNSET)

        current_a_a = d.pop("currentA_a", UNSET)

        current_b_a = d.pop("currentB_a", UNSET)

        current_c_a = d.pop("currentC_a", UNSET)

        current_n_a = d.pop("currentN_a", UNSET)

        voltage_a_v = d.pop("voltageA_v", UNSET)

        voltage_b_v = d.pop("voltageB_v", UNSET)

        voltage_c_v = d.pop("voltageC_v", UNSET)

        relay_coil_v = d.pop("relay_coil_v", UNSET)

        pcba_temp_c = d.pop("pcba_temp_c", UNSET)

        handle_temp_c = d.pop("handle_temp_c", UNSET)

        mcu_temp_c = d.pop("mcu_temp_c", UNSET)

        uptime_s = d.pop("uptime_s", UNSET)

        input_thermopile_uv = d.pop("input_thermopile_uv", UNSET)

        prox_v = d.pop("prox_v", UNSET)

        pilot_high_v = d.pop("pilot_high_v", UNSET)

        pilot_low_v = d.pop("pilot_low_v", UNSET)

        session_energy_wh = d.pop("session_energy_wh", UNSET)

        config_status = d.pop("config_status", UNSET)

        evse_state = d.pop("evse_state", UNSET)

        current_alerts = cast(List[str], d.pop("current_alerts", UNSET))

        vitals_response = cls(
            contactor_closed=contactor_closed,
            vehicle_connected=vehicle_connected,
            session_s=session_s,
            grid_v=grid_v,
            grid_hz=grid_hz,
            vehicle_current_a=vehicle_current_a,
            current_a_a=current_a_a,
            current_b_a=current_b_a,
            current_c_a=current_c_a,
            current_n_a=current_n_a,
            voltage_a_v=voltage_a_v,
            voltage_b_v=voltage_b_v,
            voltage_c_v=voltage_c_v,
            relay_coil_v=relay_coil_v,
            pcba_temp_c=pcba_temp_c,
            handle_temp_c=handle_temp_c,
            mcu_temp_c=mcu_temp_c,
            uptime_s=uptime_s,
            input_thermopile_uv=input_thermopile_uv,
            prox_v=prox_v,
            pilot_high_v=pilot_high_v,
            pilot_low_v=pilot_low_v,
            session_energy_wh=session_energy_wh,
            config_status=config_status,
            evse_state=evse_state,
            current_alerts=current_alerts,
        )

        vitals_response.additional_properties = d
        return vitals_response

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
