from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionResponse")


@attr.s(auto_attribs=True)
class VersionResponse:
    """
    Attributes:
        firmware_version (Union[Unset, str]):  Example: 22.23.0+gb7356e54a091bc.
        part_number (Union[Unset, str]):  Example: 1457768-02-G.
        serial_number (Union[Unset, str]):
    """

    firmware_version: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        firmware_version = self.firmware_version
        part_number = self.part_number
        serial_number = self.serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        firmware_version = d.pop("firmware_version", UNSET)

        part_number = d.pop("part_number", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        version_response = cls(
            firmware_version=firmware_version,
            part_number=part_number,
            serial_number=serial_number,
        )

        version_response.additional_properties = d
        return version_response

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
