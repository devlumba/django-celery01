from __future__ import absolute_import, unicode_literals
from proj.celery import app

from celery import shared_task
from celery.utils.log import get_task_logger

from .email import send_review_email

logger = get_task_logger(__name__)


@shared_task(name="send_review_email_task")
def send_review_email_task(name, email, review_content):
    logger.info("Sent review email")
    return send_review_email(name, email, review_content)
