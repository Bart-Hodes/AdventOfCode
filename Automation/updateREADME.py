import os
import subprocess
import time

# Path to the README file
README_PATH = "README.md"
# Path to the folder containing solutions
SOLUTIONS_FOLDER = "2024"


def get_solution_folders(folder):
    """Retrieve solution folders from the main folder."""
    return sorted([f for f in os.listdir(folder) if f.startswith("Day")])


def run_solution(file_path, part):
    """Run a solution file (part1.py or part2.py) and measure runtime."""
    start_time = time.time()
    try:
        subprocess.run(
            ["python3", os.path.join(file_path, f"{part}.py")],
            check=True,
            capture_output=True,
        )
        runtime = time.time() - start_time
    except subprocess.CalledProcessError as e:
        print(f"Error running {file_path}/{part}.py: {e}")
        runtime = None
    return runtime


def generate_readme(runtimes_part1, runtimes_part2, stars_part1, stars_part2):
    """Generate a new README file with stars and runtimes."""
    readme_content = "# Advent of Code 2024\n\n"
    readme_content += (
        "| Day | Part 1 Stars | Part 1 Runtime | Part 2 Stars | Part 2 Runtime |\n"
    )
    readme_content += (
        "|-----|--------------|----------------|--------------|----------------|\n"
    )

    for day in sorted(runtimes_part1.keys()):
        stars1 = "⭐" * stars_part1.get(day, 0)
        runtime1 = (
            f"{runtimes_part1.get(day, 'N/A'):.2f}s" if day in runtimes_part1 else "N/A"
        )
        stars2 = "⭐" * stars_part2.get(day, 0)
        runtime2 = (
            f"{runtimes_part2.get(day, 'N/A'):.2f}s" if day in runtimes_part2 else "N/A"
        )

        readme_content += f"| {day} | {stars1} | {runtime1} | {stars2} | {runtime2} |\n"

    with open(README_PATH, "w") as f:
        f.write(readme_content)
    print(f"README file created at: {README_PATH}")


def main():
    stars_part1 = {}
    stars_part2 = {}
    runtimes_part1 = {}
    runtimes_part2 = {}

    for folder in get_solution_folders(SOLUTIONS_FOLDER):
        day = int(folder.split("Day")[1])
        file_path = os.path.join(SOLUTIONS_FOLDER, folder)

        # Run part1.py and record runtime
        runtime1 = run_solution(file_path, "part1")
        if runtime1 is not None:
            stars_part1[day] = 1
            runtimes_part1[day] = runtime1

        # Run part2.py and record runtime
        runtime2 = run_solution(file_path, "part2")
        if runtime2 is not None:
            stars_part2[day] = 1
            runtimes_part2[day] = runtime2

    # Generate a new README with stars and runtimes
    generate_readme(runtimes_part1, runtimes_part2, stars_part1, stars_part2)


if __name__ == "__main__":
    main()
