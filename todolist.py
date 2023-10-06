from tasks import tasks
import time


def create_file_name():
    timestamp = int(time.time())
    name = input("What do you want to name your file? ")
    return (name + " " + str(timestamp))
    
def write_to_file(to_do, file):
    for task in to_do:
        file.write(f"Course: {task.course}\n")
        file.write(f"Assignment: {task.assignment}\n")
        file.write(f"Due Date: {task.due_date}\n")
        file.write(f"Is Favorite?: {task.is_favourite}\n")
        file.write("\n")

def add_task():
    course = input("What is the course name? ")
    assignment = input("What is the assignment name? ")
    due_date = input("When is it due? ")
    is_favourite = input("Favourite Task? (yes or no): ").lower()

    while is_favourite not in ("yes", "y", "no", "n"):
        is_favourite = input("Should it be favorited? Type 'yes' or 'no': ").lower()

    if is_favourite == "yes" or is_favourite == "y":
        is_favourite = True
    else:
        is_favourite = False

    new_task = tasks(course, assignment, due_date, is_favourite)
    to_do.append(new_task)

to_do = []
file_name = None

while True:
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter your choice: ")
    while choice not in ("1", "2", "3", "4"):
        choice = input("Please enter a valid input: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        for index, task in enumerate(to_do):
            print("---------------------")
            print(f"Task {index+1}:")
            task.print_list()
    elif choice == "3":
        if file_name == None:
            file_name = create_file_name()
        file = open(file_name, 'w')
        write_to_file(to_do, file)
        file.close()
    elif choice == "4":
        break
