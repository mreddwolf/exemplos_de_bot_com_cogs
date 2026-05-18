import discord
from discord.ext import commands
from discord import app_commands


class Ping(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Exemplo de comando com prefixo (!)
    @commands.command(name="oi")
    async def oi(self, ctx):
        await ctx.send("Olá, Wumpus! Este é um Prefix Command...")

    # Exemplo de comando com slash (/)
    @app_commands.command(name="ola", description="Responde com uma mensagem usando slash command.")
    async def ola(self, interaction: discord.Interaction):
        await interaction.response.send_message("Olá, Wumpus! Este é um Slash Command...")

    # Exemplo de comando híbrido (! ou /)
    @commands.hybrid_command(name="ping", description="Mostra a latência atual do bot.")
    async def ping(self, ctx: commands.Context) -> None:
        await ctx.send(f"⏱️ | `{round(self.bot.latency * 1000, 2)}ms!`")

    # Exemplo simples de comando útil sem transformar o projeto em um bot completo
    @commands.hybrid_command(name="servidor", description="Mostra um resumo simples do servidor.")
    async def servidor(self, ctx: commands.Context) -> None:
        if ctx.guild is None:
            await ctx.send("Este comando só funciona dentro de um servidor.")
            return

        member_count = ctx.guild.member_count or "não informado"
        await ctx.send(
            f"Servidor: **{ctx.guild.name}**\n"
            f"Membros: **{member_count}**\n"
            f"Canais de texto: **{len(ctx.guild.text_channels)}**"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(Ping(bot))
