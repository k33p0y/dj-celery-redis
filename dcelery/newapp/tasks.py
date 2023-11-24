from celery import shared_task

@shared_task
def sharedtask(data):
    print(data)
    for i in range(1, 100):
        print(i)
    return data