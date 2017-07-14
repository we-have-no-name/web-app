import sys, os
import numpy as np

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from ml_modules.ClassifierInterface import ClassifierInterface, IncomingQueue
from ml_modules.TwitterAgent import TwitterAgent


class SentimentTracker():
    def __init__(self):
        self.ta = TwitterAgent()
        self.incoming_queue = IncomingQueue()
        self.c = ClassifierInterface(self.incoming_queue)
        self.ready_queue = self.c.ready_queue

    def get_tweets_sample(self, count=5):
        self.max_tweets = [count]
        self.ta.get_sample_tweets_stream(max_tweets=self.max_tweets, data_handler=self.incoming_queue, lang='en',
                                         save_to_files=False)
        self.c.classify_batch()
        tweets = []
        sentiments = np.zeros((count, 8), dtype=np.float32)
        for i in range(count):
            tweet = self.ready_queue.get()
            tweets.append(tweet)
            sentiments[i] = tweet.sentiment
        return [tweets, sentiments]


# An example usage of the SentimentTracker
sent_map = ['Happy', 'Love', 'Hopeful', 'Neutral', 'Angry', 'Hopeless', 'Hate', 'Sad']
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


def main(print_tweets=False, print_sentiments=False):
    '''
    Prints the classified tweets.
    '''
    st = SentimentTracker()
    tweets, sentiments = st.get_tweets_sample(5)  # 5 is count
    if print_tweets:
        for tweet in tweets:
            probs = ', '.join(
                ['{}: {:.3}'.format(sent_map[l], tweet.sentiment[l]) for l in np.argsort(tweet.sentiment)[::-1][:3] if
                 tweet.sentiment[l] > 0.01])
            print('tweet: {}\nprobs: {}\ncountry: {}\nlocation: {}\nlang: {}\n'.format(tweet.text, probs, tweet.country,
                                                                                       tweet.location,
                                                                                       tweet.lang).translate(
                non_bmp_map))
    if print_sentiments:
        print(sentiments)


if __name__ == '__main__': main()
