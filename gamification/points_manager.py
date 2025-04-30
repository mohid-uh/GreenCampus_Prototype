from utils.design_pattern import Subscriber

class PointsManager(Subscriber):
    """
    Subscribes to CarbonTracker events and
    awards GreenPoints to User objects.
    """
    def update(self, event, data):
        if event == "ECO_TRAVEL_LOG":
            user   = data["user"]
            points = data["points"]
            user.add_points(points)