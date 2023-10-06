class tasks:


    def __init__(self, course, assignment, due_date, is_favourite):
        self.course = course
        self.assignment = assignment
        self.due_date = due_date
        self.is_favourite = is_favourite

    def print_list(self):
        print(f"Course: {self.course}")
        print(f"Assignment: {self.assignment}")
        print(f"Due Date: {self.due_date}")
        print(f"Is Favourite?: {self.is_favourite}")



    