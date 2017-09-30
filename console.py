#!/usr/bin/python3
""" command module """
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """ cmd class """
    prompt = '(hbnb)'

    def emptyline(self):
        """change empty line default behavior"""
        pass

    def do_EOF(self, arg):
        """ exit console """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True







if __name__ == '__main__':
    HBNBCommand().cmdloop()
