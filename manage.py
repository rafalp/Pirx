from pirx import setup
from pirx.commands import cli


if __name__ == "__main__":
    setup("myapp.settings")
    cli()
