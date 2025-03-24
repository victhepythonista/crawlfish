
class InvalidSaveOptionError(Exception):
	''' To be raised when an object is not a SaveOption object '''
	def __init__(self , message):
		self.message = "Crawlfish could not load this SaveOption class -> " +  message
		super().__init__(self.message)


 
class UnsupportedSaveOptionInstanceError(Exception):
	''' To be raised when the  SaveOption instance provided is not of a supported type
	  '''
	def __init__(self , save_option_instance , supported_save_option_instances):
		self.message = """
		The SaveOption instance provided [{}] is an unsupported class of SaveOption . 
		 Supported classes are : 
		 -----------------------
		 {}
		 ------------------------
		 """.format(save_option_instance , supported_save_option_instances)
		super().__init__(self.message)


class InvalidSaveOptionError(Exception):
	''' To be raised when the  static type provided isn't supported
	  '''
	def __init__(self ,type_provided):
		self.message = """Invalid static type {} . Only Javascript and CSS are supported """.format(type_provided)
		super().__init__(self.message)

