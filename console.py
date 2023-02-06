import cmd
import sys


class HBNBCommand(cmd.Cmd):
     """HBNB console entry point"""
     prompt = '(hbnb) '

     def do_quit(self, command):
          """ Method to exit the HBNB console"""
          exit()

     def help_quit(self):
          """ Prints the help documentation for quit  """
          print("Exits the program with formatting")

     def do_EOF(self, arg):
          """ Handles EOF to exit program """
          print()
          exit()

     def help_EOF(self):
          """ Prints the help documentation for EOF """
          print("Exits the program without formatting\n")

     def emptyline(self):
          """ Overrides the emptyline method of CMD """


if __name__ == '__main__':
    HBNBCommand().cmdloop()