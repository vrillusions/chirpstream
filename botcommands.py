#!/usr/bin/env python
# vim:ts=4:sw=4:ft=python:fileencoding=utf-8
"""Commands the bot can perform."""

class BotCommands():
    def __init__(self):
        # manually define available commands
        self.commands = ('help', 'echo')
    
    def _get_commands(self):
        result = None
        for cmd in self.commands:
            if result == None:
                result = cmd
            else:
                result = result + ', ' + cmd
        return result
    
    def help(self, args):
        return 'Available commands: ' + self._get_commands()
    
    def echo(self, args):
        return args