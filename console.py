#!/usr/bin/python3

"""Console module"""

import cmd
import models
import re
from shlex import split
import json


def parse(line):
    """Parse input"""

    curly_braces = re.search(r"\{(.*?)\}", line)

    if curly_braces:
        toks = split(line[: curly_braces.span()[0]])
        args = [arg.strip(",") for arg in toks]
        args.append(curly_braces.group().replace("'", '"'))
        return args

    return [arg.strip(",") for arg in split(line)]


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_EOF(self, line: str) -> bool:
        """EOF command to exit the program"""

        return True

    def emptyline(self) -> None:
        """Do nothing on empty lines"""

        pass

    def do_quit(self, line: str) -> bool:
        """Quit command to exit the program"""

        return True

    def default(self, line):
        """Default behavior for cmd module when input is invalid"""

        commands = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count,
        }

        if "." in line:
            toks = line.split(".")
            class_name = toks[0]
            command = toks[1][0 : toks[1].find("(")]
            command_args = re.search(r"\((.*?)\)", toks[1])
            if class_name and command and command_args and command in commands:
                command_args = command_args.group()[1:-1]
                return commands[command](f"{class_name} {command_args}")

        print(f"*** Unknown syntax: {line}")
        return False

    def do_create(self, line: str) -> None:
        """Creates a new instance"""

        args = parse(line)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        new_instance = models.classes[args[0]]()
        models.storage.save()
        print(new_instance.id)

    def do_show(self, line: str) -> None:
        """Prints string representation of an instance"""

        args = parse(line)
        all_objects = models.storage.all()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if f"{class_name}.{obj_id}" not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[f"{class_name}.{obj_id}"])

    def do_destroy(self, line: str) -> None:
        """Deletes an instance"""

        args = parse(line)
        all_objects = models.storage.all()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if f"{class_name}.{obj_id}" not in all_objects:
            print("** no instance found **")
            return

        del all_objects[f"{class_name}.{obj_id}"]
        models.storage.save()

    def do_all(self, line: str) -> None:
        """Prints all string representation of all instances"""

        args = parse(line)
        all_objects = models.storage.all()

        if not args:
            for obj in all_objects.values():
                print(obj)
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        for obj in all_objects.values():
            if args[0] in obj.__class__.__name__:
                print(obj)

    def do_update(self, line: str) -> None:
        """Updates an instance"""

        args = parse(line)
        all_objects = models.storage.all()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]

        if f"{class_name}.{obj_id}" not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        obj = all_objects[f"{class_name}.{obj_id}"]

        try:
            update_dict = json.loads(args[2])
            for key, value in update_dict.items():
                if hasattr(obj, key):
                    attr_type = type(getattr(obj, key))
                    setattr(obj, key, attr_type(value))
                else:
                    setattr(obj, key, value)
            models.storage.save()
            return
        except Exception:
            pass

        if len(args) < 4:
            print("** value missing **")
            return

        key = args[2]
        value = args[3].strip("")
        if hasattr(obj, key):
            attr_type = type(getattr(obj, key))
            setattr(obj, key, attr_type(value))
        else:
            setattr(obj, key, value)
        models.storage.save()

    def do_count(self, line: str) -> None:
        """Count the number of instances of a class"""

        args = parse(line)

        if not args:
            print("** class name missing **")
            return

        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return

        count = 0
        for value in models.storage.all().values():
            if args[0] == value.__class__.__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
