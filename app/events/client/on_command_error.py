from app.vars.client import client
from app.filesystem import error as error_file
from app.helpers import Notify

@client.event
async def on_command_error(ctx, error):
    try:
        notify = Notify(ctx=ctx, title="Exception")
        notify.exception(content=error.args[0])
    except Exception as e:
        error_file(e)
        pass

