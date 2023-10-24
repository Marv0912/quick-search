#!/usr/bin/env python

import argparse
import subprocess
import urllib.parse

def search(query):
    search_query = urllib.parse.quote(query)
    url = f"https://google.com/search?q={search_query}"
    subprocess.run(["google-chrome", url])

def main():
    parser = argparse.ArgumentParser(description="Quick terminal search using Google Chrome")
    parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    search(args.query)

if __name__ == "__main__":
    main()