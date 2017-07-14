from django.core.management.base import BaseCommand, CommandError
from sentiment_analysis.models import Data

from ml_modules.example_usage import SentimentTracker


class Command(BaseCommand):
    help = 'Grape new tweets'

    def handle(self, *args, **options):
        data = SentimentTracker().get_tweets_sample(count=5)
        cnts = 8 * [0]
        for i in data[1]:
            for j in range(8):
                cnts[j] += i[j]
        for i in range(8):
            cnts[i] = (cnts[i] / 5) * 100
        data_ = Data(happy=cnts[0], love=cnts[1], hopeful=cnts[2], neutral=cnts[3], angry=cnts[4], hopeless=cnts[5],
                     hate=cnts[6], sad=cnts[7])
        data_.save()
        self.stdout.write(self.style.SUCCESS('Successfully added ' + str(cnts)))
