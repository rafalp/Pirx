# Pirx

Pirx is a project skeleton and a contract for applications built with [Starlette](https://www.starlette.io/) and 3rd party modules.


## Features

### Plugins

Primary feature that Pirx provides to application developers is a plugin system.

Plugins are just a Python packages that Pirx loads on application's start.


### Configuration

Like Django, Pirx uses Python module (usually named `settings`) for configuration. Loaded settings are available as attributes of `Settings` object, importable from `pirx.conf`:

```python
from pirx import setup
from pirx.conf import settings
from starlette.applications import Starlette


setup("myapp.settings")


app = Starlette(debug=settings.DEBUG, routes=[
    ...
])
```

By default Pirx specifies following settings:

- `ASGI_APP: str`: path to ASGI application instance in application's code.
- `DEBUGL: bool`: controls if the Application is running in debug mode or not.
- `PLUGINS: List[str]`: list of configured plugins.


### Management commands

Pirx skeleton provides `manage.py` Python file that can be used to run management commands in the project:

```console
$ python manage.py runserver
```

Plugin can implement custom management commands by defining `commands` python module:

```python
import click
from pirx.commands import cli


@cli.add_command
@click.command(short_help="Says hello world!")
def hello_world():
    click.echo("Hello world!")
```


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

Contracts are not limited to Python modules. Static files plugin could check other plugins for presence of "static" directories, and provide Starlette view that would discover and serve files located in those directories during dev:

```python
import os

from pirx.plugins import plugins


static_dirs = []
for plugin in plugins.get_plugins_with_directory("static"):
    static_dirs.append(os.path.join(plugin.get_path(), "static")
```
