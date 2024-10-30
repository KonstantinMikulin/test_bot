from aiogram.types import BotCommand

# list of commands for main menu button
main_menu_commands = [
    BotCommand(command="/start", description="Start bot"),
    BotCommand(command="/weight", description="Add weight"),
    BotCommand(command="/stats", description="Statistics for admin"),
]
