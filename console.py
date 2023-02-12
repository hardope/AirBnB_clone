import cmd
import sys
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
     """HBNB console entry point"""
     prompt = '(hbnb) '

     classes = {
               'BaseModel': BaseModel
     }

     def precmd(self, line):
          """Reformat command line for advanced command syntax.

          Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
          (Brackets denote optional fields in usage example.)
          """
          _cmd = _cls = _id = _args = ''  # initialize line elements

          # scan for general formating - i.e '.', '(', ')'
          if not ('.' in line and '(' in line and ')' in line):
               return line

          try:  # parse line left to right
               pline = line[:]  # parsed line

               # isolate <class name>
               _cls = pline[:pline.find('.')]

               # isolate and validate <command>
               _cmd = pline[pline.find('.') + 1:pline.find('(')]
               if _cmd not in HBNBCommand.dot_cmds:
                    raise Exception

               # if parantheses contain arguments, parse them
               pline = pline[pline.find('(') + 1:pline.find(')')]
               if pline:
                    # partition args: (<id>, [<delim>], [<*args>])
                    pline = pline.partition(', ')  # pline convert to tuple

                    # isolate _id, stripping quotes
                    _id = pline[0].replace('\"', '')
                    # possible bug here:
                    # empty quotes register as empty _id when replaced

                    # if arguments exist beyond _id
                    pline = pline[2].strip()  # pline is now str
                    if pline:
                         # check for *args or **kwargs
                         if pline[0] == '{' and pline[-1] == '}'\
                              and type(eval(pline)) is dict:
                              _args = pline
                         else:
                              _args = pline.replace(',', '')
               # _args = _args.replace('\"', '')
               line = ' '.join([_cmd, _cls, _id, _args])

          except Exception as mess:
               pass
          finally:
               return line

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
     
     def do_create(self, args):
          """ Create an object"""
          try:
               if not args:
                    raise SyntaxError()
               arg_list = args.split(" ")
               kw = {}
               for arg in arg_list[1:]:
                    print(arg)
                    arg_splited = arg.split("=")
                    print(arg_splitted)
                    arg_splited[1] = eval(arg_splited[1])
                    if type(arg_splited[1]) is str:
                         arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                    kw[arg_splited[0]] = arg_splited[1]
          except SyntaxError:
               print("** class name missing **")
          except NameError:
               print("** class doesn't exist **")
          new_instance = HBNBCommand.classes[arg_list[0]](**kw)
          new_instance.save()
          print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()