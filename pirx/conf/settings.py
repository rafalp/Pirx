import importlib
import os

from types import ModuleType
from typing import Any, Dict, List, Optional


class Settings:
    ASGI_APP: str
    DEBUG: bool
    PLUGINS: List[str]

    _settings: Optional[ModuleType] = None
    _overrides: Optional[Dict[str, Any]] = None

    @property
    def IN_TEST(self) -> bool:
        return False

    def __getattr__(self, setting: str) -> Any:
        if self._overrides and setting in self._overrides:
            return self._overrides[setting]

        if self._settings is None:
            raise RuntimeError("Settings must be loaded before they can be accessed.")
        
        try:
            return getattr(self._settings, setting)
        except AttributeError:
            raise AttributeError(f"'{setting}' setting is not defined.")

    def load_settings(self, settings_module: str):
        if not settings_module:
            raise RuntimeError(f"'settings_module' is not set.")
        self._settings = importlib.import_module(settings_module)
