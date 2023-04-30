import asyncio
import discord
from discord.ext import commands
from discord import app_commands
import logging
import time
import config

intents = discord.Intents.default()
intents.guilds = True

class Porygenesis_Bot(commands.Bot):
    async def setup_hook(self):
        
        await load_cogs(self, ["cogs.ping_cog"])
        asyncio.create_task(bot.tree.sync())
        
        
bot = Porygenesis_Bot(command_prefix=config.PREFIX, intents=intents)


@bot.event
async def on_ready():
    print("Bot started!")

async def on_tree_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        return await interaction.response.send_message(f"Command is currently on cooldown! Try again in {error.retry_after}s.", ephemeral=True)

    elif isinstance(error, app_commands.MissingPermissions):
        return await interaction.response.send_message("You're missing the proper permissions!", ephemeral=True)
        
    else:
        raise error

async def load_cogs(bot: commands.Bot, cog_list: list):
    for cog_name in cog_list:
        try:
            await bot.load_extension(cog_name)
        except commands.errors.ExtensionNotFound:
            print(cog_name + " cog not found")
        except commands.errors.ExtensionAlreadyLoaded:
            pass
        except commands.errors.NoEntryPointError:
            print("Put the setup() function back in " + cog_name)

handler = logging.FileHandler(filename=f'logs/{int(time.time())} discord.log', encoding='utf-8', mode='w')

bot.tree.on_error = on_tree_error
bot.run(config.TOKEN, log_handler=handler)