from data_processing import load_data, clean_data

def main():
    presenters, all_students, presentations, preferences = load_data()
    clean_data(presenters, all_students, presentations, preferences)
    