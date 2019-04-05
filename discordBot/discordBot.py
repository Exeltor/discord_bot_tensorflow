import discord

TOKEN = 'NTYzNTEzNTQwODA0MzQ1ODc2.XKadAg.j978dZcbPspY6zrtxQ_XGZQIvUs'

client = discord.Client()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!mostro"):
        msg = 'Que pasa titan {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith("!yt"):
        msg = 'Temazo'.format(message)
        await client.send_message(message.channel, msg)
        await yt(message.author, message.content)

    if message.content.startswith("!rip"):

        voice_client = client.voice_client_in(message.author.server)
        if voice_client:
            await voice_client.disconnect()
            print("Bot left the voice channel")
        else:
            print("Bot was not in channel")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


async def yt(author, url):
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

    url = url.strip('!yt ')
    player = await vc.create_ytdl_player(url)
    # player.setVolume(100)
    player.start()


client.run(TOKEN)
