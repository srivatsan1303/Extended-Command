from app.commands import Command


class ThankYouCommand(Command):
    def execute(self):
        print("Thanking you! have a great day")