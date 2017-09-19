import os

def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with file data.
    """
    data = [] # creates an empty journal
    filename = get_full_pathname(name) # gets the filename using fullpath function

    if os.path.exists(filename): # loads the file one entry per line if it does exist
        with open(filename) as fileinput:
            for entry in fileinput.readlines():
                # print("Going to load: " + entry.rstrip())
                data.append(entry.rstrip())
    return data # returns a populated or an empty dataset


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('.', 'data', name + '.jrl'))
    print('..... saved to: {}'.format(filename))

    with open(filename, 'w') as fileout: # creates a writable file and stores the entries
        for entry in journal_data:
            fileout.write(entry + '\n')

def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'data', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)


