import re
from tasks import legacy_task

@legacy_task(queue="normal")
def update_online(input) -> None:
    return re.sub("!@#$%^&*()", "", input)