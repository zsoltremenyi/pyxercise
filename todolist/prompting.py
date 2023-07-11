def creating_todo():
    todo_list = []
    while True:
        todo = input("What tasks do you have for today? ")
        if todo:
            todo_list.append(todo)
        else:
            print("That's it?! Good bye then!")
            break

    return todo_list