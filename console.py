#!/usr/bin/python3
""" command module """
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = ["BaseModel", "User", "City", "Place", "State", "Amenity", "Review"]


class HBNBCommand(cmd.Cmd):
    """ cmd class """
    prompt = '(hbnb) '

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
        list_l = args.split(".")
        classname = list_l[0]
        arguments = shlex.split(list_l[1])
        command = arguments[0].split("(")
        arguments[0] = command[1]
        modified_args = []
        for item in arguments:
            modified_args.append(item[:-1])
        command = command[0]
        string_exe = command + " " + classname + " " + " ".join(modified_args)
        self.onecmd(string_exe)

    def do_show(self, args):
        """ show string representation of an instance """
        list_args = args.split()
        all_objs = models.storage.all()

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        if list_args[0] in classes:
            if len(list_args) > 1:
                key = list_args[0] + "." + list_args[1]
                if key in all_objs:
                    one_obj = all_objs[key]
                    print(one_obj)
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        '''destroy: delete specified object from storage
        delete an object based on class name and id and update change to file
        '''
        list_args = args.split()
        all_objs = models.storage.all()

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        if list_args[0] in classes:
            if len(list_args) > 1:
                key = list_args[0] + "." + list_args[1]
                if key in all_objs:
                    # this is where we delete the ojbect from storage instance
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        '''command: all <class>
        print all instances, if class is specified, only print objects of type
        <class>
        '''
        list_args = args.split()

        all_objs = models.storage.all()

        if len(list_args) > 1:
            print("**class doesn't exist **")
            return False
        if len(list_args) != 0 and list_args[0] not in classes:
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

        if len(list_args) == 0:
            print("** class name missing **")
            return False

        classname = list_args[0]
        if classname not in classes:
            print("** class doesn't exist **")
            return False

        if len(list_args) < 2:
            print("** instance id missing **")
            return False
        my_id = list_args[1]

        key = "{}.{}".format(classname, my_id)
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

        if attribute not in ("id", "created_at", "updated_at"):
            all_objs[key].__dict__[attribute] = value
            all_objs[key].save

if __name__ == '__main__':
    HBNBCommand().cmdloop()
