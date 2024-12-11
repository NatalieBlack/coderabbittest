import re
from tasks import legacy_task

@legacy_task(queue="normal")
def some_task(input) -> None:
    return re.sub("!@#$%^&*()", "", input)