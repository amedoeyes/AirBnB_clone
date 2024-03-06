#!/usr/bin/python3

"""FileStorage test module"""

import unittest
import os
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """TestFileStorage class"""

    def test_docstring(self):
        """Test docstring"""

        self.assertIsNotNone(file_storage.__doc__)
        for func in dir(file_storage):
            self.assertIsNotNone(func.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)
        for method in dir(FileStorage):
            self.assertIsNotNone(method.__doc__)

    def test_new(self):
        """Test new method"""

        storage = FileStorage()
        all = storage.all()

        base = BaseModel()
        storage.new(base)

        self.assertEqual(len(all), 1)
        self.assertEqual(all[f"{base.__class__.__name__}.{base.id}"], base)

        base2 = BaseModel()
        storage.new(base2)

        self.assertEqual(len(all), 2)
        self.assertEqual(all[f"{base2.__class__.__name__}.{base2.id}"], base2)

    def test_save(self):
        """Test save method"""

        storage = FileStorage()
        storage.save()

        self.assertTrue(os.path.exists("file.json"))
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(os.path.getsize("file.json") > 0)

    def test_reload(self):
        """Test reload method"""

        base = BaseModel()
        base2 = BaseModel()

        storage = FileStorage()
        storage.new(base)
        storage.new(base2)
        storage.save()

        storage2 = FileStorage()
        storage2.reload()

        all = storage2.all()

        self.assertEqual(
            all[f"{base.__class__.__name__}.{base.id}"].to_dict(),
            base.to_dict(),
        )
        self.assertEqual(
            all[f"{base2.__class__.__name__}.{base2.id}"].to_dict(),
            base2.to_dict(),
        )


if __name__ == "__main__":
    unittest.main()
