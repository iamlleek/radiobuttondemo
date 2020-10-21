"""
Program: radiobuttondemo.py
Author: Nylek 10/19/2020
Example on pages 283 - 284

SimpleGUI-based application highlighting the use of checkboxes
"""

from breezypythongui import EasyFrame

class RadiobuttonDemo(EasyFrame):
	"""Allows the user to place a restaurant order from a set of radio button options."""

	def __init__(self):
		"""Sets up the window and the widgeta."""
		EasyFrame.__init__(self, title = "Radio Button Demo")

		# Add the label, button group and radio buttons for meats
		self.addLabel(text = "Meat", row = 0, column = 0)
		self.meatGroup = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 2)
		defaultRB = self.meatGroup.addRadiobutton(text = "Chicken")
		# Make the chicken radio button the pre-selected option
		self.meatGroup.setSelectedButton(defaultRB)
		self.meatGroup.addRadiobutton(text = "Beef")

		# Add the label, button group and radio buttons for potatoes
		self.addLabel(text = "Potatoes", row = 0, column = 1)
		self.taterGroup = self.addRadiobuttonGroup(row = 1, column = 1, rowspan = 2)
		defaultRB = self.taterGroup.addRadiobutton(text = "French Fries")
		# Make the chicken radio button the pre-selected option
		self.taterGroup.setSelectedButton(defaultRB)
		self.taterGroup.addRadiobutton(text = "Baked Potato")

		# Add the label, button group and radio buttons for veggies
		self.addLabel(text = "Vegetable", row = 0, column = 2)
		self.vegGroup = self.addRadiobuttonGroup(row = 1, column = 2, rowspan = 2)
		defaultRB = self.vegGroup.addRadiobutton(text = "Applesauce")
		# Make the applesauce radio button the pre-selected option
		self.vegGroup.setSelectedButton(defaultRB)
		self.vegGroup.addRadiobutton(text = "Green Beans")		

		# Add the command button
		self.addButton(text = "Place Order", row = 3, column = 0, columnspan = 3, command = self.placeOrder)

	# Event handling method
	def placeOrder(self):
			"""Display a message box with the order summary."""
			message = ""
			message += self.meatGroup.getSelectedButton()["text"] + "\n\n"
			message += self.taterGroup.getSelectedButton()["text"] + "\n\n"
			message += self.vegGroup.getSelectedButton()["text"] + "\n\n"
			# generate a message dialog with message variable text inside
			self.messageBox(title = "Customer Order", message = message)

# Definition of the main() function
def main():
	RadiobuttonDemo().mainloop()

# global call to the main() function
main()