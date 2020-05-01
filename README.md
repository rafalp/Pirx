# Pirx

Pirx is a project skeleton and a contract for applications built with [Starlette](https://www.starlette.io/).


## Features

### Configuration


### Plugins

Primary feature that Pirx provides to application developers is a plugin system.

Plugins are just a Python packages that Pirx loads on application's start.


### Management commands


### Tests runner


## Introducing new contracts

Plugins can introduce new contracts for other plugins to use. For example, the ORM plugin could load "models" modules in other plugins, provide new fixtures to test runner and add new management commands to `manage.py`.

To load `models` modules and do something with them, `ORM` plugin could run following code in its `main.py`:

```python
from pirx.plugins import plugins

from .modelsregistry import register_models


models = plugins.import_modules_if_exists("models")
register_models(models)

```

