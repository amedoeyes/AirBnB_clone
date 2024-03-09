#!/usr/bin/python3

"""BaseModel test module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def test_init_dict(self):
        base1 = BaseModel()
        base2 = BaseModel(**base1.to_dict())

        self.assertNotEqual(base1, base2)
        self.assertEqual(base1.id, base2.id)
        self.assertEqual(base1.created_at, base2.created_at)
        self.assertEqual(base1.updated_at, base2.updated_at)

    def test_id(self):
        self.assertEqual(type(BaseModel().id), str)

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        """Test created_at"""

        self.assertEqual(type(BaseModel().created_at), datetime)

    def test_updated_at(self):
        self.assertEqual(type(BaseModel().updated_at), datetime)

    def test_save(self):
        base = BaseModel()
        base.save()

        self.assertNotEqual(base.created_at, base.updated_at)

    def test_str(self):
        base = BaseModel()

        self.assertIn(base.__str__(), str(base))

        self.assertEqual(
            base.__str__(),
            f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}",
        )

    def test_to_dict(self):
        base = BaseModel()
        base_dict = base.to_dict()

        self.assertEqual(type(base_dict), dict)

        self.assertIn("id", base_dict)
        self.assertIn("created_at", base_dict)
        self.assertIn("updated_at", base_dict)
        self.assertIn("__class__", base_dict)

        self.assertEqual(type(base_dict["id"]), str)
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)
        self.assertEqual(type(base_dict["__class__"]), str)

        self.assertEqual(base_dict["id"], base.id)
        self.assertEqual(base_dict["created_at"], base.created_at.isoformat())
        self.assertEqual(base_dict["updated_at"], base.updated_at.isoformat())
        self.assertEqual(base_dict["__class__"], base.__class__.__name__)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


if __name__ == "__main__":
    unittest.main()
