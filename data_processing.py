import pandas as pd 
from models import Student

def load_data(presenters, all_students, presentations, preferences): #loads data from csv files and makes it into dataframes + easier to work with 
    presenters = pd.read_csv(presenters)
    all_students = pd.read_csv(all_students) 
    presentations = pd.read_csv(presentations)
    preferences = pd.read_csv(preferences)
    
    return presenters, all_students, presentations, preferences
    
def clean_data(presenters, all_students, presentations, preferences): # cleans data, making all emails lowercase + marking presenters
    # make the presenters dataframe be all lowercase
    presenters["Email"] = presenters["Email"].str.lower()
    all_students["Email"] = all_students["Email"].str.lower()
    
    # mark presenters
    all_students["is_presenter"] = all_students["Email"].isin(presenters["Email"])
    
    return presenters, all_students, presentations, preferences

def create_student_objects(all_students, presenters): # takes the data from the all_students dataframe and creates a dictionary of students
    student_dict = {}
    for _, row in all_students.iterrows():
        email = row["Email"]
        user_id = row["UserID"]
        last_name = row["Last"]
        first_name = row["First"]
        is_presenter = row["is_presenter"]
        
        if not is_presenter:
            preferences_row = preferences[preferences["Email Address"] == email].iloc[0,5:] #gets just the preferences
            preferences = [preferences_row[i:i+5] for i in range(0, len(preferences_row), 5)] #splits the preferences into a list of lists
        else:
            preferences = None
        student = Student(user_id, first_name, last_name, email, preferences, is_presenter)
        
        student_dict[email] = student
    

presenters, all_students, presentations, preferences = load_data("presenters.csv", "allstudents.csv", "presentations-caps.csv", "preferences-numbers.csv")
clean_data(presenters, all_students, presentations, preferences)