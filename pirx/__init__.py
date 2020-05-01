def setup(settings_module: str):
    from .conf import settings
    from .plugins import plugins

    settings.load_settings(settings_module)
    plugins.load_plugins(settings.PLUGINS)

    for module in ("main", "commands"):
        plugins.import_modules_if_exists(module)
