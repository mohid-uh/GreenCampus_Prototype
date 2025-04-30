from utils.design_pattern import Publisher

class CarbonTracker(Publisher):
    """
    Calculates carbon footprint based on travel choices.
    Then publishes events when points should be awarded.
    """
    EMISSIONS_PER_KM = {
        "car": 0.21,    # kg CO2 per km
        "bus": 0.08,
        "train": 0.02,
        "bike": 0.0,
        "walk": 0.0
    }

    # Initialise Publisher
    def __init__(self):
        super().__init__()

    def calculate_co2(self, transport_type, distance_km):
        """
        Returns the CO2 in kg for a given mode of transport.
        Raises ValueError for unsupported transport modes or invalid distance.
        """
        if transport_type not in self.EMISSIONS_PER_KM:
            raise ValueError(f"Transport type '{transport_type}' not supported.")
        if distance_km < 0:
            raise ValueError("Distance cannot be negative.")

        co2_per_km = self.EMISSIONS_PER_KM[transport_type]
        return co2_per_km * distance_km

