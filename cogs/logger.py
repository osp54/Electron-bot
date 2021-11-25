import nextcord
from datetime import datetime

async def lloger(ctx,client,command,a=None):
    cch = nextcord.Client.get_channel(client,913446383187554324)
    g_name = str(ctx.guild.name)
    g_id = "`"+str(ctx.guild.id)+"`"
    au_name = str(ctx.message.author)
    au_id = "`"+str(ctx.message.author.id)+"`"
    ch_name = str(ctx.channel)
    ch_id = "`"+str(ctx.channel.id)+"`"
    logem = nextcord.Embed(title="Console log "+str(datetime.now()),color=0xE4B400)
    logem.add_field(name="Guild",value=g_name+" \n"+g_id)
    logem.add_field(name="Author",value=au_name+" \n"+au_id)
    logem.add_field(name="Channel",value=ch_name+" \n"+ch_id)
    logem.add_field(name="Commnd",value=command)
    if a == None:
        pass
    else:
        logem.add_field(name="Content",value=str(a),inline=False)
    await cch.send(embed=logem)