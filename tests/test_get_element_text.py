

from unittest import TestCase 


from .data import grocery_list_soup

from crawlfish.html import get_element_text , get_elements_text

test_soup = grocery_list_soup

class TestGettingElementText(TestCase):

	def test_get_element_text(self):
		expected_text = "listHeading"
		heading_element = test_soup.find("h1" , {"class":"list-heading"})
		text = get_element_text(heading_element)
		self.assertTrue(text == expected_text)


	def test_get_elements_text(self):
		expected_result = [  'Milk', 'Pears' , "Oranges" , 'Tomatoes' , 'Cheese' ]
		texts = get_elements_text(test_soup ,tag_name = 'li', attribute =  'class' , attribute_value = 'grocery-list-item')
		print("TEST RESULT : " , texts)
		self.assertTrue(expected_result == texts)