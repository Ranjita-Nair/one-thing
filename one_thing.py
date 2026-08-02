import sys

tasks = [
    "Make form for new project requests",
    "GENAI node for performance testing",
    "Brainstorm on how to automate the autogenerating documentation of test strategy",
    "Make a general template for automating different sections",
    "Make human in loop steps",
]
def pick_one(tasks):
    """Crude rule: the shortest task is usually the easiest to start."""
    return min(tasks, key=len)

def read_tasks():
    try:
        with open("tasks.txt") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def add_task(text):
    with open("tasks.txt", "a") as f:
        f.write(text + "\n")

def to_first_step(task):
    """Turn a task into something you can actually begin."""
    return f"Spend 5 minutes on: {task}"


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "add":
        text = " ".join(sys.argv[2:])
        add_task(text)
        print("Added: " + text)
        return
    tasks = read_tasks()
    if not tasks:
        print()
        print("No tasks found. Please add tasks to tasks.txt.")
        return
    task = pick_one(tasks)
    print()
    print("Your one thing right now:")
    print("   " + to_first_step(task))
    print()

if __name__ == "__main__":
    main()