from __future__ import absolute_import, unicode_literals
from proj.celery import app

from celery import shared_task
from celery.utils.log import get_task_logger

from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


# from .email import send_review_email

logger = get_task_logger(__name__)

# I've deleted old function and changed it with email.py contents, cuz that would be less complex


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review_content):

    context = {
        'name': name,
        'email': email,
        'review_content': review_content,
    }

    email_subject = 'Thank you for your review'
    email_body = render_to_string('app2/email_message.txt', context)

    email = EmailMessage(email_subject, email_body,
                         settings.DEFAULT_FROM_EMAIL, [email, ])
    logger.info("Sent review email")
    return email.send(fail_silently=False)

