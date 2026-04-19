#!/usr/bin/env python3
from handle_prompt import handle_user_prompt

def main():
    try:
        handle_user_prompt()
    except ValueError as e:
        print(f"Ooops. Something went wrong: {e}")

if __name__=="__main__":
    main()