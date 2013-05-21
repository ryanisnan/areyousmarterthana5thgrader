from django import template
import random

register = template.Library()

"""
Template tag to display a captcha form field
"""
def captcha_field(context):
	response_dict = {}
	
	# Captcha Code
	operand1 = random.randint(4,8)
	operand2 = random.randint(1,4)
	operator = random.randint(1,2)
	answer = None
	if operator == 1:
		# Addition
		answer = operand1 + operand2
		response_dict.update({ 'captcha_operator' : '+' })
	elif operator == 2:
		# Subtraction
		answer = operand1 - operand2
		response_dict.update({ 'captcha_operator' : '-' })
	
	response_dict.update({ 'captcha_operand1' : operand1 })
	response_dict.update({ 'captcha_operand2' : operand2 })
	response_dict.update({ 'captcha_answer' : answer })
	response_dict.update({ 'captcha_answer_errors' : context.get('captcha_answer_errors') })
	
	return response_dict
	
register.inclusion_tag('captcha_field.html', takes_context=True)(captcha_field)