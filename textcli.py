import argparse
from analyzer import Text

def main():
    parser = argparse.ArgumentParser(description= "Text Analyzer Tool")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command")

    #Add Stats
    stats_parser = subparsers.add_parser("stats", help="line, word, character count")
    stats_parser.add_argument("--file", required=True)

    #Add Top
    top_parser = subparsers.add_parser("top" , help=" most frequent N words")
    top_parser.add_argument("--file", required=True)
    top_parser.add_argument("-n", required=True, type=int)

    #Add Match
    match_parser = subparsers.add_parser("match", help="search and print matching lines")
    match_parser.add_argument("--file", required=True)
    match_parser.add_argument("--pattern", required=True)

    args = parser.parse_args()

    
    if args.command == 'stats':
        t = Text(args.file)
        print(t.stats())
    
    elif args.command == "top":
        t = Text(args.file)
        print(t.top(args.n))

    elif args.command == "match":
        t = Text(args.file)
        print(t.match(args.pattern))

    else:
        print(args.help)
    


if __name__ == "__main__":
    main()
