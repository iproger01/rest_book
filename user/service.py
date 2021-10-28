from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from books_rest.celery import app


@app.task(bind=True)
def send_email():
    subject = 'Тема сообщения'
    message = 'Вам отправленно сообщение'
    from_email = 'shagvladislavgolubenko@gmail.com'
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['golubenkovladislav99@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')