import os
import time
import json
from aocd.models import Puzzle
from importlib import import_module


# Paths
SOLUTIONS_BASE_FOLDER = "."
README_PATH = "README.md"
CACHE_PATH = "cache.json"


def get_solution_files(year):
    """Retrieve solution files for a specific year."""
    folder = os.path.join(SOLUTIONS_BASE_FOLDER, str(year))
    if not os.path.exists(folder):
        return []
    return sorted(
        [f for f in os.listdir(folder) if f.startswith("Day") and f.endswith(".py")]
    )


def run_solution(year, day, part, puzzle):
    """Run the solution function (part_a or part_b) and measure runtime."""
    module_name = f"{year}.Day{day}"
    try:
        start_time = time.time()
        solution_module = import_module(module_name)
        result = getattr(solution_module, f"part_{part}")(puzzle.input_data)
        if part == "a":
            assert (
                str(result) == puzzle.answer_a
            ), f"Expected: {puzzle.answer_a}, got: {result}"
        else:
            assert (
                str(result) == puzzle.answer_b
            ), f"Expected: {puzzle.answer_b}, got: {result}"
        runtime = time.time() - start_time
        return runtime
    except Exception as e:
        print(f"Error running {module_name}.part_{part}: {e}")
        return None


def format_runtime(runtime):
    """Format runtime into a human-readable string."""
    if runtime is None:
        return "N/A"
    elif runtime < 1e-3:
        return f"{runtime * 1e6:.2f} µs"
    elif runtime < 1:
        return f"{runtime * 1e3:.2f} ms"
    else:
        return f"{runtime:.2f} s"


def load_cache():
    """Load cache from file."""
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            data = json.load(f)
        return data.get("data", {}), data.get("timestamps", {})
    else:
        return {}, {}


def save_cache(all_data, timestamps):
    """Save cache to file."""
    data_to_save = {"data": all_data, "timestamps": timestamps}
    with open(CACHE_PATH, "w") as f:
        json.dump(data_to_save, f)


def generate_readme(all_data):
    """Generate a new README file with stars and runtimes for all years."""
    total_stars = sum(
        sum(stars.values())
        for year_data in all_data.values()
        for stars in year_data["stars"].values()
    )

    readme_content = f"# Advent of Code - Total Stars: {total_stars}\n\n"

    for year, year_data in sorted(all_data.items()):
        total_year_stars = sum(year_data["stars"]["part_a"].values()) + sum(
            year_data["stars"]["part_b"].values()
        )

        if total_year_stars == 0:
            continue  # Skip years with no solved days

        readme_content += f"<details>\n<summary> {year} - Total Stars: {total_year_stars}</summary>\n\n"
        readme_content += (
            "| Day | Part A Stars | Part A Runtime | Part B Stars | Part B Runtime |\n"
        )
        readme_content += (
            "|-----|--------------|----------------|--------------|----------------|\n"
        )

        for day in sorted(year_data["runtimes"]["part_a"].keys()):
            stars_a = "⭐" * year_data["stars"]["part_a"].get(day, 0)
            runtime_a = format_runtime(year_data["runtimes"]["part_a"].get(day))
            stars_b = "⭐" * year_data["stars"]["part_b"].get(day, 0)
            runtime_b = format_runtime(year_data["runtimes"]["part_b"].get(day))

            readme_content += f"| [{day}](https://adventofcode.com/{year}/day/{day}) | {stars_a} | {runtime_a} | {stars_b} | {runtime_b} |\n"

        readme_content += "\n</details>\n\n"

    with open(README_PATH, "w") as f:
        f.write(readme_content)
    print(f"README file created at: {README_PATH}")


def main():
    cache, timestamps = load_cache()
    all_data = {}

    for year in range(2015, 2025):
        # Initialize yearly data
        stars_part_a = {}
        stars_part_b = {}
        runtimes_part_a = {}
        runtimes_part_b = {}

        for file_name in get_solution_files(year):
            day = int(file_name.split("Day")[1].split(".")[0])
            puzzle = Puzzle(year=year, day=day)

            # Get the full path of the file
            file_path = os.path.join(SOLUTIONS_BASE_FOLDER, str(year), file_name)

            # Check if cache is up-to-date
            current_mtime = os.path.getmtime(file_path)
            if (
                str(year) in cache
                and str(day) in cache[str(year)]["stars"]["part_a"]
                and str(day) in cache[str(year)]["stars"]["part_b"]
                and str(year) in timestamps
                and str(day) in timestamps[str(year)]
                and current_mtime == timestamps[str(year)][str(day)]
            ):
                print(f"Skipping {year}/Day{day} (cached)")
                stars_part_a[day] = cache[str(year)]["stars"]["part_a"][str(day)]
                runtimes_part_a[day] = cache[str(year)]["runtimes"]["part_a"][str(day)]
                stars_part_b[day] = cache[str(year)]["stars"]["part_b"][str(day)]
                runtimes_part_b[day] = cache[str(year)]["runtimes"]["part_b"][str(day)]
            else:
                # Run part_a and record runtime
                print(f"Running {year}/Day{day} - part_a")
                runtime_a = run_solution(year, day, "a", puzzle)
                stars_part_a[day] = 1 if runtime_a is not None else 0
                runtimes_part_a[day] = runtime_a

                # Run part_b and record runtime
                print(f"Running {year}/Day{day} - part_b")
                runtime_b = run_solution(year, day, "b", puzzle)
                stars_part_b[day] = 1 if runtime_b is not None else 0
                runtimes_part_b[day] = runtime_b

                # Update timestamp for the current file
                if str(year) not in timestamps:
                    timestamps[str(year)] = {}
                timestamps[str(year)][str(day)] = current_mtime

        # Store data for the year
        all_data[year] = {
            "stars": {"part_a": stars_part_a, "part_b": stars_part_b},
            "runtimes": {"part_a": runtimes_part_a, "part_b": runtimes_part_b},
        }

    # Save updated cache and timestamps
    save_cache(all_data, timestamps)

    # Generate a new README with total stars and per-year details
    generate_readme(all_data)


if __name__ == "__main__":
    main()
