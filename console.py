#!/usr/bin/python3
"""Module for HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits program"""

        return True

    def do_EOF(self, line):
        """ Quits program """
        return True

    def emptyline(self):
        """does not execute anything"""
        pass

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()

