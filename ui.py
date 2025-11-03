# Basic UI for final project
# Katherine Collier
import time
import random
import task_object as task
import copy

"""
welcome(user)

This function operates the welcome UI, which opens every time the program loads.
The user is greeted with a welcome message, then is allows to navigate to the main
page or getting help. 

parameters: user- user object (from task_object.py)
returns: None
"""
def welcome(user):
    print("Welcome to Task Manager (selfmade edition)!")
    print('')
    # still coming up with something better, details are a wip here

    while True:
        # allows the user to 
        nav = input("To view your to-do list, input 1, or to get help input 2: ")

        if nav == '1':
            # take user to task view
            # call task function
            print("Loading task page...")
            task_view(user)
            break

        elif nav == '2':
            # take user to help page (call help function)
            print("Loading help page...")
            help(user)
            break
        
        else:
            # error/misinput handling
            print("Unknown Option, please retry")

"""
help(user)

This function operates the help page, which essentially just prints help information.
The user can navigate back to the welcome page.

parameters: user - user object (from task_object.py)
returns: None
"""
def help(user):
    # Prints help information for help page
    print("This software allows you to make a customizable to-do list with tagged tasks and an archive. \n" \
    "Use task tags to improve your organization and categorize your tasks, and use \n" \
    "the archive to keep a record of all completed tasks. You can sort your tasks by priority, \n" \
    "oldest to newest, or filter by specific tags. \n" \
    "Email for questions: colliek3@oregonstate.edu")

    # navigation block
    while True:
        nav = input("Input 1 to return home: ")

        if nav == '1':
            # return home
            welcome(user)
            break

        else:
            # error/misinput handling
            print("Unknown Option, please retry")
            time.sleep(1)

"""
task_view(user)

This function prints all the user's tasks if they exist. If they don't,
prompts the user to add a task.

parameters: user- user object (from task_object.py)
returns: None
"""
def task_view(user):
    # if the tasks exist, print them
    print('')
    if user.task_list:
        user.print_tasks()
        while True:
            sort = input('Would you like to sort these tasks a different way? (y/n): ')
            if sort == 'y':
                while True:
                    method = input('Would you like to sort by priority (p) , sort by number (n),\n' \
                    'or filter for a specific tag (tag)?: ')
                    if method == 'p':
                        # call sort by priority
                        sort_by_priority(user)
                        break
                    
                    elif method == 'n':
                        # call sort by number
                        sort_by_number(user)
                        break
                    
                    elif method == 'tag':
                        # call filter by tag
                        filter_by_tag(user)
                        break
                
                    else: 
                        print('Unknown option. Try again?')
        
            elif sort == 'n':
                break

            else:
                print('Unknown option. Try again? ')

    # if not, asks user to add tasks. 
    else:
        print('No tasks here. Input add to add a task!')
    # call nav
    page_nav(user)

"""
add_task(user)

This function allows the user to add a task to their task list. The user is prompted to 
add a title, description, tags, and priority- these attributes, along with a 'number' 
which tracks the age of tasks over time (older task, higher number), are added to a new 
task object within the user object and saved. 

parameters: user- user object (from task_object.py)
returns: None
"""
def add_task(user):
    # user adds name and description to a new task
    name = input("Enter the title of your new task: ")
    description = input("Describe your task: ")
    # number is the task's original position in the list
    number = len(user.task_list) + 1
    
    # initalizes empty tag list
    tag_list = []

    # users can add tags to their task
    while True:
        yesorno = input("Would you like to add tags? (y/n): ")

        # user adds a new tag as many times as they want
        if yesorno == 'y':
            new_tag = input("Add tag: ")
            tag_list.append(new_tag)
        
        # once done, they enter n
        elif yesorno == 'n':
            break

        else: 
            # error/misinput handling
            print('unknown option. try again?')
    
    # user can add a priority level (if they want)
    while True:
        pri = input('Would you like to assign a priority to this task? (y/n): ')
        if pri == 'y':
            priority = input("Add priority (smallest int is the highest priority): ")
            try: 
                int(priority)
                break

            except:
                ValueError
        
        elif pri == 'n':
            # default priority is very big (user chooses to not assign)
            priority = 10000000
            break

        else:
            print('unknown option. try again?')
    
    # make a new task with all the information user provided
    new_task = task.task(name, number, description, tag_list, int(priority))
    print('')
    new_task.print_info()

    # allows user to check if all their inputs were correct
    while True:
        check = input('Is all information correct? (y/n): ')
        
        # save task to user's task list
        if check == 'y':
            print('Great! Saving task...')
            user.task_list.append(new_task)
            task_view(user)
            break
        
        elif check == 'n':
            # avoid undefined memory
            del new_task
            add_task(user)
            break
        
        else:
            print('Unknown option. Try again?')

    # call nav
    page_nav(user)

"""
archive(user)

This function allows the user to move an existing task into the archive list. This allows for
a distinction between tasks that are currrently in progress and former tasks. 

parameters: user- user object (from task_object.py)
returns: None
"""
def archive(user):
    # if the user has archived tasks, print them
    if user.archive_list:
        user.print_archive()
    else:
        print('you have no archived tasks. you can archive a task from its full page view.')
    # call nav
    page_nav(user)

"""
this_task(user)

This function allows the user to view a specific task in more detail, and archive the 
task if they want to. 

parameters: user- user object (from task_object.py)
returns: None
"""
def this_task(user, index):
    # index == task number == actual index in the task_list
    user.task_list[index - 1].print_info()

    while True:
        # check if user wants to archive the task
        arch = input('Would you like to archive this task? (y/n): ')
        
        # encourage tinkerers to tinker mindfully
        if arch == 'y':
            conf = input('Are you sure? This action cannot be undone. (y/n): ')

            if conf == 'y':   
                # copy task into user's archive list
                to_be_archived = copy.deepcopy(user.task_list[index - 1])
                user.archive_list.append(to_be_archived)

                # delete the old task from task list
                del user.task_list[index - 1]
                for i in range(index - 1, len(user.task_list)):
                    user.task_list[i].number -= 1
                task_view(user)
                break

            else: 
                break
        
        elif arch == 'n':
            break

        else:
            print('Unknown option. Try again?')
    # call nav
    page_nav(user)

"""
save_and_exit(user)

This function writes all task and archive list data to text files. The data is
formatted in a way that is easy to process for the following functions. 

parameters: user- user object (from task_object.py)
returns: None
"""
def save_and_exit(user):
    # write all task_list data to userdata.txt
    with open('userdata.txt', 'w') as file:
        file.write(str(len(user.task_list)) + '\n')
        for task in user.task_list:
            file.write(str(task.number) + '\n')
            file.write(task.name + '\n')
            file.write(task.description + '\n')
            file.write(str(len(task.tags)) + '\n')
            for tag in task.tags:
                file.write(tag + '\n')
            file.write(str(task.priority) + '\n')
            file.write('\n')

    # write all archive_list data to archivedata.txt
    with open('archivedata.txt', 'w') as file:
        file.write(str(len(user.archive_list)) + '\n')
        for task in user.archive_list:
            file.write(str(task.number) + '\n')
            file.write(task.name + '\n')
            file.write(task.description + '\n')
            file.write(str(len(task.tags)) + '\n')
            for tag in task.tags:
                file.write(tag + '\n')
            file.write(str(task.priority) + '\n')
            file.write('\n')

"""
load_from_file(user)

This function loads any previously saved user data back into modifiable task objects.
The task_list and archive_list are made separately. 

parameters: user- user object (from task_object.py)
returns: None
"""
def load_from_file(user):
    # if user has a file with data in it, turn them into tasks
    # first line is length, then each line after is a specific element.
    # blank line between tasks
    with open('userdata.txt', 'r+') as file:
        line1 = file.readline()
        if line1 != '':
            num = int(line1)

            # iterates for the amount of tasks the user saved
            for i in range(0, num):
                number = file.readline().strip()
                name = file.readline().strip()
                description = file.readline().strip()
                tags = []
                num_tags = int(file.readline().strip())
            
                # iterates over amount of tags
                for j in range(0, num_tags):
                    tag = file.readline().strip()
                    tags.append(tag)

                priority = file.readline().strip()
                file.readline()

                # make a new task object, append it to the task_list
                new_task = task.task(name, int(number), description, tags, int(priority))
                user.task_list.append(new_task)

    # also load user's archived tasks
    with open('archivedata.txt', 'r+') as file:
        line1 = file.readline()
        if line1 != '':
            num = int(line1)

            for i in range(0, num):
                number = file.readline().strip()
                name = file.readline().strip()
                description = file.readline().strip()
                tags = []
                num_tags = int(file.readline().strip())

                for j in range(0, num_tags):
                    tag = file.readline().strip()
                    tags.append(tag)
                
                priority = file.readline().strip()
                file.readline()
                new_task = task.task(name, int(number), description, tags, int(priority))
                user.archive_list.append(new_task)

"""
sort_by_number(user)

This function allows the user to sort all tasks in their list by age, where the
smallest number is the oldest. This allows the user to frame data in a way they want
to see. 

parameters: user- user object (from task_object.py)
returns: None
"""
def sort_by_number(user):
    # sort the tasks by number
    user.task_list.sort(key=lambda task:task.number)
    user.print_tasks()

"""
sort_by_priority(user)

This function allows the user to sort their tasks by priority, if they set different priorities
when adding tasks. 

parameters: user- user object (from task_object.py)
returns: None
"""
def sort_by_priority(user):
    # sort by priority level 
    user.task_list.sort(key=lambda task:task.priority)
    user.print_tasks()

"""
filter_by_tag(user)

This function allows the user to only see tasks that are tagged with a specific tag. This allows
the user to only see tasks relevant to their specific needs. 

parameters: user- user object (from task_object.py)
returns: None
"""
def filter_by_tag(user):
    # only displays tasks with a specific tag
    while True:
        user_input = input("What tag would you like to search by?: ")
        tag_exists = False

        # if a matching tag exists, print the tag
        for task in user.task_list:
            for tag in task.tags:
                if tag == user_input:
                    tag_exists = True
                    task.print_info()
        # print all tasks before breaking
        if tag_exists == True:
            break
        # or check all tasks before breaking
        else:
            print('Input is not a current tag. Retry?')

"""
page_nav(user)

This function controls most of the basic navigation options presented to the user. 
It allows the user to move between pages, exit, and see more specific information
about specific tasks. 

parameters: user- user object (from task_object.py)
returns: None
"""
def page_nav(user):
    # Most pages have duplicate navigation - one function -> reusability
    while True:
        nav = input("Input 'w' for welcome, 'e' to exit, 'h' for help, \n'archive' for archive, " \
        "'add' to add a new task, 't' to see to-do list \n or a task number to see more: ")

        # welcome page
        if nav == 'w':
            print("Loading Welcome...")
            time.sleep(1)
            welcome(user)
            break
        
        # exit program
        elif nav == 'e':
            save_and_exit(user)
            exit()

        # view all tasks
        elif nav == 't':
            print('Loading Tasks...')
            time.sleep(1)
            task_view(user)
            break
        
        # help page
        elif nav == 'h':
            print("Loading Help...")
            time.sleep(1)
            help(user)
            break
        
        # see archived tasks
        elif nav == 'archive':
            print("Loading Archive...")
            time.sleep(1)
            archive(user)
            break
        
        # add a new task
        elif nav == 'add':
            print("Initializing...")
            time.sleep(1)
            add_task(user)
            break
        
        # error check nav is an int before loading indiv task
        try:
            int(nav)
            # needs to be in range of tasks
            if int(nav) in range(0, len(user.task_list)+ 1):
                print("Loading Task...")
                time.sleep(1)
                this_task(user, int(nav))
            break
        except ValueError:
            print('Unknown option, retry')

def main():
    name = ''
    # initialize blank user
    user = task.user(name)
    # if the user data files have data, load it
    load_from_file(user)
    welcome(user)

if __name__ == "__main__":
    main()