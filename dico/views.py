from contact_form.views import ContactFormView as BaseFormView
from .forms import ContactForm

class ContactFormView(BaseFormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/contact/sent/'
