import os
import subprocess
import time
import json

# Paths
SOLUTIONS_BASE_FOLDER = "."
README_PATH = "README.md"
CACHE_PATH = "cache.json"


def get_solution_folders(year):
    """Retrieve solution folders for a specific year."""
    folder = os.path.join(SOLUTIONS_BASE_FOLDER, str(year))
    if not os.path.exists(folder):
        return []
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
    """Load cache from the cache file."""
    if os.path.exists(CACHE_PATH):
        with open(CACHE_PATH, "r") as f:
            return json.load(f)
    return {}


def save_cache(cache):
    """Save cache to the cache file."""
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, indent=4)


def has_folder_changed(folder, cached_timestamps):
    """Check if a folder's contents have changed based on timestamps."""
    current_timestamps = {
        f: os.path.getmtime(os.path.join(folder, f)) for f in os.listdir(folder)
    }
    return current_timestamps != cached_timestamps, current_timestamps


def generate_readme(all_data):
    """Generate a new README file with stars and runtimes for all years."""
    total_stars = sum(
        sum(stars.values()) for year_data in all_data.values() for stars in year_data["stars"].values()
    )

    readme_content = f"# Advent of Code - Total Stars: {total_stars}\n\n"

    for year, year_data in sorted(all_data.items()):
        if not any(year_data["stars"]["part1"].values()) and not any(
            year_data["stars"]["part2"].values()
        ):
            # Skip years with no solved days
            continue

        readme_content += f"<details>\n<summary>{year}</summary>\n\n"
        readme_content += (
            "| Day | Part 1 Stars | Part 1 Runtime | Part 2 Stars | Part 2 Runtime |\n"
        )
        readme_content += (
            "|-----|--------------|----------------|--------------|----------------|\n"
        )

        for day in sorted(year_data["runtimes"]["part1"].keys()):
            stars1 = "⭐" * year_data["stars"]["part1"].get(day, 0)
            runtime1 = format_runtime(year_data["runtimes"]["part1"].get(day))
            stars2 = "⭐" * year_data["stars"]["part2"].get(day, 0)
            runtime2 = format_runtime(year_data["runtimes"]["part2"].get(day))

            readme_content += f"| {day} | {stars1} | {runtime1} | {stars2} | {runtime2} |\n"

        readme_content += "\n</details>\n\n"

    with open(README_PATH, "w") as f:
        f.write(readme_content)
    print(f"README file created at: {README_PATH}")


def main():
    cache = load_cache()
    all_data = {}

    for year in range(2015, 2025):
        stars_part1 = {}
        stars_part2 = {}
        runtimes_part1 = {}
        runtimes_part2 = {}

        for folder in get_solution_folders(year):
            day = int(folder.split("Day")[1])
            file_path = os.path.join(SOLUTIONS_BASE_FOLDER, str(year), folder)

            # Check if the folder's contents have changed
            folder_changed, current_timestamps = has_folder_changed(
                file_path, cache.get(str(year), {}).get(folder, {}).get("timestamps", {})
            )

            if folder_changed:
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

                # Update cache
                if year not in cache:
                    cache[str(year)] = {}
                cache[str(year)][folder] = {
                    "timestamps": current_timestamps,
                    "stars": {"part1": stars_part1.get(day, 0), "part2": stars_part2.get(day, 0)},
                    "runtimes": {"part1": runtimes_part1.get(day), "part2": runtimes_part2.get(day)},
                }
            else:
                # Load from cache
                cached_data = cache[str(year)][folder]
                stars_part1[day] = cached_data["stars"]["part1"]
                stars_part2[day] = cached_data["stars"]["part2"]
                runtimes_part1[day] = cached_data["runtimes"]["part1"]
                runtimes_part2[day] = cached_data["runtimes"]["part2"]

        # Store data for the year
        all_data[year] = {
            "stars": {"part1": stars_part1, "part2": stars_part2},
            "runtimes": {"part1": runtimes_part1, "part2": runtimes_part2},
        }

    # Save updated cache
    save_cache(cache)

    # Generate a new README with total stars and per-year details
    generate_readme(all_data)


if __name__ == "__main__":
    main()
