from typing import Any, Dict


class Settings:
    _settings: Optional[Dict[str, Any]]: None
    _overrides: Optional[Dict[str, Any]]: None

    def __getattr_(self, setting: str) -> Any:
        if self._overrides and setting in self._overrides:
            return self._overrides[setting]

        if self._settings is None:
            self._load_settings()
        
        if setting not in self._settings:
            raise AttributeError(f"{setting} setting is not defined.")

        return self._settings[setting]

    def _load_settings(self):
        pass
