import discord
from discord.ext import commands
import youtube_dl
import os
from discord_components import DiscordComponents, Button, ButtonStyle

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    DiscordComponents(client)
    print("bot connected")

@client.command()
async def test(ctx):
    await ctx.send(content=None, tts=False, embed=None, file=None, files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)(
        embed=discord.Embed(title="ANAl:"),
        components=[
            Button(style=ButtonStyle.URL, label="Hate", url="https://funpay.ru/users/127065/"),
            Button(style=ButtonStyle.URL, label="CyberTm", url="https://funpay.ru/users/3020297/"),
            Button(style=ButtonStyle.URL, label="По вопросам", url="https://vk.com/alto_bro"),
            Button(style=ButtonStyle.URL, label="Ссылка на лоадер и инструкцию", url="https://disk.yandex.ru/i/mZUl3CIXWGlRCQ")
        ]
    )

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="🐔Ферма🐷")
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Бот не находиться в канале кишалов лох.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command()
async def clearr (ctx, amount = 0):
    await ctx.channel.purge(limit = amount);



client.run('NzEwMTM0MTk4NDEyOTAyNDMw.XrwCAg.Ayu2a5xTYwJw_5UdgDAM2W3rngs')