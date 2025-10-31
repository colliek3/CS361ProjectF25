# This file holds the object structure of a task object
# import as task
class task:
    def __init__(self, name, number, description, tags, priority):
        self.name = name #string
        self.number = number #int
        self.description = description #string
        self.tags = tags #list of strings
        self.priority = priority #int
    
    def print_info(self):
        print('number: ', self.number)
        print('name:', self.name)
        print('description:', self.description)
        print('tags:', self.tags)
        print('priority:', self.priority)

class user:
    def __init__(self, name, task_list=[], archive_list=[]):
        self.name = name # string
        self.task_list = task_list #list of task objects
        self.archive_list = archive_list #list of task objects
    
    def print_tasks(self):
        for task in self.task_list:
            task.print_info()
    
    def print_archive(self):
        for task in self.archive_list:
            task.print_info()