from app.commands import Command


class WelcomeCommand(Command):
    def execute(self):
        print("Welcome! Have a nice day")