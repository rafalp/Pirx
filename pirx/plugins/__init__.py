from ..conf import settings
from .loader import PluginLoader


plugins = PluginLoader(settings.enabled_plugins)


for module in ("main", "commands"):
    plugins.import_modules_if_exists(module)
