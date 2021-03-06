import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore, error


@client.command(aliases=['removeallchannels', 'deleteChannels'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def deleteAllChannels(ctx, *, channelType: str.lower = ''):
    notify = Notify(ctx=ctx, title ='Deleting All Channels...')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    if(channelType == 'text'):
        type = ctx.guild.text_channels
    elif(channelType == 'voice'):
        type = ctx.guild.voice_channels
    elif(channelType == 'category'):
        type = ctx.guild.categories
    elif(channelType == 'all'):
        type = ctx.guild.channels
    else:
        notify.error(content='Not provided channel type:\n Text | Voice | Category | All')
        return

    for channel in type:
        try:
            await channel.delete()
            await asyncio.sleep(0.33)
        except Exception as e:
            error(e)
            pass        
    else:
        if(channelType != 'all'):
            notify.success(content=f'Successful deleted {channelType} channels')    