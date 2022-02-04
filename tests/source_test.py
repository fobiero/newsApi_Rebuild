import unittest
from app.model import Sources

class SourceTest(unittest.TestCase):
    """
    Test class to test the behaviour of the news class
    """

    def setUp(self):
        """
        """
        self.new_source = Sources('Test id','Test name','Test description','Test author', 'Test publishedAt', 'Test title', 'Test urlToImage')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources)) 

