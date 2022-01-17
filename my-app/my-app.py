"""
@author: mronen
"""
import os
import sys
import traceback


def get_parent_script_dir_path():
    # Get the parent directory path of the running script
    path = os.path.dirname(os.path.abspath(__file__))
    return path


def main():
    try:
        test_file = 'test.txt'
        parent_script_dir_path = get_parent_script_dir_path()
        print(f"parent_script_dir_path={parent_script_dir_path}")

        # Set the "test.txt" file path to be reside next to this script
        test_file_path = os.path.join(parent_script_dir_path, test_file)
        print(f"test_file_path={test_file_path}")

        with open(test_file_path, 'w') as f:
            f.write("Hello World")
    except Exception as e:
        print(f"program failed with error: {e}")
        tb = traceback.format_exc()
        print(f"Stack Trace: {tb}")
        return 1
    return 0


if __name__ == '__main__':
    rc = main()
    sys.exit(rc)
