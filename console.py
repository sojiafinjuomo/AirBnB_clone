#!/usr/bin/python3
"""
Module for a class HBNBCommand
Authors: Mire & Soji
"""

import cmd
from models import storage
from models.base_model import BaseModel
import json
objects = storage.all()
classes = ['BaseModel', 'User']

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
        if not line:
            print("** class name missing **")
        elif line not in classes:
            print("** class doesn't exist **")
        else:
            new_model = f'{line}'()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints String representation of an Instance
        Usage: show <class_name> <id>
        """
        args = line.split()
        args.append(None)
        if not args[0]:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist**")
        elif not args[1]:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects:
            print("** no instance found **")
        else:
            model = objects[f'{args[0]}.{args[1]}']
            print(model)

    def do_delete(self, line):
        """
        Deletes Instance from storage
        Usage: delete <class_name> <id>
        """
        args = line.split()
        args.append(None)
        if not args[0]:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist**")
        elif not args[1]:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects:
            print("** no instance found **")
        else:
            del objects[f'{args[0]}.{args[1]}']
            with open("./models/engine/storage.json", 'w') as file:
                json.dump(objects, file)

    def do_all(self, line):
        """Prints the string representation of all instances
        Usage:
           all <class_name>(optional)
        """
        models = []
        if line != '' and line not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                sep = key.split('.')
                models.append(f'[{sep[0]}] ({sep[1]}) {value}')
            print(models)

    def do_update(self, line):
        """Update object attributes or add attributes to object

        Usage:
            update <class_name> <id> <attribute name>
            <attribute value>
        """
        args = line.split()
        args.append(None)
        if not args[0]:
            print('** class name missing **')
        elif args[0] not in classes:
            print("** class doesn't exist**")
        elif not args[1]:
            print("** instance id missing **")
        elif f'{args[0]}.{args[1]}' not in objects:
            print("** no instance found **")
        elif not args[2]:
            print("** attribute name missing **")
        elif not args[3]:
            print("** value missing **")
        else:
            objects[f'{args[0]}.{args[1]}'][f'{args[2]}'] = f'{args[3]}'
            with open('./models/engine/storage.json', 'w') as file:
                json.dump(objects, file)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
