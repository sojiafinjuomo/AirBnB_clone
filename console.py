#!/usr/bin/python3
"""
Module for a class HBNBCommand
Authors: Mire & Soji
"""

import cmd
import models
from models import storage
from shlex import split as split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
           'City': City, 'Amenity': Amenity, 'Place': Place,
           'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    contains the entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def do_greet(self, line):
        """
        Greets the User
        Usage: greet <user>
        """
        if line:
            print("hi", line)
        else:
            print("hi")

    def do_quit(self, line):
        """
        Quit command to exit the program
        Usage: quit
        """
        return True

    def do_exit(self, line):
        """
        Exits the program
        Usage: exit
        """

    def emptyline(self):
        """shouldn't execute anything"""
        pass

    def do_EOF(self, line):
        """ Exit the program"""
        return True

    def do_create(self, line):
        """
        Creates new instance of BaseModel
        Usage: create <class_name>
        """
        split_line = split(line)
        if not split_line:
            print("** class name missing **")
        elif split_line[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_model = classes[split_line[0]]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints String representation of an Instance
        Usage: show <class_name> <id>
        """
        split_line = split(line)
        if not split_line:
            print('** class name missing **')
        elif split_line[0] not in classes:
            print("** class doesn't exist**")
        elif len(split_line) < 2:
            print("** instance id missing **")
        else:
            new_model = split_line[0] + '.' + split_line[1]
            if new_model not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[new_model])

    def do_destroy(self, line):
        """
        Deletes Instance from storage
        Usage: delete <class_name> <id>
        """
        split_line = split(line)
        if not split_line:
            print('** class name missing **')
            return False
        elif split_line[0] not in classes:
            print("** class doesn't exist**")
        elif len(split_line) < 2:
            print("** instance id missing **")
        else:
            new_model = split_line[0] + '.' + split_line[1]
            if new_model not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_model]
                models.storage.save()

    def do_all(self, line):
        """Prints the string representation of all instances
        Usage:
           all <class_name>(optional)
        """
        str_lst = []
        if not line:
            for new_model in models.storgae.all().values():
                str_lst.append(str(new_model))
        else:
            split_line = split(line)
            if split_line[0] in classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == split_line[0]:
                        str_lst.append(str(value))
            else:
                print("** class doesn't exist **")
        print(str_lst)

    def do_update(self, line):
        """
        Update object attributes or add attributes to object

        Usage:
            update <class_name> <id> <attribute name>
            <attribute value>
        """
        split_line = split(line)
        if not split_line:
            print('** class name missing **')
        elif split_line[0] not in classes:
            print("** class doesn't exist**")
        elif len(split_line) < 2:
            print("** instance id missing **")
        elif len(split_line) < 3:
            print("** attribute name missing **")
        elif len(split_line) < 4:
            print("** value missing **")
        else:
            new_model = split_line[0] + '.' + split_line[1]
            if new_model not in models.storeage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_model],
                        split_line[2], split_line[3])
                models.storage.save()

    def default(self, args):
        """ Retrieve all instances of a class. """
        count = 0
        split_line = args.split('.', 1)
        if len(split_line) >= 2:
            args = split_line[1].split('(')
            if args[0] == 'all':
                self.do_all(split_line[0])
            elif args[0] == 'count':
                for key in models.storage.all():
                    if split_line[0] == key.split(".")[0]:
                        count += 1
                print(count)
            elif args[0] == 'show':
                id = args[1].split(')')
                str_id = str(split_line[0]) + " " + str(id[0])
                self.do_show(str_id)
            elif args[0] == 'destroy':
                id = args[1].split(')')
                str_id = str(split_line[0]) + " " + str(id[0])
                self.do_destroy(str_id)
            elif args[0] == 'update':
                update = args[1].split(')')
                split = update[0].split('{')
                if len(split) == 1:
                    arg = update[0].split(",")
                    str_id = str(split_line[0]) + " " + str(arg[0]) + \
                        " " + str(arg[1]) + " " + str(arg[2])
                    self.do_update(str_id)
                else:
                    id = split[0][:-2]
                    str_dict = split[1][:-1]
                    delim = str_dict.split(',')
                    for row in delim:
                        key_value = row.split(':')
                        str_id = str(split_line[0]) + " " + str(id) + \
                            " " + str(key_value[0]) + " " + str(key_value[1])
                        self.do_update(str_id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
