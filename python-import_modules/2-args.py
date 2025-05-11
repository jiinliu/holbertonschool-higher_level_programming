#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]
    count = len(args)
    if count == 0:
        print(f"{count} arguments.")
    elif count == 1:
            print(f"{count} argumment:")
    else:
     print(f"{count} arguments:")
     for idx, arg in enumerate(args, start=1):
         print(f"{idx}: {arg}")
         if __name__ == "__main__":
              main()