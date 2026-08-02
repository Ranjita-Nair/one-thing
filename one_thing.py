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


def to_first_step(task):
    """Turn a task into something you can actually begin."""
    return f"Spend 5 minutes on: {task}"


def main():
    task = pick_one(tasks)
    print()
    print("Your one thing right now:")
    print("   " + to_first_step(task))
    print()


if __name__ == "__main__":
    main()