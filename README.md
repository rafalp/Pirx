# Pirx

Pirx is a project skeleton and a contract for applications built with ASGI frameworks like [Starlette](https://www.starlette.io/) and 3rd party modules.


## Pirx is not a framework

By itself Pirx doesn't implement any features required to implement web applications. It doesn't provide HTTP request handling, routing, sessions or other features like this.

Instead, Pirx is a contract enabling developers of ASGI web applications and libraries to work together. To this end, Pirx provides the glue code for basic and common tasks that most web applications have to realize:

- Loading configuration
- Separating features into modules ("plugins")
- Running console commands

It also provides a cookie cutter project template built with [Starlette](https://www.starlette.io/).


## Loading configuration

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
- `DEBUG: bool`: controls if the Application is running in debug mode or not.
- `IN_TEST: bool`: set to `True` if Pirx is running in test mode.
- `PLUGINS: List[str]`: list of configured plugins.


## Plugins

Primary feature that Pirx provides to the application developers is a plugin system.

Plugins are a python modules that Pirx loads on application's start, providing a clear entry point and a way for library developers to access the configuration, validate it and run initialization logic of their features.

For example, an ORM library could access the configuration and check if it contains database connection settings. It could then create an database connection object.


## Management commands

Pirx skeleton provides the `manage.py` Python file that can be used to run management commands in the project:

```console
$ python manage.py runserver
```

Plugins can implement custom management commands by defining `commands` python module:

```python
import click
from pirx.commands import cli


@cli.add_command
@click.command(short_help="Says hello world!")
def hello_world():
    click.echo("Hello world!")
```


## Introducing new contracts

Plugins can introduce new contracts that applications and other plugins can then use. The ORM plugin could load "models" modules from other plugins, provide new fixtures to test runner and add new management commands to `manage.py`.

To load `models` modules and do something with them, `ORM` plugin could run following code in its `main.py`:

```python
from pirx.plugins import plugins

from .modelsregistry import register_models


models = plugins.import_modules_if_exists("models")
# models will be a list of (name: str, module: ModuleType) tuples
register_models(models)
```

Contracts are not limited to Python modules. Static files plugin could check other plugins for presence of "static" directories, and provide ASGI app that would discover and serve files located in those directories during dev:

```python
import os

from pirx.plugins import plugins


static_dirs = []
for plugin in plugins.get_plugins_with_directory("static"):
    static_dirs.append(os.path.join(plugin.get_path(), "static")
```
