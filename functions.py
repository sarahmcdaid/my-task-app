FILEPATH = 'tasks.txt'

def get_tasks(filepath=FILEPATH):
    """ Read a text file and return the list of
    task items.
    """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Write a task items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)

