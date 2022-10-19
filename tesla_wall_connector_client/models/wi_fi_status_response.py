from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WiFiStatusResponse")


@attr.s(auto_attribs=True)
class WiFiStatusResponse:
    """
    Attributes:
        wifi_ssid (Union[Unset, str]):  Example: TXkgV2lGaQ==.
        wifi_signal_strength (Union[Unset, int]):  Example: 98.
        wifi_rssi (Union[Unset, int]):  Example: -41.
        wifi_snr (Union[Unset, int]):  Example: 51.
        wifi_connected (Union[Unset, bool]):
        wifi_infra_ip (Union[Unset, str]):
        internet (Union[Unset, bool]):
        wifi_mac (Union[Unset, str]):
    """

    wifi_ssid: Union[Unset, str] = UNSET
    wifi_signal_strength: Union[Unset, int] = UNSET
    wifi_rssi: Union[Unset, int] = UNSET
    wifi_snr: Union[Unset, int] = UNSET
    wifi_connected: Union[Unset, bool] = UNSET
    wifi_infra_ip: Union[Unset, str] = UNSET
    internet: Union[Unset, bool] = UNSET
    wifi_mac: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wifi_ssid = self.wifi_ssid
        wifi_signal_strength = self.wifi_signal_strength
        wifi_rssi = self.wifi_rssi
        wifi_snr = self.wifi_snr
        wifi_connected = self.wifi_connected
        wifi_infra_ip = self.wifi_infra_ip
        internet = self.internet
        wifi_mac = self.wifi_mac

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wifi_ssid is not UNSET:
            field_dict["wifi_ssid"] = wifi_ssid
        if wifi_signal_strength is not UNSET:
            field_dict["wifi_signal_strength"] = wifi_signal_strength
        if wifi_rssi is not UNSET:
            field_dict["wifi_rssi"] = wifi_rssi
        if wifi_snr is not UNSET:
            field_dict["wifi_snr"] = wifi_snr
        if wifi_connected is not UNSET:
            field_dict["wifi_connected"] = wifi_connected
        if wifi_infra_ip is not UNSET:
            field_dict["wifi_infra_ip"] = wifi_infra_ip
        if internet is not UNSET:
            field_dict["internet"] = internet
        if wifi_mac is not UNSET:
            field_dict["wifi_mac"] = wifi_mac

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wifi_ssid = d.pop("wifi_ssid", UNSET)

        wifi_signal_strength = d.pop("wifi_signal_strength", UNSET)

        wifi_rssi = d.pop("wifi_rssi", UNSET)

        wifi_snr = d.pop("wifi_snr", UNSET)

        wifi_connected = d.pop("wifi_connected", UNSET)

        wifi_infra_ip = d.pop("wifi_infra_ip", UNSET)

        internet = d.pop("internet", UNSET)

        wifi_mac = d.pop("wifi_mac", UNSET)

        wi_fi_status_response = cls(
            wifi_ssid=wifi_ssid,
            wifi_signal_strength=wifi_signal_strength,
            wifi_rssi=wifi_rssi,
            wifi_snr=wifi_snr,
            wifi_connected=wifi_connected,
            wifi_infra_ip=wifi_infra_ip,
            internet=internet,
            wifi_mac=wifi_mac,
        )

        wi_fi_status_response.additional_properties = d
        return wi_fi_status_response

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
