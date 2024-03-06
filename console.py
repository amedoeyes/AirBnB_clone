#!/usr/bin/python3

"""Console module"""

import cmd
import models


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

    def do_create(self, line: str) -> None:
        """Creates a new instance"""

        args = line.split()

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

        args = line.split()
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

        args = line.split()
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

        args = line.split()
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

        args = line.split()
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

        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objects[f"{class_name}.{obj_id}"]
        key = args[2]
        value = args[3].strip("")

        if hasattr(obj, key):
            attr_type = type(getattr(obj, key))
            setattr(obj, key, attr_type(value))
        else:
            setattr(obj, key, value)

        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
