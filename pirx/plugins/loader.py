import sys
from typing import List, Tuple
from types import ModuleType

from .plugin import Plugin


class PluginLoader:
    _plugins: List[Plugin]

    def __init__(self):
        self._plugins = []

    def load_plugins(self, plugin_list: List[str]) -> List[Plugin]:
        for plugin in plugin_list:
            self._plugins.append(Plugin(plugin))
        return self._plugins

    def import_modules_if_exists(
        self, module_name: str
    ) -> List[Tuple[str, ModuleType]]:
        modules = []
        for plugin in self._plugins:
            module = plugin.import_module_if_exists(module_name)
            if module:
                modules.append((plugin.module_name, module))

        return modules

    def get_plugins_with_directory(self, directory_name: str) -> List[Plugin]:
        plugins = []
        for plugin in self._plugins:
            if plugin.has_directory(directory_name):
                plugins.append(plugin)
        return plugins
