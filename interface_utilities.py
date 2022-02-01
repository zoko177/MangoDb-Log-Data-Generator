import datetime
import random

from mangoSetup import Mangodb

db = Mangodb()
locked_items = ["_id", "number of data", "time random from"]


def random_date(end_date):
    start = datetime.datetime.now()
    return (start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(int((end_date - start).total_seconds()), 0),
    )).replace(microsecond=0)


def fun_info():
    print("Information:")
    print("'Create st' - Create base structure and pushes to database")
    print("'Add' - Add item to structure or change existing one")
    print("'Show' - Show current structure")
    print("'Delete' - Delete item from structure")
    print("'Change Date' - Change starting date to randomize data from")
    print("'Change Number' - Change the number of data to generate")
    print("'Create' - Create randomized data according to structure and push it to managoDB")
    print("Locked items for add and delete:"+str(locked_items))
    print()


def create_structure():
    structure_test = {
        "_id": 1,
        "Number of Data": 100,
        "Time Random From": "1/1/2020 6:50 AM",
        "Name": ['test1', 'test2', 'test3', 'test4', 'test6'],
        "Error": ['Critical', 'Error', 'General']
    }
    structure_test["Time Random From"] = datetime.datetime.strptime(structure_test.get("Time Random From"),
                                                                    '%m/%d/%Y %I:%M %p')
    db.push_structure(structure_test)
    print("Base structure created")


def add_to_structure():
    st_name = input("Insert item name to add to structure\n")
    if st_name.lower() in locked_items:
        print("Cannot change this item")
    else:
        st_data = (input("Insert items to randomize from with ',' in between items\n")).split(',')
        structure = db.get_structure()
        structure[st_name] = st_data
        db.push_structure(structure)
        print("Item added\n")


def show_structure():
    structure = db.get_structure()
    if structure is None:
        print("Structure not exit")
        return
    for i in structure.items():
        print(i[0] + ": " + str(i[1]))
    print()


def delete_from_show_structure():
    name_to_delete = input("Enter name to delete item from structure\n")
    structure = db.get_structure()
    if name_to_delete.lower() in locked_items:
        print("Cannot delete this item")
    elif name_to_delete not in structure:
        print("Not exits\n")
    else:
        structure.pop(name_to_delete)
        db.push_structure(structure)
        print("Item deleted from structure\n")


def change_structure_date():
    new_date = input("Enter new date as to following:\nExample: '1/1/2020 6:50 AM'\n")
    try:
        date = datetime.datetime.strptime(new_date, '%m/%d/%Y %I:%M %p')
    except:
        print("Wrong date format")
        return
    structure = db.get_structure()
    structure["Time Random From"] = date
    db.push_structure(structure)
    print("Date changed\n")


def change_number_of_tests():
    num = int(input("Enter new number of tests to generate\n"))
    structure = db.get_structure()
    structure["Number of Data"] = num
    db.push_structure(structure)
    print("Number of data to generate changed\n")


def create_generated_data():
    structure = db.get_structure()
    data_head = list(structure)[2:]
    generated_data = []
    for i in range(structure["Number of Data"]):
        tempDic = {"_id": i + 1}
        for j in data_head:
            if j == "Time Random From":
                tempDic["Time"] = random_date(structure[j])
                continue
            tempDic[j] = structure[j][random.randint(0, len(structure[j]) - 1)]
        generated_data.append(tempDic)
    generated_data.sort(key=lambda d: d['Time'])
    for i in range(len(generated_data)): generated_data[i]["_id"] = i + 1
    db.push_data(generated_data)
    print("Data generated and pushed to db successfully")

