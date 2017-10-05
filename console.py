#!/usr/bin/python3
""" command module """
import cmd
import models
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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

    def do_create(self, args):
        """create <class>
        creates new instance of type class
        """
        list_args = args.split()
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

    def default(self, args):
        ''' method: default
        default handles any command that do not parse to a defined method'''
        args = args.split(".")
        this_class = args[0]
        args = "".join(args[1:])
        args = args.split("(")
        this_func = args[0]
        these_args = "".join(args[1:])  # these_args are all args that append
        # ... to class, which is the 1st arg
        these_args = these_args[:-1]  # strip off trailing closing parenthesis
        these_args = these_args.split()
        these_args.insert(0, this_class)
        for arg in these_args:
            arg = '''"''' + arg + '''"'''
        arg_str = " ".join(these_args)
        # print("arg_str: {}".format(arg_str))
        # print("this_func: {}".format(this_func))
        # print("these_args: {}".format(these_args))
        # print("--------------")
        if len(these_args) == 0:
            print("len = 0")
            exe = ('self.do_{}(*{})'.format(this_func, these_args))
            print(exe)
            eval(exe)
        else:
            print('len > 0')
            exe = ("self.do_{}(*{})".format(this_func, these_args))
            print(exe)
            eval(exe)

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

        all_classes = models.storage.all_classes()
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
        all_objs = models.storage.all()
        all_classes = models.storage.all_classes()

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        classname = list_args[0]
        if classname not in all_classes:
            print("** class doesn't exist **")
            return False

        if len(list_args) < 2:
            print("** instance id missing **")
            return False

        key = "{}.{}".format(list_args[0], list_args[1])
        if key not in all_objs.keys():
            print("** no instance found **")
            return False

        if len(list_args) < 3:
            print("** attribute name missing **")
            return False
        attribute = list_args[2]

        if len(list_args) < 4:
            print("** value missing **")
            return False
        value = list_args[3]

        if attribute not in ("created_at", "updated_at"):
            all_objs[key].__dict__[attribute] = value
            all_objs[key].save

if __name__ == '__main__':
    HBNBCommand().cmdloop()
