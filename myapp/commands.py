import click
from pirx.commands import cli


@cli.add_command
@click.command(short_help="Says hello world!")
def hello_world():
    click.echo("Hello world!")
