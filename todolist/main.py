from text_handling import TextHandler
import prompting

add_or_del = input("Adding or deleting task? (a or d) ")
text_handler = TextHandler(prompting.creating_todo(), "to_do_list.txt")

if add_or_del == "a":
    print("Tasks have been added.")
    text_handler.adding_tasks()
elif add_or_del == "d":
    print("Tasks have been deleted.")
    text_handler.del_task()


print(f"Your tasks:\n{text_handler.read_text()}")