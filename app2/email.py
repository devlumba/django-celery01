from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_review_email(name, email, review_content):

    context = {
        'name': name,
        'email': email,
        'review_content': review_content,
    }

    email_subject = 'Thank you for your review'
    email_body = render_to_string('app2/email_message.txt', context)

    email = EmailMessage(email_subject, email_body,
                         settings.DEFAULT_FROM_EMAIL, [email, ])
    return email.send(fail_silently=False)
