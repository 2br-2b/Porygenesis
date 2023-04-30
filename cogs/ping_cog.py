import discord
from discord.ext import tasks, commands
from discord import app_commands

# Listens for DMs to add to the story
class ping_cog(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        self.loop_tasks = [
            self.do_stuff_regularly
        ]
        
            
    @app_commands.guild_only()
    @app_commands.command(name="command_name")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def command_name(self, interaction: discord.Interaction):
        # if the command will take longer than 5 seconds to process, run this as the initial response
        # await interaction.response.defer()
        
        # For all responses past the first one (including if the first response is a deferral), make sure to run this code instead:
        # interaction.followup.send("stuff")
        
        await interaction.response.send_message("Pong!")
        pass
    
    
    @tasks.loop(hours = 1)
    async def do_stuff_regularly(self):
        """Runs regular maintenance on the server"""
        pass
            
            
    
    
    
    ###################################################################
    #### Regular maintenance stuff 
    ###################################################################
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Starting tasks")
        for task in self.loop_tasks:
            try:
                task.start()
            except RuntimeError as e:
                if not str(e) == "Task is already launched and is not completed.":
                    raise RuntimeError(str(e))

    def cog_unload(self):
        print("Stopping tasks")
        for task in self.loop_tasks:
            task.stop()
           
async def setup(bot):
    await bot.add_cog(ping_cog(bot))

