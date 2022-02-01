import interface_utilities as iu


def myInterface():
    print("For all commands type 'Info'\nTo Exit enter '0'")
    while (1):
        command = input("Enter Command:\n")
        match command.lower():
            case "create st":
                print("create structure")
            case "add":
                iu.add_to_structure()
            case "show":
                iu.show_structure()
            case "delete":
                iu.delete_from_show_structure()
            case "change date":
                iu.change_structure_date()
            case "create":
                iu.create_generated_data()
            case "info":
                iu.fun_info()
            case "change number":
                iu.change_number_of_tests()

            case "0":
                print("Job's Done")
                break
            case _:
                print("Command no exits")
