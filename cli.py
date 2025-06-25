import argparse
from logic import Maths

def main():
    parser = argparse.ArgumentParser(description="Maths Tool")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command")

    #Factorial
    factorial_parser = subparsers.add_parser("factorial", help="Give factorial of given number")
    factorial_parser.add_argument("-n", required=True, type = int)

    #Is Prime
    prime_parser = subparsers.add_parser("is-prime", help="Show given number is prime or not")
    prime_parser.add_argument('-n', required=True, type = int)

    #Fibonacci
    fibonacci_parser = subparsers.add_parser("fibonacci", help="Give fibonacci series of range of given number")
    fibonacci_parser.add_argument('-n', required=True, type=int)


    args = parser.parse_args()
    math = Maths(args.n)
    
    if args.command == 'factorial':
        print(math.factorial())

    elif args.command == "is-prime":
        print(math.is_prime())

    elif args.command == 'fibonacci':
        print(math.fibonacci())

    else:
        print(args.help)

if __name__ == '__main__':
    main()
                                             
