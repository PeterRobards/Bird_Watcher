#!/usr/bin/env python
"""
Python script designed to parse specific twitter data from a json file to a csv file
	Created on Thu Aug 30 09:21:00 2019
	@author: Peter Robards
"""
# -*- coding: utf-8 -*-
#
# Twitter Live Stream Collection Program -- Version 1.1
# Copyright (c) Peter Robards
#
##########################################################################################


import json
import sys
from csv import writer


def check_format(json_string, correct_value):
    """takes the first key from json formatted string and compares it to a desired value"""
    string_start = json_string.split(":", 1)[0]
    first_value = string_start.strip("{")

    return first_value == correct_value


def process_hash_tags(raw_hash_tags):
    """method that takes the hashtags from a dictionary and stores them in a list"""

    hashtag_list = list()

    for hash_tag in raw_hash_tags:
        text = hash_tag["text"]
        # Append the text of any included hashtags to our list
        hashtag_list.append(text)

    return hashtag_list


def main():
    '''Python script designed to parse specific twitter data from a json file to a csv file'''
    # Check for above arguments - if none are provided, Display --help
    if len(sys.argv) == 1:
        input_file = input("\nPlease enter name of the input file where the raw json tweets are: ")
        output_file = input("\nPlease enter name of file where you wish to save results: ")
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        print(f'Error - Three arguments expected: 1. \'{sys.argv[0]}\' 2. \'infile\' 3. \'outfile\'')
        print(f'Instead {len(sys.argv)} received...')
        print(f'Arguments provided: {sys.argv}')
        sys.exit(1)
    
    with open(input_file) as in_file, open(output_file, "w") as out_file:
        # Create column headers for our CSV file and output to file
        headers = [
            "tweet_id",
            "tweet_time",
            "tweet_author",
            "tweet_author_id",
            "tweet_author_location",
            "tweet_author_followerCount",
            "tweet_author_friendCount",
            "tweet_language",
            "tweet_geo",
            "tweet_text",
            "tweet_hashtags",
        ]
        csv = writer(out_file)
        csv.writerow(headers)
        tweet_count = 0

        for line in in_file:
            # print(f'\n{line}')

            # Check if line contains data: skips over blank lines
            if line.strip():

                # Check if line's format matches a tweet: first key = "created_at"
                check_string = '"created_at"'
                if check_format(line, check_string):
                    tweet_count += 1
                    # Loading tweets from json file into a python dictionary line by line
                    tweet = json.loads(line)

                    raw_hash_tags = tweet["entities"]["hashtags"]
                    hash_tags = process_hash_tags(raw_hash_tags)

                    # Extract out the desired data from our dictionary of tweets
                    row = (
                        tweet["id"],                       # tweet_id
                        tweet["created_at"],               # tweet_time
                        tweet["user"]["screen_name"],      # tweet_author
                        tweet["user"]["id_str"],           # tweet_authod_id
                        tweet["user"]["location"],         # tweet_author_location
                        tweet["user"]["followers_count"],  # tweet_author_followerCount
                        tweet["user"]["friends_count"],    # tweet_author_friendCount
                        tweet["lang"],                     # tweet_language
                        tweet["geo"],                      # tweet_geo
                        tweet["text"],                     # tweet_text
                        hash_tags,                         # tweet_hashtags
                    )
                    values = [
                        (value.encode("utf8") if hasattr(value, "encode") else value)
                        for value in row
                    ]
                    csv.writerow(values)

    # print the name of each file and the number of tweets imported
    print("File Imported:", str(sys.argv[1]))
    print("# Tweets Imported:", tweet_count)
    print("File Exported:", str(sys.argv[2]))


if __name__ == "__main__":

    main()
