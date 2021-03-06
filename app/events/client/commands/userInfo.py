import discord
from app.vars.client import client
from app.helpers import Notify


@client.command()
async def userInfo(ctx, Member: discord.Member = None):
    notify = Notify(ctx=ctx, title="User Info")
    notify.prepair()
    if not (Member):
        notify.error(content='No user has passed')
        return

    try:
        if (Member.bot):
            IsBot = '✔️'
        else:
            IsBot = '❌'

        if (Member.premium_since):
            Booster = '✔️'
        else:
            Booster = '❌'
            
        fields = [(f"User:", f'```{str(Member)}```', True),
                    ("ID:", f'```{Member.id}```', True),
                    ("Bot?", f'```{IsBot}```', True),
                    ("Status: ", f'```{str(Member.status).title()}```', True),
                    ("Activity:", f"```{str(Member.activity.type).split('.')[-1].title() if Member.activity else 'N/A'} {Member.activity.name if Member.activity else ''}```", True),
                    ("Created In:", f'```{Member.created_at.strftime("%d/%m/%Y")}```', True),
                    ("Joined In:", f'```{Member.joined_at.strftime("%d/%m/%Y")}```', True),
                    ("Booster?", f'```{Booster}```', True)]
        notify.fields(fields=fields)
    except Exception as e:
        notify.error(content=e)
