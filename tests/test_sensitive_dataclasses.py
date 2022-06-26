import dataclasses
import pytest

from sensitive_dataclasses import SensitiveData, sensitive_dataclass


@sensitive_dataclass
class UsualDataclass:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData


@sensitive_dataclass
class DataclassWithExplicitlyDefinedFields:
    username: str
    phone: str
    email: SensitiveData
    password: SensitiveData = dataclasses.field(
        default='default-password',
    )


@sensitive_dataclass(frozen=True)
class FrozenDataclass:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData


@sensitive_dataclass
class InheritedDataclass(UsualDataclass):
    bank_card: SensitiveData
    comment: str


def get_parametrization():
    return [
        (
            UsualDataclass(
                username='test',
                password='secret',
                phone='88005553535',
                email='sensitive@info.com',
            ),
            "UsualDataclass(username='test', phone='88005553535')",
        ),
        (
            DataclassWithExplicitlyDefinedFields(
                username='test',
                password='secret',
                phone='88005553535',
                email='sensitive@info.com',
            ),
            "DataclassWithExplicitlyDefinedFields(username='test', phone='88005553535')",
        ),
        (
            FrozenDataclass(
                username='test',
                password='secret',
                phone='88005553535',
                email='sensitive@info.com',
            ),
            "FrozenDataclass(username='test', phone='88005553535')",
        ),
        (
            InheritedDataclass(
                username='test',
                password='secret',
                phone='88005553535',
                email='sensitive@info.com',
                bank_card='bank_card_info',
                comment='test comment',
            ),
            "InheritedDataclass(username='test', phone='88005553535', comment='test comment')",
        ),
    ]


@pytest.mark.parametrize(
    ('dataclass', 'expected_repr'),
    get_parametrization()
)
def test_repr_with_sensitive_data(dataclass, expected_repr):
    assert repr(dataclass) == expected_repr
    assert dataclass.password == 'secret'
    assert dataclass.email == 'sensitive@info.com'


@pytest.mark.parametrize(
    ('dataclass', 'expected_str'),
    get_parametrization()
)
def test_str_sensitive_dataclass(dataclass, expected_str):
    assert str(dataclass) == expected_str
    assert dataclass.password == 'secret'
    assert dataclass.email == 'sensitive@info.com'
