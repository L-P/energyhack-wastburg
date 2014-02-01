from django.core.management.base import BaseCommand
from matplotlib import pyplot as plt
from Profile import Profile

class Command(BaseCommand):
    def handle(self, *args, **options):
        p = Profile()

        doys = range(365)
        plt.hold(True)
        plt.plot(doys, p.predict_cost(doys, surface=20), c='r')
        plt.xlabel("day")
        plt.ylabel("cost")
        plt.show()
