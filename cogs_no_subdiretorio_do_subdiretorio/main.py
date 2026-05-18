import discord
import os
import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Variável {name} não definida. Copie .env.example para .env e configure o valor."
        )
    return value


TOKEN = get_required_env("DISCORD_TOKEN")

try:
    server_id = discord.Object(id=int(get_required_env("GUILD_ID")))
except ValueError as exc:
    raise RuntimeError("GUILD_ID deve conter apenas números.") from exc

date = datetime.datetime.today()
now = date.strftime('%d-%m-%Y %H:%M:%S')

class MyClient(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Isso é necessário para usar comandos de texto
        super().__init__(
            command_prefix="!",
            intents=intents,
        )

    async def setup_hook(self):

        # Carrega todos os arquivos .py nos subdiretórios da pasta cogs
        cog_dir = './cogs'

        for dirname in os.listdir(cog_dir):
            module_dir = os.path.join(cog_dir, dirname)
            if not os.path.isdir(module_dir):
                continue

            for filename in os.listdir(module_dir):
                if filename.endswith('.py') and not filename.startswith('__'):
                    extension = f'cogs.{dirname}.{filename[:-3]}'
                    await self.load_extension(extension)
                    print(extension)

        self.tree.copy_global_to(guild=server_id)
        await self.tree.sync(guild=server_id) 

bot = MyClient()

@bot.event
async def on_ready():
    print(f"\033[1;34m{now}\033[1;34m INFO  \033[1;33m   {bot.user.name} \033[m está online! ✔️")


@bot.event
async def on_command_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.CommandNotFound):
        return

    raise error

bot.run(TOKEN)
