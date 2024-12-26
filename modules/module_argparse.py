import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple argparse example")
    
    # Adding arguments
    parser.add_argument('name', type=str, help='Your name')
    parser.add_argument('-a', '--age', type=int, help='Your age', required=True)
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    
    # Parsing arguments
    args = parser.parse_args()
    
    # Using the arguments
    print(f"Hello, {args.name}!")
    print(f"You are {args.age} years old.")
    
    if args.verbose:
        print("Verbose mode is enabled.")

if __name__ == "__main__":
    main()