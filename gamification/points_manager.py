from utils.design_pattern import Subscriber

class PointsManager(Subscriber):
    """
    Subscribes to CarbonTracker/EnergyTracker events and
    awards GreenPoints to User objects.
    """
    def update(self, event, data):
        user = data.get("user")
        points = data.get("points", 0)

        if event == "ECO_TRAVEL_LOG" or event == "ENERGY_EFFICIENT_CHOICE":
            user.add_points(points)