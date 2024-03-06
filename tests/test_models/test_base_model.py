#!/usr/bin/python3

"""BaseModel class test module"""

import unittest
from datetime import datetime
from models import base_model


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def test_docstring(self):
        """Test docstring"""

        self.assertIsNotNone(base_model.__doc__)
        for func in dir(base_model):
            self.assertIsNotNone(func.__doc__)
        self.assertIsNotNone(base_model.BaseModel.__doc__)
        for method in dir(base_model.BaseModel):
            self.assertIsNotNone(method.__doc__)

    def test_init_dict(self):
        """Test init with dict"""

        base1 = base_model.BaseModel()
        base2 = base_model.BaseModel(**base1.to_dict())

        self.assertNotEqual(base1, base2)
        self.assertEqual(base1.id, base2.id)
        self.assertEqual(base1.created_at, base2.created_at)
        self.assertEqual(base1.updated_at, base2.updated_at)

    def test_id(self):
        """Test id"""

        self.assertEqual(type(base_model.BaseModel().id), str)

        base1 = base_model.BaseModel()
        base2 = base_model.BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_created_at(self):
        """Test created_at"""

        self.assertEqual(type(base_model.BaseModel().created_at), datetime)

    def test_updated_at(self):
        """Test updated_at"""

        self.assertEqual(type(base_model.BaseModel().updated_at), datetime)

    def test_save(self):
        """Test save"""

        base = base_model.BaseModel()
        base.save()

        self.assertNotEqual(base.created_at, base.updated_at)

    def test_str(self):
        """Test __str__"""

        base = base_model.BaseModel()

        self.assertIn(base.__str__(), str(base))

        self.assertEqual(
            base.__str__(),
            f"[{base.__class__.__name__}] ({base.id}) {base.__dict__}",
        )

    def test_to_dict(self):
        """Test to_dict"""

        base = base_model.BaseModel()
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


if __name__ == "__main__":
    unittest.main()
