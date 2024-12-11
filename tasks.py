import celery

queue = celery.Celery("tasks")

def legacy_task(queue: str, *args, **kwargs):
    return queue.task(*args, **kwargs, queue=queue, base=celery.Task)