"""
Generates a directory tree file for all the nested sub directories!
"""

import context
import os


def generate_directory_tree(
    root_dir, ignore_dirs=None, output_file="./docs/directory_tree.md"
):
    if ignore_dirs is None:
        ignore_dirs = {".venv", ".git", "__pycache__", "pytest", "node_modules"}

    # Create a list to hold the lines of the output
    output_lines = []

    # Get the base directory name to include it at the top
    base_dir_name = os.path.basename(root_dir)

    # Add the base directory at the top
    output_lines.append(f"{base_dir_name}/")

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modify the list of directories to ignore them
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]

        # Get the depth of the current directory
        depth = dirpath.count(os.sep) - root_dir.count(os.sep)

        # Only process specified file types
        # Skip __init__.py, those are just visually noisy IMHO
        allowed_extensions = (
            ".py",
            ".md",
            ".txt",
            ".yaml",
            ".producton",
            ".staging",
            ".flake8",
        )
        filtered_files = [
            f
            for f in filenames
            if f.endswith(allowed_extensions) and f != "__init__.py"
        ]

        # Create indentation based on depth
        indent = "    " * depth

        # Add directory name with proper indentation
        if depth > 0:
            output_lines.append(
                f"{indent}└── {os.path.basename(dirpath)}/"
            )  # Directory name

        # Add files to the output with appropriate indentation
        for i, file in enumerate(filtered_files):
            if i == len(filtered_files) - 1:
                output_lines.append(f"{indent}    └── {file}")  # Last item
            else:
                output_lines.append(f"{indent}    ├── {file}")  # Other items

    # Write the structure to the output file
    with open(output_file, "w") as f:
        title = "## Directory Tree"
        f.write(title + "\n\n" + "```txt" + "\n")
        for line in output_lines:
            f.write(line + "\n")
        f.write("```")


if __name__ == "__main__":
    # Specify the root directory to start from
    root_directory = "."  # Change this to your desired root directory
    generate_directory_tree(root_directory)
