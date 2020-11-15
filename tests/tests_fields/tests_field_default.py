import unittest
from ontosqlson.ontology import Ontology
from ontosqlson.schema import Schema
from ontosqlson.field import (TextField,
                              IntegerField,
                              PositiveIntegerField,
                              RelationField,
                              MixField)


class TestFieldDefault(unittest.TestCase):
    def setUp(self):
        ontology = Ontology()
        ontology.schema_fields.clear()
        ontology.schema_models.clear()

    def test_field_text(self):
        class Thing(Schema):
            name = TextField(default="default")
        thing = Thing()
        self.assertEqual(thing.name, "default")
        thing.name = "name1"
        self.assertEqual(thing.name, "name1")

    def test_field_integer(self):
        class Thing(Schema):
            name = IntegerField(default=1)
        thing = Thing()
        self.assertEqual(thing.name, 1)
        thing.name = 2
        self.assertEqual(thing.name, 2)

    def test_field_positive_integer(self):
        class Thing(Schema):
            name = PositiveIntegerField(default=1)
        thing = Thing()
        self.assertEqual(thing.name, 1)
        thing.name = 2
        self.assertEqual(thing.name, 2)

    def test_field_class(self):
        class Thing(Schema):
            name = TextField(default="default")

        class Thing2(Schema):
            other = RelationField("Thing", default=Thing(name="name1"))

        thing2 = Thing2()
        self.assertEqual(thing2.other.name, "name1")
        thing2.other.name = "new_name"
        self.assertEqual(thing2.other.name, "new_name")

    def test_field_mix(self):
        class Thing(Schema):
            name = TextField(default="default")

        class Thing2(Schema):  # NOSONAR
            name2 = TextField(default="default2")

        class Thing3(Schema):
            other = MixField(["Thing", "Thing2"], default=Thing(name="name1"))

        thing3 = Thing3()
        self.assertEqual(thing3.other.name, "name1")
        thing3.other.name = "new_name"
        self.assertEqual(thing3.other.name, "new_name")
