import pytest


def test_repr_sensitive_dataclass(usual_dataclass):
    result = repr(usual_dataclass)

    assert result == "UsualDataclass(username='test', phone='88005553535')"
    assert usual_dataclass.password == 'secret'
    assert usual_dataclass.email == 'sensitive@info.com'


def test_class_with_explicit_defined_fields(dataclass_with_explicitly_defined_fields):
    result = repr(dataclass_with_explicitly_defined_fields)

    assert result == "DataclassWithExplicitlyDefinedFields(username='test')"
    assert dataclass_with_explicitly_defined_fields.password == 'default-password'


def test_frozen_dataclass_respectets_sensitive_type(frozen_dataclass):
    result = repr(frozen_dataclass)

    assert result == "FrozenDataclass(username='test')"
    assert frozen_dataclass.password == 'top-secret'


@pytest.mark.skip
def test_str_sensitive_dataclass():
    pass


@pytest.mark.skip
def test_sensitive_dataclass_traceback():
    pass


@pytest.mark.skip
def test_log_sensitive_dataclass():
    pass


@pytest.mark.skip
def test_class_inheritance():
    pass


@pytest.mark.skip
def test_sensitive_dataclass_with_no_annotations():
    pass
