import dataclasses

import pytest

from sensitive_dataclasses import sensitive_dataclass, SensitiveData


@sensitive_dataclass
class UsualDataclass:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData


@sensitive_dataclass
class DataclassWithExplicitlyDefinedFields:
    username: str
    password: SensitiveData = dataclasses.field(
        default='default-password',
    )


@sensitive_dataclass(frozen=True)
class FrozenDataclass:
    username: str
    password: SensitiveData


@pytest.fixture()
def usual_dataclass():
    return UsualDataclass(
        username='test',
        password='secret',
        phone='88005553535',
        email='sensitive@info.com',
    )


@pytest.fixture()
def dataclass_with_explicitly_defined_fields():
    return DataclassWithExplicitlyDefinedFields(
        username='test',
    )


@pytest.fixture()
def frozen_dataclass():
    return FrozenDataclass(
        username='test',
        password='top-secret',
    )
