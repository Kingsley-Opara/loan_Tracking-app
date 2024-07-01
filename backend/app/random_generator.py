import secrets

# from worker import random_profit_tasks

def randomly_generate_profit():
    profit = secrets.SystemRandom().randint(100, 10000)
    # print(random_profit_tasks.delay())
    return profit
