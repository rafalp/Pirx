import click
from uvicorn.main import run

from .conf import settings


@click.group()
def cli():
    pass


@cli.add_command
@click.command(short_help="Runs development server with Uvicorn")
def runserver():
    run(
        settings.ASGI_APP,
        debug=settings.DEBUG,
        reload=True,
    )

