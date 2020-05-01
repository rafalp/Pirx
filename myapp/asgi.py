from pirx import setup
from pirx.conf import settings
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


setup("myapp.settings")


async def homepage(request):
    return JSONResponse({'hello': 'World!'})


app = Starlette(debug=settings.DEBUG, routes=[
    Route('/', homepage),
])