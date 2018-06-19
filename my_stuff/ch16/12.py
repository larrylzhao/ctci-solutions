# Encode some XML.

def xml_encoding(xml_object, mapping):
    out_str = ""

    out_str += str(mapping[xml_object.element]) + " "
    if xml_object.attributes:
        for key, value in sorted(xml_object.attributes.items(), reverse=True):
            out_str += str(mapping[key]) + " " + value + " "
    out_str += "0"
    if xml_object.children:
        for child in xml_object.children:
            out_str += " " + xml_encoding(child, mapping)
    out_str += " 0"
    # out_str = out_str.strip()
    return out_str


class XMLObject(object):
    def __init__(self, element, attributes=None, children=None):
        self.element = element
        self.attributes = attributes
        self.children = children



import unittest

class Test(unittest.TestCase):
    def test_xml_encoding(self):
        mapping = {"name": 1, "instrument": 2, "person": 3, "monkey": 4, "color": 5}
        xml = XMLObject("person",
                        {"name": "The Man with the Yellow Hat", "instrument": "tuba"},
                        [XMLObject("monkey", {"name": "George", "color": "brown"})])
        self.assertEqual(xml_encoding(xml, mapping),
                         "3 1 The Man with the Yellow Hat 2 tuba 0 4 1 George 5 brown 0 0 0")

if __name__ == "__main__":
    unittest.main()

