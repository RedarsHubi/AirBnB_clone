#!/usr/bin/python3
"""Module for HBNBCommand class"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Line Interpreter"""

    prompt = "(hbnb) "
    all_classes = {"BaseModel"}

    def do_quit(self, args):
        """Quits program"""
        return True

    def do_EOF(self, line):
        """ Quits program """
        return True

    def emptyline(self):
        """does not execute anything"""
        pass

    def do_create(self, args):
        """creates an instance of a  class"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            B = eval(args)()
            storage.save()
            print(B.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

