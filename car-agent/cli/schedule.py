import json

def schedule_task(args):
    """
    Schedules a task based on the provided arguments.
    """
    # Example logic for scheduling a task
    schedule = {
        "task": args.task,
        "time": args.time or "Sat 07",
        "preview": args.preview
    }

    # Output the schedule as JSON
    print(json.dumps(schedule, indent=4))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Schedule a task.")
    parser.add_argument("task", type=str, help="The task to schedule.")
    parser.add_argument("--time", type=str, help="Override driving time.")
    parser.add_argument("--preview", action="store_true", help="Preview scheduling.")

    args = parser.parse_args()
    schedule_task(args)
