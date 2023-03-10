from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger

#from ..rabbit.celery import app
from celery import shared_task
from .emalil import send_review_email

logger = get_task_logger(__name__)

#@app.task(name='send_review_email_task')
@shared_task
def send_review_email_task(name, email, review):
    logger.info('Sent review email')
    return send_review_email(name, email, review)