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
        return True
    
    def do_EOF(self, arg):
        """ EOF signal to exit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()