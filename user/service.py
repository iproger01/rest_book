from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from books_rest.celery import app


@app.task(bind=True)
def send_email(request, *args):
    print('before we sending messege')

    msg = EmailMessage('Request Callback',
                       'Here is the message.', to=['golubenkovladislav99@gmail.com'])
    msg.send()

    # send_mail('Subject here', 'Here is the message.', 'shagvladislavgolubenko@gmail.com',
    #           ['golubenkovladislav99@gmail.com'], fail_silently=False)
    print('App wont to send messege')


