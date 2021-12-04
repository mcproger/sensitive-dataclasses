import pytest
import dataclasses

from sensitive_dataclasses import sensitive_dataclass, SensitiveData


@sensitive_dataclass
class TestClass:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData


@sensitive_dataclass
class TestClassWithExplicitFields:
    username: str
    password: SensitiveData = dataclasses.field(
        default='default-password',
    )


@pytest.fixture()
def test_dataclass():
    return TestClass(
        username='test',
        password='secret',
        phone='88005553535',
        email='sensitive@info.com',
    )


@pytest.fixture()
def test_class_with_explicit_fields():
    return TestClassWithExplicitFields(
        username='test',
    )


def test_repr_sensitive_dataclass(test_dataclass):
    result = repr(test_dataclass)

    assert result == "TestClass(username='test', phone='88005553535')"


def test_class_with_explicit_defined_fields(test_class_with_explicit_fields):
    result = repr(test_class_with_explicit_fields)

    assert result == "TestClassWithExplicitFields(username='test')"
    assert test_class_with_explicit_fields.password == 'default-password'


def test_sensitive_dataclass_with_decorator_arguments():
    pass


def test_str_sensitive_dataclass():
    pass


def test_sensitive_dataclass_traceback():
    pass


def test_log_sensitive_dataclass():
    pass


def test_class_inheritance():
    pass


def test_sensitive_dataclass_with_no_annotations():
    pass
