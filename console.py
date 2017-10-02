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
        # print(args)
        # print(type(args))
        list_args = args[0].split()
        # print(list_args)
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
        # print ("list_args: {}".format(list_args))
        all_objs = models.storage.all()
        # print("all_obs: {}".format(str(type(all_objs))))
        # print(all_objs)
        if len(list_args) == 0:
            print("** class name missing **")
            return False

        all_classes = []
        for obj in all_objs:
            # print("----------")
            # print(obj)
            # print(all_objs[obj])
            a_class = obj.split(".")[0]
            if a_class not in all_classes:
                all_classes.append(a_class)
        # print("all_classes: {}".format(all_classes))

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
        '''method: do_delete
        delete an object based on class name and id and update change to file
        '''
        list_args = args.split()
        all_objs = models.storage.all()
        if len(list_args) == 0:
            print("** class name missing **")
            return False

        # build list of all classes of objects in storage
        all_classes = []
        for obj in all_objs:
            a_class = obj.split(".")[0]
            if a_class not in all_classes:
                all_classes.append(a_class)

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
