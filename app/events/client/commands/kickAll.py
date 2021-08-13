from discord.ext import commands
from app.vars.client import client
from app.helpers import notify
from app.helpers.notify import ConsoleLog

@client.command()
@commands.guild_only()
@commands.has_permissions(kick_members=True)
async def kickAll(ctx):
    AllowList = []
    for member in ctx.guild.members:
        if member.id != ctx.author.id:
            try:
                if not(member.id in AllowList):
                    await member.kick()
                    ConsoleLog(f'[{member.display_name}]: Has been kicked.')
                else:
                    ConsoleLog(f'[{member.display_name}]: Has been skipped.')
            except Exception as e:
                ConsoleLog(f'[Error]: {e.text}')
                pass
    else:
        await notify.success(ctx,f'All members successfully kicked')
