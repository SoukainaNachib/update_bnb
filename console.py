#!/usr/bin/python3
""" Defines the HbnB console."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines tha alxBnB cammand interpreter.
    Attribute:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass


    def do_quit(self, arg):
        """ Quit command to exit the program"""
        exit()
    
    def do_EOF(self, arg):
        """ EOF signal to exit the program"""
        print("")
        exit()
    
    def do_create(self, args):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if not args:
            print("Class name Missing")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exit  **")
            return
        new_instatce = eval[args]()
        new_instatce.save()
        print(new_instatce.id)


        

















if __name__ == "__main__":
    HBNBCommand().cmdloop()