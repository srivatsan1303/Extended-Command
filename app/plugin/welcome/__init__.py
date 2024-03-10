from app.commands import Command
import logging


class WelcomeCommand(Command):
    def execute(self):
        logging.info("Welcome! Have a nice day")
        print("Welcome! Have a nice day")