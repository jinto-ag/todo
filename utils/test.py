import unittest
from base import Field
from django.db.models import fields

class FieldTest(unittest.TestCase):
    field = Field("age", "CharField", max_length=500, blank=True)
    
    def test_create_field(self):
        field = self.field
        self.assertEqual(field.type, fields.CharField)
        
    def test_get_field(self):
        self.assertEqual(str(self.field), "age = CharField(max_length=500, blank=True)")
        
    def test_get_field_options(self):
        self.assertDictEqual(self.field.options, {})
        
    
        
if __name__ == "__main__":
    unittest.main()