from django.shortcuts import render, redirect
# test
from django.http import HttpResponse
# signup
from django.contrib.auth import authenticate, login
from .forms import UserCreateForm
# contact
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# sendgrid
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def test(request):

	return HttpResponse('<h1>successful</h1>')

def index(request):
	context={}
	return render(request, 'usuarios/index.html', context)

def signup(request):
	"""Signup - Victor Wooding"""
	if request.method == "POST":
		form = UserCreateForm(request.POST)
		print(form.errors)
		if form.is_valid():
			usuario_nuevo = form.save()
			usuario_nuevo = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
				)
			login(request, usuario_nuevo)
			return redirect('index')
	else:
		form = UserCreateForm()
	return render(request, 'registration/signup.html', {'form': form})



def contact(request):
	"""enviar email - Victor Wooding"""
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject ="mensaje de {}".format(form.cleaned_data['name'])
			message = form.cleaned_data['message']
			sender = form.cleaned_data['email']
			recipients = ['jesusgilberdugo@gmail.com']
			try:
				send_mail(subject, message, sender, recipients, fail_silently=True)
			except BadHeaderError:
				return HttpResponse("invalid header found")
			return HttpResponse("success... message has been sent")		
	return render(request, 'usuarios/contact.html', {'form': form})

from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string, get_template


def enviar_correo(asunto, contenido, email_server, clientes):
	context = {
		'nombre': "Jesus",
		'contenido': contenido
	}
	contenido = render_to_string('correo.html', context)
	contenido = get_template('correo.html')
	contenido.render(context)
	## version 1
	# email = EmailMessage(asunto, contenido, email_server, clientes)
	# email.fail_silently=False
	# email.send()
	## version 2
	email = EmailMultiAlternatives(asunto, 'prueba', email_server, clientes) 
	email.attach_alternative(contenido, 'text/html')
	email.send()
	## version 3
	# send_mail(asunto, contenido, email_server, clientes)
	return None

def correotest(request):
	asunto = 'test 2 de octubre'
	contenido = 'masterproelite'
	email_server = settings.EMAIL_HOST_USER
	clientes = [settings.EMAIL_HOST_USER]
	enviar_correo(asunto, contenido, email_server, clientes)
	return HttpResponse('<h1>Correo Enviado</h2>')


# def contact_sendgrid(request):
# 	"""enviar email - documentación sendgrid"""
# 	form = ContactForm()
# 	if request.method == "POST":
# 		form = ContactForm(request.POST)
# 		if form.is_valid():
# 			message = Mail(
# 				from_email=form.cleaned_data['email'],
# 				to_emails='jesusgilberdugo@gmail.com',
# 				subject="mensaje de {}".format(form.cleaned_data['name']),
# 				html_content='<strong>{}</strong>'.format(form.cleaned_data['message']))
# 			try:
# 				sg = SendGridAPIClient(settings.SENDGRID_API_KEY) #os.environ.get('SENDGRID_API_KEY')
# 				response = sg.send(message)
# 				print(response.status_code)
# 				print(response.body)
# 				print(response.headers)
# 			except Exception as e:
# 				print(e)
# 			return HttpResponse("success... message has been sent")		
# 	return render(request, 'usuarios/contact.html', {'form': form})