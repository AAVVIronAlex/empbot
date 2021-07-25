from importlib import import_module
from emp import bot
from emp.modules import ALL_MODULES


for module_name in ALL_MODULES:
    imported_module = import_module("emp.modules." + module_name)


print("EMP Bot is running!")

bot.polling()
