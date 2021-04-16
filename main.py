import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "#", description = "Budget Bot pour calculer votre budget")

@bot.event
async def on_ready():
    print("Bot démarré avec succés !")
    await bot.change_presence(activity=discord.Game(name="dit moi ton budget avec #budget (ton budget) !"))

@bot.command()
async def coucou(ctx):
	await ctx.send("ici on dit pas coucou on dit OUHO !")

@bot.command()
async def ouho(ctx):
	await ctx.send("OUHO !")

@bot.command()
async def bonjour(ctx):
	await ctx.send("Bonjour ! :wave:")

@bot.command()
async def zebi(ctx):
	await ctx.send("Zebi la mouche ! :call_me:")

@bot.command()
async def fdp(ctx):
	await ctx.send("Ta mère ! :middle_finger_tone1:")

@bot.command()
async def repeat(ctx, *texte):
	await ctx.send(" ".join(texte))

@bot.command()
async def style(ctx, *text):
	chineseChar = "丹书ㄈ力已下呂廾工丿片乚爪ㄇ口尸厶尺ㄎ丁凵人山父了乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))

@bot.command()
async def clear(ctx, nombre : int):
    await ctx.channel.purge(limit = nombre + 1)

@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f"{member} à été kick avec succés avec comme raison: {reason}")
	print(f"{member} à été kick pour la raison: {reason}")

@bot.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f"{member} à été unban avec succés")
			return
	await ctx.send(f"{member} n'est pas dans la liste de bans")

		


@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f"{member} à été banni avec succés avec comme raison: {reason}")
	print(f"{member} à été banni pour la raison: {raison}")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Muted")

		for channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

	await member.add_roles(mutedRole, reason=reason)
	await ctx.send(f"{member} à été mute avec succés avec comme raison: {reason}")
	await member.send(f"Vous avez été mute dans le serveur Pc server pour comme raison {reason}. Réfléchissez la prochaine fois...")
	await member.remove_roles(memberRole)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
	mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
	memberRole = discord.utils.get(ctx.guild.roles, name="Membre")

	await member.remove_roles(mutedRole)
	await member.add_roles(memberRole)
	await ctx.send(f"{member} à été unmute")
	await member.send(f"Vous avez été unmute du server Pc server")

@bot.command()
async def serverinfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Ce serveur ({serverName}) contient {numberOfPerson} personnes. \n La description du serveur {serverName} est: {serverDescription}. \n Ce serveur possède {numberOfTextChannels} salons écrit ainsi que {numberOfVoiceChannels} vocaux"
	await ctx.send(message)





bot.run("ODMxNjAwMDI3MTM4MTI5OTIw.YHXl4A.a8c3kv62hAwOvMYLeaWtgLxW8K8")

#ĄBĆÐËFǴĦİĴĶĻMŃǪPQŔŠŤŲVŴXŶŹ

