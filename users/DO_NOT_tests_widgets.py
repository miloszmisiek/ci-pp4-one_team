# from django.test import TestCase, SimpleTestCase
# from django.forms.renderers import DjangoTemplates, Jinja2
# from django.forms import Select
# from .widgets import SelectWithDisabled
# from .forms import RANNK_CHOICES, UserSignupForm

# try:
#     import jinja2
# except ImportError:
#     jinja2 = None

# class WidgetTest(SimpleTestCase):
#     beatles = (("J", "John"), ("P", "Paul"), ("G", "George"), ("R", "Ringo"))

#     @classmethod
#     def setUpClass(cls):
#         cls.django_renderer = DjangoTemplates()
#         cls.jinja2_renderer = Jinja2() if jinja2 else None
#         cls.renderers = [cls.django_renderer] + (
#             [cls.jinja2_renderer] if cls.jinja2_renderer else []
#         )
#         super().setUpClass()

#     def check_html(
#         self, widget, name, value, html="", attrs=None, strict=False, **kwargs
#     ):
#         assertEqual = self.assertEqual if strict else self.assertHTMLEqual
#         if self.jinja2_renderer:
#             output = widget.render(
#                 name, value, attrs=attrs, renderer=self.jinja2_renderer, **kwargs
#             )
#             # Django escapes quotes with '&quot;' while Jinja2 uses '&#34;'.
#             output = output.replace("&#34;", "&quot;")
#             # Django escapes single quotes with '&#x27;' while Jinja2 uses '&#39;'.
#             output = output.replace("&#39;", "&#x27;")
#             assertEqual(output, html)

#         output = widget.render(
#             name, value, attrs=attrs, renderer=self.django_renderer, **kwargs
#         )
#         assertEqual(output, html)




# class CustomWidgetsTest(WidgetTest):
#     widget = Select
#     choices = RANNK_CHOICES
#     form = UserSignupForm(
#             data={
#                 'username': 'username',
#                 'email': 'username@mail.com',
#                 'email2': 'username@mail.com',
#                 'password1': 'passwor34Rd',
#                 'password2': 'passwor34Rd',
#                 'first_name': 'first_name',
#                 'last_name': 'last_name',
#                 'rank': RANNK_CHOICES[0][0]
#             }
#         )

#     def test_render(self):
#         self.check_html(
#             self.widget(choices)
#         )