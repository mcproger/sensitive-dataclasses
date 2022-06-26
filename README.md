# Sensitive dataclasses

[![Build Status](https://github.com/mcproger/sensitive-dataclasses/workflows/test/badge.svg?branch=master&event=push)](https://github.com/mcproger/sensitive-dataclasses/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/mcproger/sensitive-dataclasses/branch/master/graph/badge.svg)](https://codecov.io/gh/mcproger/sensitive-dataclasses)

An enhancement for the original python `@dataclass` decorator to prevent sensitive data leaks in logs, tracebacks, etc.

*It is in the early developlemnt stage*

## Why?

If you are using [dataclasses](https://docs.python.org/3/library/dataclasses.html) as containers for your ORM data,
DTOs, value objects or something like that, you could have an issue with sensitive data leaks in logging/monitoring systems (like Sentry), when the system logs your data containers that contain user's sensitive data
This package helps to prevent such an issue.

For example, let take a simple use case:

```python3
import dataclasses
import sentry_sdk

sentry_sdk.init(
    dsn='<your-sentry-dsn>',
)


@dataclasses.dataclass
class MyClass:
    username: str
    int_field: int
    str_field: str


m = MyClass(
    username='another_test',
    int_field=100600,
    str_field='another_test',
)


def run(m: MyClass):
    # produces a TypeError exception to Sentry
    m.int_field + m.str_field

run(m)
```

this code snippet will produce an error to Sentry, and Sentry will log all the fields.

![example1](https://raw.githubusercontent.com/mcproger/sensitive-dataclasses/master/docs/example1.png)

But what if one of the fields contains something, that we won't to be logged?

We can use the type extension and the decorator to prevent this case:

```python3
import sentry_sdk
from sensitive_dataclasses import sensitive_dataclass, SensitiveData


sentry_sdk.init(
    dsn='<your-sentry-dsn>',
)


@sensitive_dataclass
class MyClass:
    username: str
    int_field: int
    str_field: SensitiveData


m = MyClass(
    username='one_more_test',
    int_field=100700,
    str_field='one_more_test',
)


def run(m: MyClass):
    # produces a TypeError exception to Sentry
    m.int_field + m.str_field

run(m)
```

![example2](https://raw.githubusercontent.com/mcproger/sensitive-dataclasses/master/docs/example2.png)

This also will work for logging, debug prints and reprs.

## Example

Just import the decorator and the extended type and use it like a usual `@dataclass` decrorator with type annotations.

```python3
from sensitive_dataclasses import sensitive_dataclass


@sensitive_dataclass
class User:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData

```

It also works with the explicitly defined dataclass fields:

```python3
from sensitive_dataclasses import sensitive_dataclass


@sensitive_dataclass
class User:
    username: str
    phone: str
    email: SensitiveData
    password: SensitiveData = dataclasses.field(
        default='default-value',
    )

```

and supports the original decorator arguments:

```python3
from sensitive_dataclasses import sensitive_dataclass


@sensitive_dataclass(frozen=True)
class User:
    username: str
    password: SensitiveData
    phone: str
    email: SensitiveData

```

## Installation

TODO
