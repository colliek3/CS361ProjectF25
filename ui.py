# Basic UI for final project
# Katherine Collier
import time
import random
import task_object as task
import copy

def welcome(user):
    print("Welcome to Task Manager (selfmade edition)!")
    # still coming up with something better, details are a wip here

    while True:

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
            time.sleep(1)
            help()
            break
        
        else:
            print("Unknown Option, please retry")
            time.sleep(1)

def help():
    # Prints help information for help page
    print("This software allows you to make a customizable to-do list with tagged tasks and an archive. \n" \
    "Use task tags to improve your organization and categorize your tasks, and use \n" \
    "the archive to keep a record of all completed tasks. \n" \
    "Email for questions: colliek3@oregonstate.edu")

    while True:
        nav = input("Input 1 to return home: ")

        if nav == '1':
            # return home
            welcome()
            break

        else:
            print("Unknown Option, please retry")
            time.sleep(1)

def task_view(user):
    if user.task_list:
        user.print_tasks()
    else:
        print('no tasks here. enter add to add a task!')
    page_nav(user)

def add_task(user):
    # Allows the user to define a new task based on their descriptions
    name = input("Enter the title of your new task: ")
    description = input("Describe your task: ")
    number = len(user.task_list) + 1
    
    tag_list = []

    while True:
        yesorno = input("Would you like to add tags? (y/n): ")

        if yesorno == 'y':
            new_tag = input("Add tag: ")
            tag_list.append(new_tag)
        
        elif yesorno == 'n':
            break

        else: 
            print('unknown option. try again?')
    
    while True:
        pri = input('Would you like to assign a priority to this task? (y/n):')
        if pri == 'y':
            priority = input("Add priority: ")
            break
        
        elif pri == 'n':
            priority = -1
            break

        else:
            print('unknown option. try again?')
    
    new_task = task.task(name, number, description, tag_list, priority)

    new_task.print_info()

    while True:
        check = input('Is all information correct? (y/n):')
        
        if check == 'y':
            print('great! saving task...')
            user.task_list.append(new_task)
            task_view(user)
            break
        
        elif check == 'n':
            add_task(user)
            break
        
        else:
            print('try again')

    page_nav(user)

def archive(user):
    if user.archive_list:
        user.print_archive()
    else:
        print('you have no archived tasks.you can archive a task from its full page view.')
    # call nav
    page_nav(user)

def this_task(user, index):
    # index == task number == actual index in the task_list
    user.task_list[index - 1].print_info()

    while True:
        arch = input('Would you like to archive this task? (y/n): ')
        
        if arch == 'y':
            # move task to archive, then return to task view
            to_be_archived = copy.deepcopy(user.task_list[index - 1])
            user.archive_list.append(to_be_archived)

            del user.task_list[index - 1]
            for i in range(index - 1, len(user.task_list)):
                user.task_list[i].number -= 1
            task_view(user)
            break
        elif arch == 'n':
            break

        else:
            print('unknown option. try again?')
    # call nav
    page_nav(user)

def page_nav(user):
    # Most pages have duplicate navigation
    # So this helps manage that
    while True:
        nav = input("Input 'w' to return to welcome, 'e' to exit program, 'h' to get help, \n'archive' to see all tasks, " \
        "'add' to add a new task, 't' to return to your to-do list \n or the task number to see more details: ")

        if nav == 'w':
            print("Loading Welcome...")
            time.sleep(1)
            welcome(user)
            break

        elif nav == 'e':
            exit()

        elif nav == 't':
            print('Loading Tasks...')
            task_view(user)
            break

        elif nav == 'h':
            print("Loading Help...")
            time.sleep(1)
            help()
            break

        elif nav == 'archive':
            print("Loading Archive...")
            time.sleep(1)
            archive(user)
            break

        elif nav == 'add':
            print("Initializing...")
            time.sleep(1)
            add_task(user)
            break

        try:
            int(nav)
            # needs to be in range of tasks (class of to-do list w member list)
            if int(nav) in range(0, len(user.task_list())):
                print("Loading Task...")
                time.sleep(1)
                this_task(user, int(nav))
            break
        except ValueError:
            print('Unknown option, retry')

def main():
    name = ''
    user = task.user(name)
    welcome(user)

if __name__ == "__main__":
    main()