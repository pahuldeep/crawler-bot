import argparse

from modules.crawler import run_crawler
from modules.processor import run_processor
from modules.memory import run_memory

def main():
    parser = argparse.ArgumentParser(description="Web Scraping + Q&A CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Crawl subcommand
    crawl_parser = subparsers.add_parser("crawl", help="Run the crawler")
    crawl_parser.add_argument("url", help="Start URL to crawl (Enter url: for user preferred website)")
    crawl_parser.add_argument("--max_pages", type=int, default=10, help="Maximum Pages to crawl (default: 10)")

    # Process subcommand
    process_parser = subparsers.add_parser("process", help="Process data into chunks")
    process_parser.add_argument("query", nargs='?', default='', help="User guided chunk filtering")
    process_parser.add_argument("numbers", nargs='?', type=int, default=20, help="Enter the number of data chunks (default: 20)")

    # Summarize subcommand
    memory_parser = subparsers.add_parser("memory", help="Summarize and classify relevant chunks")

    # Add the QA subcommand
    question_parser = subparsers.add_parser("ask", help="Ask any question related to the website")
    question_parser.add_argument("query", nargs='?', default='', help="User query to be answered by the BOT")

    args = parser.parse_args()

    if args.command == "crawl":
        run_crawler(args.url, args.max_pages)
    elif args.command == "process":
        run_processor(args.query, args.numbers)
    elif args.command == "memory":
        run_memory()
    elif args.command == "ask":
        print(args.query, "\ncurrently untested!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
