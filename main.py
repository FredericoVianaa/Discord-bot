import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Configurações dos canais
MENU_CHANNEL_ID = 1274486865650516081  # ID do canal onde o menu de reações estará
SUMMARY_CHANNEL_ID_JASON = 1274481661404512267  # ID do canal onde o resumo será enviado
SUMMARY_CHANNEL_ID_PRAGA = 1274481675774201917  # ID do canal onde o resumo será enviado

# Função para criar o menu de reações
async def create_menu(channel):
    menu_message = await channel.send("```Escolha uma reação para iniciar a coleta de informações. \n 🪓 = Jason \n ☢️ = Ameaça não identificada```")
    await menu_message.add_reaction("🪓")
    await menu_message.add_reaction("☢️")  # Reação para iniciar o formulário
    return menu_message

# Evento que dispara quando o bot está pronto
@bot.event
async def on_ready():
    menu_channel = bot.get_channel(MENU_CHANNEL_ID)
    global menu_message  # Definindo a mensagem do menu como global para que possa ser acessada em outras funções
    menu_message = await create_menu(menu_channel)
    print(f'Bot conectado como {bot.user}!')

# Evento que monitora as reações
@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    if reaction.message.channel.id == MENU_CHANNEL_ID and reaction.emoji == "🪓":
        await start_questionnaire_jason(reaction.message.channel, user)
    if reaction.message.channel.id == MENU_CHANNEL_ID and reaction.emoji == "☢️":
        await start_questionnaire_praga(reaction.message.channel, user)

# Função para iniciar o questionário
async def start_questionnaire_jason(channel, user):
    questions = [
        "Nome do Investigador:",
        "RG:",
        "Data do acontecimento:",
        "Nome dos envolvidos:",
        "Lugar:",
        "Relato:"
    ]
    answers = {}

    def check(m):
        return m.author == user and m.channel == channel

    try:
        summary_message = "Resumo do Relato:\n"
        for question in questions:
            await channel.send(f"```{question}```")
            msg = await bot.wait_for('message', check=check)
            answers[question] = msg.content
            summary_message += f"{question} {msg.content}\n"
            await msg.delete()  # Apaga a resposta do usuário
            async for message in channel.history(limit=1):
                if message.content.startswith("```"):
                    await message.delete()  # Apaga a pergunta

        # Envia o resumo para o canal de resumo
        summary_channel = bot.get_channel(SUMMARY_CHANNEL_ID_JASON)
        await summary_channel.send(f"```{summary_message}```")

        # Remove todas as reações e as adiciona novamente para resetar
        await menu_message.clear_reactions()
        await menu_message.add_reaction("🪓")
        await menu_message.add_reaction("☢️")
    except Exception as e:
        print(f"Erro: {e}")

async def start_questionnaire_praga(channel, user):
    questions = [
        "Nome do Investigador:",
        "RG:",
        "Data do acontecimento:",
        "Nome dos envolvidos:",
        "Lugar:",
        "Relato:"
    ]
    answers = {}

    def check(m):
        return m.author == user and m.channel == channel

    try:
        summary_message = "Resumo do Relato:\n"
        for question in questions:
            await channel.send(f"```{question}```")
            msg = await bot.wait_for('message', check=check)
            answers[question] = msg.content
            summary_message += f"{question} {msg.content}\n"
            await msg.delete()  # Apaga a resposta do usuário
            async for message in channel.history(limit=1):
                if message.content.startswith("```"):
                    await message.delete()  # Apaga a pergunta

        # Envia o resumo para o canal de resumo
        summary_channel = bot.get_channel(SUMMARY_CHANNEL_ID_PRAGA)
        await summary_channel.send(f"```{summary_message}```")

        # Remove todas as reações e as adiciona novamente para resetar
        await menu_message.clear_reactions()
        await menu_message.add_reaction("🪓")
        await menu_message.add_reaction("☢️")
    except Exception as e:
        print(f"Erro: {e}")

bot.run('SEU TOKEN')
