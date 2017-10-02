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
        list_args = args[0].split()
        if len(list_args) == 0:
            print("** class name missing **")
            return False

        classname = list_args[0]
        try:
            new_obj = eval(classname)()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ show string representation of an instance """
        list_args = args.split()
        all_objs = models.storage.all()
		all_classes = models.storage.all_classes()

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        if list_args[0] in all_classes:
            if len(list_args) > 1:
                key = list_args[0] + "." + list_args[1]
                if key in all_objs:
                    one_obj = all_objs[key]
                    print(one_obj)
                else:
                    print("** no instance found **")
            else:
                print("** instance id  missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        '''destroy: delete specified object from storage
        delete an object based on class name and id and update change to file
        '''
        list_args = args.split()
        all_objs = models.storage.all()
		all_classes = models.storage.all_classes()

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        if list_args[0] in all_classes:
            if len(list_args) > 1:
                key = list_args[0] + "." + list_args[1]
                if key in all_objs:
                    # this is where we delete the ojbect from storage instance
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id  missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        '''command: all <class>
        print all instances, if class is specified, only print objects of type
        <class>
        '''
        list_args = args.split()

        all_classes = models.storage.all_classes() # first use of this method
        all_objs = models.storage.all()

        if len(list_args) > 1:
            print("**class doesn't exist **")
            return False
        if len(list_args) != 0 and list_args[0] not in all_classes:
            print("** class doesn't exist **")
            return False

        if len(list_args) == 0:  # print all objects, since no class specified
            for obj in all_objs:
                print(all_objs[obj])
        else:  # only print objects matching specified class
            for obj in all_objs:
                a_class = obj.split(".")[0]
                if a_class == list_args[0]:
                    print(all_objs[obj])

    def do_update(self, args):
        '''command: update <class> <UUID> <key> <value>
        update object specified by <class> and <UUID> by adding or updating
        an attribute specified by <key> <value>
        '''
        list_args = args.split()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
