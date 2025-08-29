import subprocess

def run_demo():
    print("\n--- Generating Maintenance Plan ---")
    subprocess.run(["python", "car-agent/cli/plan.py", "--accept"])

    print("\n--- Optimizing Trip ---")
    subprocess.run(["python", "car-agent/cli/optimize.py", "Bangalore to Mysore", "--mode", "city"])

    print("\n--- Scheduling Task ---")
    subprocess.run(["python", "car-agent/cli/schedule.py", "trip.json", "--time", "Sat 07"])

    print("\n--- Analyzing Performance Metrics ---")
    subprocess.run(["python", "car-agent/cli/metrics.py", "--import", "fuel.csv", "--summary"])

if __name__ == "__main__":
    run_demo()
