from celery import Celery
from app.config import get_settings
import secrets


celery_app = Celery(__name__)

settings = get_settings()

REDIS_URL = settings.redis_url

celery_app.conf.broker_url = REDIS_URL

@celery_app.task
def random_function_task(name):
    print(f'who throws a shoe by {name}')

def setup_periodic_tasks(sender, *args, **kwargs):
    # print(randomly_generate_profit())
    pass


@celery_app.task
def random_profit_tasks():
    profit = secrets.SystemRandom().randint(100, 10000)
    print(profit)
    return profit




