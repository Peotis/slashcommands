import discord
from discord.ext import commands
from discord import app_commands
from setting import settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='m', intents=intents)

@bot.event
async def on_ready():
    guild = discord.Object(id="Your_Guild_Id")  # Replace with your guild ID
    await bot.tree.sync(guild=guild)
    print(f'We have logged in as {bot.user} and synced commands to guild: {guild.id}')

# Define the testfunction command without any parameters
@bot.tree.command(name="testfunction", description="Test the bot's functionality with a slash command")
async def testfunction(interaction: discord.Interaction):
    # Send response visible to everyone
    await interaction.response.send_message("This is just a test function for slash commands!")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"Error in event {event}: {args} {kwargs}")

# Run the bot with the token from the settings
bot.run(settings['Token'])
