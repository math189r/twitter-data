import argparse
import json
from pprint import pprint
import sys

import tweepy

import handlers
import stream

def main():
    '''main
    loads config file determined in the
    command line argument --config or -c.

    Connects to twitter steaming and handles
    the data resultant given the options
    passed in the config
    '''
    # capture command line args
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config',
            help='path to the json config file containing Twitter auth and handlers params, etc.')
    args = parser.parse_args()

    # load config file from json
    with open(args.config) as config_file:
        config = json.load(config_file)

    # pick handler to use based on config
    if config['handler'] == 'print':
        handler = handlers.PrintHandler(config)
    elif config['handler'] == 'postgres':
        handler = handlers.PostgresHandler(config)

    # create streamer with given handler
    listener = stream.TweetListener(handler)

    # create auth
    auth = tweepy.OAuthHandler(config['twitter']['consumer_key'],
            config['twitter']['consumer_secret'])
    auth.set_access_token(config['twitter']['access_token'],
            config['twitter']['access_token_secret'])
    streamer = tweepy.Stream(auth, listener)

    # stream given config params
    try:
        langs = ['en'] if 'languages' not in config else config['languages']
        if config['stream'] == 'filter':
            streamer.filter(track=config['track'], languages=langs)
        elif config['stream'] == 'sample':
            streamer.sample(languages=langs, async=True)
    except KeyboardInterrupt:
        # handle deconstruction of handler
        with open('log.out', 'a') as f:
            stats = listener.stats()
            stats['config'] = args.config
            f.write(json.dumps(stats))
            f.write('\n')
        handler.close()
        streamer.disconnect()
        sys.exit()


if __name__ == '__main__':
    main()
