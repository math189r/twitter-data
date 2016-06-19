import psycopg2
import json

class PostgresHandler():
    '''PostgresHandler
    Gives access to the database by passing in a config
    file with DB params. Abstracts pushing tweets to the
    database.
    '''
    conn = None
    cur  = None

    def __init__(self, config):
        '''__init__
        Initialized a database instance (of type
        abstracted from the user).

            config (dict) -> Expects config['db_uri']
        '''
        self.conn = psychopg2(config['db_uri'])
        self.cur  = self.conn.cursor()

    def close(self):
        '''close
        Closes the database connection
        '''
        self.cur.close()
        self.conn.close()

    def push_tweet(self, tweet):
        '''push_tweet
        takes in a tweet dictionary according to the
        twitter api spec and pushes it to the db
        '''
        if not self.conn or not self.cur:
            raise ConnectionError('==> Attempting to push tweet without active db connection')
        ## TODO
        print(tweet)

class PrintHandler():
    '''PrintHandler
    Mocks inserting tweets. Doesn't connect to database
    and just prints input to stdout
    '''

    def __init__(self, config):
        '''__init__
        Configures which fields to print from the tweets.
        if config['fields'] is not present, every field
        will be printed.

            config (dict) -> Expects config['fields'] (list)
        '''
        self.fields = None if 'fields' not in config else config['fields']

    def close(self):
        pass

    def push_tweet(self, tweet):
        '''push_tweet
        takes in a tweet dictionary according to the
        twitter api spec and prints it
        '''
        if not self.fields:
            filtered = tweet
        else:
            # filter by fields
            filtered = {field: tweet[field] for field in self.fields}
        print(json.dumps(filtered, ensure_ascii=False))
