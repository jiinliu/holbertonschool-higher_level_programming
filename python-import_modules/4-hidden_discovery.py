#!/usr/bin/python3
import hidden_4


def main():
    names = dir(hidden_4)

    # Filter out names that start with '__'
    filtered_names = [name for name in names if not name.startswith('__')]

    # Print names in alphabetical order
    for name in sorted(filtered_names):
        print(name)


if __name__ == "__main__":
    main()
