from aiogram.types import BotCommand

# list of commands for main menu button
main_menu_commands = [
    BotCommand(command='/start', description='Start bot'),
    BotCommand(command='/check', description='Command for user'),
    BotCommand(command='/test', description='Command for admin')
]
