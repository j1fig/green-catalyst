BROKER_URL = 'amqp://green:greencatalyst@localhost'
CELERY_RESULT_BACKEND = 'amqp://green:greencatalyst@localhost'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Lisbon'
CELERY_ENABLE_UTC = True
