from django import forms

# signup
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
	"""Form con email para el registro de usuarios"""
	email = forms.EmailField(required=True, label='email', error_messages={'exists': 'Este correo ya está en uso'})

	class Meta:
		model = User 
		fields = ('username', 'email', 'password1', 'password2')

	def save(self, commit=True):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError(self.fields['email'].error_messages['exists'])
		return self.cleaned_data['email']


def should_be_empty(value):
	if value:
		raise forms.ValidationError('Bot ¬¬')
class ContactForm(forms.Form):
	"""Form de Contacto"""
	name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	forcefield = forms.CharField(required=False, widget=forms.HiddenInput, label="leave empty", validators=[should_be_empty])

