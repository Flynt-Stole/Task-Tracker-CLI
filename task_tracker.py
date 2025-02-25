import json
print("TASK TRACKER APP")

a = int(input("enter the number of tasks you want to add: "))
tasks = {f"task_{i+1}": input(f"Task {i+1}: ") for i in range(a)}
prnt_this = (tasks.values())

with open("data.json" , "w") as file:
    json.dump(tasks , file , indent=4)

print("tasks to do: " , prnt_this)




stp = "stop"
while True:
    print("1. update a task...(updt)\n2. add a task...(add)\n3. remove a task...(rmv)\n4.mark a task as done...(done)\n5.mark a task as in progress...(ip)\n6.list all tasks...(lst)\n7.list done tasks...(lst_done)\n8.list in progress tasks...(lst_ip)")
    kaam = input("=> ")

    if kaam == "updt":
        print("enter task to update (0-9)")
        task_num = int(input())
        if 0 <= task_num <= 9:
            task_key = f"task_{task_num+1}"  # Convert to match original key format
            tasks[task_key] = input("Enter new task: ")
            print(f"updated tasks: {list(tasks.values())}")
            # Save all tasks to JSON file
            with open("data.json", "w") as file:
                json.dump(tasks, file, indent=4)
    elif kaam == "rmv":
        print("enter task to remove (0-9)")
        task_num = int(input())
        if 0 <= task_num <= 9:
            task_key = f"task_{task_num+1}"  # Convert to match original key format
            del tasks[task_key]
            print(f"updated tasks: {list(tasks.values())}")
            # Save all tasks to JSON file
            with open("data.json", "w") as file:
                json.dump(tasks, file, indent=4)
        else:
            print("Invalid task number. Please enter a number between 0 and 9")
    elif kaam == "add":
        print("enter task: )")
        a = int(input("enter the number of tasks you want to add: "))
        tasks = {f"task_{i+1}": input(f"Task {i+1}: ") for i in range(a)}
        print(f"updated tasks: {list(tasks.values())}")
            # Save all tasks to JSON file
        with open("data.json", "w") as file:
            json.dump(tasks, file, indent=4)
    elif kaam == "lst":
        try:
            with open("data.json", "r") as file:
                loaded_tasks = json.load(file)
            print("tasks to do: ", loaded_tasks)
        except FileNotFoundError:
            print("No tasks file found. Please add some tasks first.")
    elif kaam == "done":
        print("enter task to mark as done (0-9)")
        task_num = int(input())
        if 0 <= task_num <= 9:
            task_key = f"task_{task_num+1}"  # Convert to match original key format
            tasks[task_key] = tasks[task_key] + " (done)"
            print(f"updated tasks: {list(tasks.values())}")
    elif kaam == "ip":
        print("enter task to mark as in progress (0-9)")
        task_num = int(input())
        if 0 <= task_num <= 9:
            task_key = f"task_{task_num+1}"  # Convert to match original key format
            tasks[task_key] = tasks[task_key] + " (in progress)"
            print(f"updated tasks: {list(tasks.values())}")
    elif kaam == "lst_done":
        with open("data.json", "r") as file:
            loaded_tasks = json.load(file)
            print("done tasks: " , loaded_tasks)
    elif kaam == "lst_ip":
        with open("data.json", "r") as file:
            loaded_tasks = json.load(file)
            print("in progress tasks: " , loaded_tasks)
    elif kaam == "lst_ip":
        with open("data.json", "r") as file:
            loaded_tasks = json.load(file)
            print("in progress tasks: " , loaded_tasks)
    if kaam == stp:
        break

