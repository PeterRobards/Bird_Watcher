#!/usr/bin/env python
"""Python Program to collect live tweets containing matches to a list of user supplied key words"""
# -*- coding: utf-8 -*-
#
# Twitter Live Stream Collection Program -- Version 1.1
# - Peter Robards.
#
##########################################################################################

__author__ = ["Peter Robards"]
__date__ = "10/20/2019"
__description__ = (
    "Python script to collect live tweets containing matches to a list of key words"
)

import sys
import time
import logging
import argparse
from tweepy import Stream
from tweepy.streaming import StreamListener as SListener
from api_config import create_api

# Enable Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


################################ Class Definition ########################################
# This is a basic listener that simply prints received tweets to stdout.
#  Note:  to save to file: get_tweet.py > some_file.txt
class StreamListener(SListener):
    """Simple Stream listener that simply prints received tweets to stdout """

    def __init__(
        self, api=None, out_file="raw_tweets.json", page_limit=20000, time_limit=3600.00
    ):
        self.api = api
        self.counter = 0
        self.page_count = 0
        self.page_limit = page_limit
        self.start_time = time.time()
        self.time_limit = time_limit
        self.output = out_file

    def on_data(self, data):
        "capture all data and export to designated file"

        with open(self.output, "a") as o_file:
            o_file.write(data)

        if (time.time() - self.start_time) < self.time_limit:
            self.counter += 1

            # Limit number of tweets saved to an individual file (default: 20,000 ~ 1.75GB)
            if self.counter >= self.page_limit:
                self.page_count += 1
                if self.page_count > 1:
                    file_name = self.output.split(".", 1)[0]
                    file_ext = self.output.split(".", 1)[1]
                    file_name = file_name.split("_", 1)[0]
                    new_file = file_name + "." + file_ext
                else:
                    new_file = self.output.split(".", 1)[0] + "_" + str(self.page_count)
                    new_file += "." + self.output.split(".", 1)[1]
                    self.output = new_file
                    self.counter = 0

            return True

        else:
            return False

    def on_error(self, status):
        "if an Error occurs: log it and display it to std out"
        total_tweets = self.counter + self.page_count * self.page_limit
        print(f"\nError : {status}\nProcessed #{total_tweets} tweets")
        logger.error(
            "Error : {status} - Processed #{total_tweets} tweets", exc_info=True
        )


############################### Method Definition ########################################
# Converts user input to a list of key words.
def get_search_terms():
    """Ask user for list of key words to search for and return as a list"""
    search_terms = []
    raw_input = input(
        "\nPlease enter key words/phrases to search for separaterd by a ','"
    )

    search_terms = raw_input.split(",")

    return search_terms

################################# Main() Method #########################################
def main():
    """Python Program that collects live tweets based on a list of user supplied key words """

    parser = argparse.ArgumentParser(
        description=__description__,
        epilog="Last Modified by {} on {}".format(", ".join(__author__), __date__),
    )
    parser.add_argument(
        "-s",
        "--search_terms",
        nargs="+",
        dest="search_terms",
        help="Key word(s) or phrase(s) to search for",
    )
    parser.add_argument(
        "-o",
        "--out_file",
        nargs="?",
        dest="out_file",
        help="Output file to save raw json tweets",
    )
    parser.add_argument(
        "-t",
        "--time_limit",
        nargs="?",
        dest="time_limit",
        type=float,
        default=3600,
        help="Set time limit (in seconds) for the program. Default: 3600 seconds",
    )
    parser.add_argument(
        "-p",
        "--page_limit",
        nargs="?",
        dest="page_limit",
        type=int,
        default=20000,
        help="Set the limit for # of tweets saved per file. Defaul: 20,000",
    )

    # Check for above arguments - if none are provided, Display --help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    page_limit = args.page_limit
    time_limit = args.time_limit

    if args.search_terms:
        search_terms = args.search_terms
    else:
        # search_terms = ['keyword', 'some phrase', 'hashtag1', 'hashtag2']
        search_terms = get_search_terms()

    if args.out_file:
        out_file = args.out_file
    else:
        out_file = input("\nPlease enter name of file where you wish to save results: ")

    print("\n ***** Running Program *****")

    print("[+] Creating API...")
    # This handles Twitter authetification and the connection to Twitter Streaming API
    api = create_api()

    tweet_listener = StreamListener(api, out_file, page_limit, time_limit)
    stream = Stream(api.auth, tweet_listener)
    print("[+] Starting Listener...")
    print(f"[+] Program will run for {time_limit} seconds...")
    print(f"[+] Searching for the following key words:\n\t{search_terms}")
    print(f"[+] Saving stream to '{out_file}' ...\n")

    # Filters the Twitter Stream to capture data with the keywords in the list: 'search_terms[]'
    # Note: 'is_async' parameter on filter runs stream on a new thread
    stream.filter(track=search_terms, is_async=True)
##########################################################################################

if __name__ == "__main__":

    main()
