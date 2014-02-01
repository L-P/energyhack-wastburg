from Profile import Profile
from django.core.management.base import BaseCommand
from matplotlib import pyplot as plt
from wastburg.models import Lot

class Command(BaseCommand):
    def handle(self, *args, **options):
        p = Profile()
        lot = Lot.objects.get(name="B123")
        goal = p.get_goal(lot.surface)
        heat = p.get_bullshit_heat_spendings(lot.surface, .3, .3)

        doys = range(365)
        goal_daily = p.get_daily_goals(lot.surface)
        diff = map((lambda x,y: goal + x-y), heat, goal_daily)

        plt.plot(doys[:150], diff[:150])
        plt.plot(doys[150:], diff[150:], '--')
        plt.axhline(goal, label="goal", c="b")
        plt.xlabel("day")
        plt.ylabel("cost")
        plt.legend()
        plt.show()
