import unittest
from ontosqlson.ontology import Ontology
from ontosqlson.schema import Schema
from ontosqlson.field import (TextField)


class TestFieldMany(unittest.TestCase):
    def setUp(self):
        ontology = Ontology()
        ontology.schema_fields.clear()
        ontology.schema_models.clear()

    def test_field_many_basic(self):
        class Thing(Schema):
            names = TextField(many=True)
        thing = Thing()
        thing.names.append("name1")
        thing.names.append("name2")
        self.assertEqual(len(thing.names), 2)
        self.assertTrue("name1" in thing.names)
        self.assertTrue("name2" in thing.names)

    def test_field_many_load(self):
        class Thing(Schema):
            names = TextField(many=True)
        thing = Thing()
        json_data = {"instance_of": "Thing", "names": ["name1", "name2"]}
        thing.load(json_data)
        self.assertEqual(len(thing.names), 2)
        self.assertTrue("name1" in thing.names)
        self.assertTrue("name2" in thing.names)

    def test_field_many_save(self):
        class Thing(Schema):
            names = TextField(many=True)
        thing = Thing()
        thing.names.append("name1")
        thing.names.append("name2")
        json_data = thing.save()
        self.assertEqual(len(json_data["names"]), 2)
        self.assertTrue("name1" in json_data["names"])
        self.assertTrue("name2" in json_data["names"])