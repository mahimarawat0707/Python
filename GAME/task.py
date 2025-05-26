def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def addtask(my_list):
    task = input("🆕 Enter your new task: ").strip().title()
    if task:
        my_list.append(task)
        save_tasks(my_list)
        print(f"✅ Task added: {task}")
    else:
        print("⚠️ Task can't be empty!")

def viewtask(my_list):
    if not my_list:
        print("📭 Your task list is empty!")
    else:
        print("\n📋 Your tasks:")
        for index, task in enumerate(my_list, 1):
            print(f"{index}. {task}")

def removetask(my_list):
    if not my_list:
        print("❌ Your task list is already empty!")
        return
    viewtask(my_list)
    try:
        rem = int(input("🔢 Enter the number of the task to remove: "))
        if 1 <= rem <= len(my_list):
            removed = my_list.pop(rem - 1)
            save_tasks(my_list)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def to_do_task_app():
    my_list = load_tasks()

    while True:
        print("\n📝=== To-Do List Menu ===")
        print("1. ➕ Add Task")
        print("2. 📋 View Tasks")
        print("3. ❌ Remove Task")
        print("4. 🚪 Exit")

        choice = input("👉 What do you want to do (1-4)? : ").strip()

        if choice == "1":
            addtask(my_list)
        elif choice == "2":
            viewtask(my_list)
        elif choice == "3":
            removetask(my_list)
        elif choice == "4":
            print("👋 Thank you for using the To-Do List. Bye!")
            break
        else:
            print("⚠️ Invalid input! Please choose between 1 and 4.")

to_do_task_app()