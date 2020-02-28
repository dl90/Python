import pickle
import reminder
import reminder_storage
import os.path as path


class Program:

    def __init__(self):
        self.__storage = reminder_storage.ReminderStorage()
        self.__state = True
        self.__action = None

    def run(self):
        main_menu = (
            "\n\tReminders Menu:\n\n"
            "\t1. Show all reminders\n"
            "\t2. Search reminders\n"
            "\t3. Add new reminders\n"
            "\t4. Modify existing reminders\n"
            "\t5. Export reminders\n"
            "\t6. Import reminders\n"
            "\t7. Exit (lose all unsaved reminders)\n"
            )

        while self.__state:
            print(main_menu)

            try:
                self.__action = int(input("Enter an option: ").strip())
            except:
                print("Incorrect input. Please enter a valid option.")
            
            if self.__action or self.__action == 0:
                if self.__action == 1:
                    print("Showing all reminders...\n")
                    self.show_all_reminders()
                    self.__action = 0
                elif self.__action == 2:
                    print("Searching reminders...\n")
                    self.search_reminder_menu()
                    self.__action = 0
                elif self.__action == 3:
                    print("Adding new reminder...\n")
                    self.add_new_reminder()
                    self.__action = 0
                elif self.__action == 4:
                    print("Modify existing reminder...\n")
                    self.modify_reminder()
                    self.__action = 0
                elif self.__action == 5:
                    print("Export reminders...\n")
                    self.export_reminder()
                    self.__action = 0
                elif self.__action == 6:
                    print("Import reminders...\n")
                    self.import_reminder()
                    self.__action = 0
                elif self.__action == 7:
                    print("\nExiting program...\n")
                    self.__action = 0
                    self.__state = False
                else:
                    print("Please enter a valid option.")


    def show_all_reminders(self):
        if len(self.__storage.storage) == 0:
            print("There are no stored reminders")
        else:
            for reminder in self.__storage.storage:
                print(str(self.__storage.storage.index(reminder) + 1) + ". " + reminder.tag)
                print(reminder.reminder)


    def add_new_reminder(self):
        reminder_ = input("Specify your reminder: ").strip()
        tag_ = input("Specify your reminder's tag (comma seperated if multiple): ").strip()
        new_reminder = reminder.Reminder(tag_, reminder_)
        self.__storage.append(new_reminder)
        print("Your reminder has been added.\n")


    def add_existing_reminder(self, reminder_):
        self.__storage.append(reminder_)


    def search_reminder_menu(self):
        action = True
        search_menu = (
        "\n\tHow would you like to search your reminders?\n"
        "\t1. By tag\n"
        "\t2. By reminder\n"
        "\t3. Both\n"
        "\t4. Back to Main Menu\n"
        "\t5. Exit program (lose all unsaved reminders)\n"
        )

        while action:
            print(search_menu)
            try:
                action_ = int(input("Enter an option: ").strip())
            except:
                print("Incorrect input. Please enter a valid option.\n")
                action_ = 0

            if action_ == 1:
                self.search_reminders_by_tag()
                action = 0
            elif action_ == 2:
                self.search_reminders_by_reminder()
                action = 0
            elif action_ == 3:
                self.search_reminders_by_tag_and_reminder()
                action = 0
            elif action_ == 4:
                print("Returning to main menu")
                action = False
            elif action_ == 5:
                print("Exiting program")
                action = False
                self.__state = False
            else:
                print("Please enter a valid option.")

    # def search_reminder(self, type):
    #     query_message = {
    #         "tag": "Enter tag: ",
    #         "text": "Enter text: ",
    #         "both": "Enter search term: "
    #     }
    #     input_ = input(query_message["tag"]).strip()
    #     not_found = True

    #     def by_tag(reminder_obj, input, state):
    #         if input in reminder_obj.tag:
    #             print(str(self.__storage.storage.index(reminder_obj) + 1) + ". " + reminder_obj.tag)
    #             print(reminder_obj.reminder)
    #             state = True
    #             return state

    #     if len(input_) > 0:
    #         print("\n---------------")
            # for reminder_obj in self.__storage.storage:
            #     if input_ in reminder_obj.
        

    def search_reminders_by_tag(self):
        tag_ = input("Enter tag: ").strip()
        not_found = True
        if len(tag_) > 0:
            print("\n---------------")
            for reminder_obj in self.__storage.storage:
                if tag_ in reminder_obj.tag:
                    not_found = False
                    print(str(self.__storage.storage.index(reminder_obj) + 1) + ". " + reminder_obj.tag)
                    print(reminder_obj.reminder)
            print("---------------")
            if(not_found):
                print("No reminders found with tag: " + tag_ + "\n")
        else:
            print("Incorrect input.\n")


    def search_reminders_by_reminder(self):
        reminder_ = input("Enter text: ").strip()
        not_found = True
        if len(reminder_) > 0:
            print("\n---------------")
            for reminder_obj in self.__storage.storage:
                if reminder_ in reminder_obj.reminder:
                    not_found = False
                    print(str(self.__storage.storage.index(reminder_obj) + 1) + ". " + reminder_obj.tag)
                    print(reminder_obj.reminder)
            print("---------------")
            if(not_found):
                print("No reminders found containing: " + reminder_ + "\n")
        else:
            print("Incorrect input.\n")


    def search_reminders_by_tag_and_reminder(self):
        input_ = input("Enter search term: ").strip()
        not_found = True
        if len(input_) > 0:
            print("\n---------------")
            for reminder_obj in self.__storage.storage:
                if (input_ in reminder_obj.tag) or (input_ in reminder_obj.reminder):
                    not_found = False
                    print(str(self.__storage.storage.index(reminder_obj) + 1) + ". " + reminder_obj.tag)
                    print(reminder_obj.reminder)
            print("---------------")
            if(not_found):
                print("No reminders with tag or text found containing: " + input_ + "\n")
        else:
            print("Incorrect input.\n")


    def modify_reminder(self):
        limit = len(self.__storage.storage)
        invalid = True
        _id = None
        modify_menu = (
        "\n\tHow would you like modify this reminder?\n"
        "\t1. Replace\n"
        "\t2. Concat\n"
        "\t3. Delete\n"
        "\t4. Back to Main Menu\n"
        "\t5. Exit program (lose all unsaved reminders)\n"
        )
        action = True

        def replace_reminder():
            _input = input("Enter new reminder to replace: ").strip()
            if(len(_input) > 0):
                self.__storage.storage[_id - 1].reminder = _input
                print("Your reminder has been replaced with: " + self.__storage.storage[_id - 1].reminder)

        def append_reminder():
            _input = input("Enter things to add to reminder: ").strip()
            if(len(_input) > 0):
                updated_reminder = self.__storage.storage[_id - 1].reminder + " " + _input
                self.__storage.storage[_id - 1].reminder = updated_reminder
                print("Your reminder has been updated: " + self.__storage.storage[_id - 1].reminder)
        
        def remove_reminder():
            prompt = input("Are you sure you want to remove reminder id '" + str(_id) + "' (yes/no): ").strip() 
            if prompt.upper() == "YES":
                reminder_obj = self.__storage.storage[_id - 1]
                self.__storage.storage.remove(reminder_obj)
                print("Reminder with id '" + str(_id) + "' has been removed.\n")

        while invalid:
            try:
                _id = int(input("Enter reminder id (press 0 to exit): ").strip())
                if (_id > 0) and (_id <= limit):
                    invalid = False
                # elif _id == 0:
                #     invalid = False
            except:
                print("Incorrect input. Try again.")

        while action and (type(_id) == int): #and _id != 0
            print(modify_menu)
            try:
                action_ = int(input("Enter an option: ").strip())
            except:
                print("Incorrect input. Please enter a valid option.")
                action_ = 0
            if action_ == 1:
                replace_reminder()
                action = False
                action_ = 0
            elif action_ == 2:
                append_reminder()
                action = False
                action_ = 0
            elif action_ == 3:
                remove_reminder()
                action = False
                action_ = 0
            elif action_ == 4:
                action = False
                action_ = 0
            elif action_ == 5:
                action = False
                action_ = 0
                self.__state = False
            else:
                print("Please enter a valid option.")


    def export_reminder(self):
        filename = input("\tSpecify export file name: ").strip()

        if len(filename) == 0:
            filename = "data"
        out_file = open(filename, "wb")
        pickle.dump(self.__storage.storage, out_file)
        out_file.close()
        print("\tReminders successfully saved as: " + filename + "\n")


    def import_reminder(self):
        filename = input("\tSpecify import file name: ").strip()

        if len(filename) == 0:
            filename = "data"
        if path.exists(filename):
            in_file = open(filename, "rb")
            self.__storage.storage.extend(pickle.load(in_file))
            in_file.close()
            print("\tReminders successfully loaded from:  " + filename + "\n")
        else:
            print("This file does not exist.")


program = Program()
program.run()
