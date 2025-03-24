
from crawlfish import ElementFinder


# Find all <h2></h2> elements from a html string 
html = "<h2>Hello</h2> <h2>there </h2> <h2>you</h2>"
finder = ElementFinder(html)
elements = finder.find_elements(tag_name = "h2") 

# Find just 2 <h2> elements from a html string
html = "<h2>Hello</h2> <h2>there </h2> <h2>you</h2>"
finder = ElementFinder(html)
elements = finder.find_elements(tag_name = "h2" , num = 2) 


# Find  elements by the tag name , atribute name and attribute value  
html = """
<!DOCTYPE html>
<html>
<head>
	<title> Let's find elements </title>
</head>
<body>

<div></div>
<div></div>
<div></div>
<div id="name" >Sherlock Holmes</div>
<div id="name" >Mansa Musa</div>



</body>
</html>

"""
finder = ElementFinder(html)
elements = finder.find_elements( tag_name = "div",  attribute = "id" , attribute_value = "name"  )



# Search elements by text match
# normal text match example
html = '<div id="person"> @ ceo Zuck </div> <div id="person">@warlord Khan</div> <div id="person">@ ceo John</div>'
finder = ElementFinder(html)
elements = finder.find_elements( text_match = "ceo" )
elements

# with regex example
html =  '<div>This is not an email</div> <div>randomemail@yahoo.com</div> <div>anotheremail@gmail.com</div>'
finder = ElementFinder(html)
email_regex = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+" 
elements = finder.find_elements(text_match = email_regex)
elements



# Search for elements by multiple values 
html = """
<!DOCTYPE html>
<html>
	<head>
		<title> Let's find elements </title>
	</head>
	<body>

	<div id="person" class="person-container" > 
		 Someone had an email and it was someemail@gmail.com , yeah , his name was Ail Someem
	</div>

	<div id="" class="" ></div>
	<div id="" class="" ></div>
	<div id="" class="" ></div>

	<div id="" class="email-div" ></div>

	<p id="email-p" >validemail@gmail.com</p>
	<p id="email-p" ></p>
	<p id="" class="email-p"></p>
	<p id="" class="email-p"></p>
	<div id="" class="email-div" >Anothervalidemail@gmail.com</div>
	<div id="" class="email-div" ></div>

	<p id="" class="email-p"></p>

	<a id="" class="" ></a>
	<a id="" class="" ></a>
	<a id="" class="" ></a>
	<a id="" class="" ></a>
	<a id="" class="" ></a>



	</body>
</html>

"""
# Lets collect elements with valid email addresses as an example
# You can see the data is jumbled up but there are some constant information we can utilize to get everything in one line
finder = ElementFinder(html)
email_regex = r"[\w\.-]+@[\w\.-]+(\.[\w]+)+" 
elements = finder.find_elements(  attributes = [ "id" , "class"] , attribute_values = ['email' , ] ,
		 tag_names = [ 'div' , 'p'] ,text_matches = [email_regex, ]    )
elements