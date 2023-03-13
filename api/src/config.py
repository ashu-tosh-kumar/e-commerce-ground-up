"""Contains the configuration variables for all application

- Why have we defined `__init__` method for `_Config`?
Because we don't want the config file to connect to external secrets manager the moment
we import it. That should happen only when we want it. Therefore, we should instantiate
the config class and then use it.
"""

import os
from typing import Type


class _Config:
    """Class containing all the configuration variables"""

    # Placeholders
    ENV = None

    def __init__(self) -> None:
        """Initializer for class `_Config`"""
        ## Add all common config variables below

        # logs
        self.LOGGER_LEVEL = os.getenv("logger_level") or "INFO"


class _ProductionConfig(_Config):
    ENV = "production"

    def __init__(self) -> None:
        """Initializer for `_ProductionConfig`"""
        super().__init__()

        ## Add all production variables below


class _TestingConfig(_Config):
    ENV = "testing"

    def __init__(self) -> None:
        """Initializer for `_TestingConfig`"""
        super().__init__()

        ## Add all testing variables below


class _DevelopmentConfig(_Config):
    ENV = "development"

    def __init__(self) -> None:
        """Initializer for `_DevelopmentConfig`"""
        super().__init__()

        ## Add all development variables below


class _LocalConfig(_Config):
    """`_LocalConfig` avoids Internet calls like to an external Secrets Manager"""

    ENV = "local"

    def __init__(self) -> None:
        """Initializer for `_LocalConfig`"""
        super().__init__()


_ENV_CONFIG_MAPPING: dict[str, Type[_ProductionConfig] | Type[_TestingConfig] | Type[_DevelopmentConfig] | Type[_LocalConfig]] = {
    "production": _ProductionConfig,
    "testing": _TestingConfig,
    "development": _DevelopmentConfig,
    "local": _LocalConfig,
}

_curr_env: str = os.getenv("env") or "development"

# Users should import below variable `Config` referencing the respective configuration class
config = _ENV_CONFIG_MAPPING[_curr_env]()
