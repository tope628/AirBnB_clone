#!/usr/bin/python3
""" command module """
import cmd
import models
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

    def do_show(self, args):
        """ show string representation of an instance """
        list_args = args.split()
        all_objs = models.storage.all()
        print(list_args)
        if len(list_args) == 0:
            print("** class name missing **")
            return False
        if len(list_args) == 1 or list_args[1] is None:
            print("** instance id  missing **")
            return False
        try:
            key = list_args[0] +  "." + list_args[1]
            one_obj = all_objs[key]
            print(one_obj)
        except Exception as e:
            print(e)
        #except:
         #   print("** class doesn't exist **")









if __name__ == '__main__':
    HBNBCommand().cmdloop()
