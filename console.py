#!/usr/bin/python3
""" command module """
import cmd
from models.base_model import BaseModel

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

    def do_create(self, *args):
        """create new instance of BaseModel """
        if len(args[0]) == 0:
            print("** class name missing **")
            return False
        try:
            classname = args[0]
            new_obj = eval(classname)()
            new_obj.save()
            print(new_obj.id)
        except:
            print("** class doesn't exist **")








if __name__ == '__main__':
    HBNBCommand().cmdloop()
