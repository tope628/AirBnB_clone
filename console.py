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
        if list_args[0]  in all_objs:
            if len(list_args) > 1:
                key = list_args[0] +  "." + list_args[1]
                if key in all_objs:
                    one_obj = all_objs[key]
                    print(one_obj)
                else:
                    print("** no instance found **")
            else:
                print("** instance id  missing **")
        else:
            print("** class doesn't exist **")
#        if list_args[1] not in all_objs:
#            print("** no instance found **")
#            return False
#        try:
#            key = list_args[0] +  "." + list_args[1]
#            one_obj = all_objs[key]
#            print(one_obj)
#        except:
#            pass








if __name__ == '__main__':
    HBNBCommand().cmdloop()
