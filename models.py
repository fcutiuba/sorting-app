class Student:
    def __init__(self,user_id, first_name, last_name, email, preferences, is_presenter = False):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.preferences = preferences
        self.assigned_classes = [[None for _ in range(5)] for _ in range(5)]
        self.is_presenter = is_presenter
        

class Class:
    def __init__(self, name, ID, roster, presenter, min_students, max_students):
        self.name = name
        self.ID = ID
        self.roster = roster
        self.presenter = presenter
        self.min_students = min_students
        self.max_students = max_students
        