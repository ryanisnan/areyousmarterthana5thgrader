areyousmarterthana5thgrader is a simple django app that enables you to use arithmetic-based captcha elements on any django form template. The numbers it has the user adding/subtracting are single digits, hence the name "Are you smarter than a 5th grader". It's simple for a reason.

areyousmarterthana5thgrader (henceforth called "app", because the name is TL;DR) is very simple, and should only really be used to prevent non-targeted, low sophistication attacks - typically from things like crawling spambots. The app does use some obfuscation techniques to try and throw off any crawlers.

Again - do not think that this app is a fool proof captcha system.

To use this app in your form template, simply do the following:

1. Add `areyousmarterthana5thgrader` to your `INSTALLED_APPS` setting
2. Add the path to this app's template directory to your project's `TEMPLATE_DIRS` setting
3. In the template of a form you would like to add captcha-vation to, simply `{% load captcha_tags %}`
4. Enter `{% captcha_field %}` wherever you would like the form element to appear within your form
This template tag simply inserts an HTML snippet with a label, a hidden form element containing the answer value, an errors section (in case the user can't add or subtract), and an input box.
5. In your views that process the captcha-vation, simply call the provided method `areyousmarterthana5thgrader.valid_captcha()`, passing in the following two POST values: `request.POST['captcha_answer']`, and `request.POST['captcha_answer_input']`
6. If the captcha method `valid_captcha()` returns False, you can return an error message to the same form with the context variable `captcha_answer_errors`.

ryanisnan@gmail.com