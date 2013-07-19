from django import forms
from contact_form.forms import ContactForm as ContactBaseForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div, Field, HTML
from crispy_forms.bootstrap import FormActions

class VerifyEmail(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    emailv = forms.EmailField(label='', required=True)

    def clean(self):
        super(VerifyEmail, self).clean()
        clean = self.cleaned_data
        em1, em2 = clean.get('email'), clean.get('emailv')
        if em1 and em2 and em1 != em2:
            raise forms.ValidationError('Emails are not the same.')
        return clean

class ContactForm(VerifyEmail, ContactBaseForm):
    name = forms.CharField(label='Name', required=True)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.subject_template_name = 'subject.txt'
        self.template_name = 'message.txt'
        
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.form_action = '/contact/us/'
        self.helper.layout = Layout(
            Fieldset(
                'Contact Us',
                'name',
                Div(
                    Field('email'),
                    Field('emailv', placeholder="Verify Email"),
                    css_class="inline"
                ),
                Field('message', css_class="span4"),
                'captcha',
            ),
            FormActions(
                Submit('submit',
                       'Send Message',
                       css_class="btn-block"),
            )
        )
