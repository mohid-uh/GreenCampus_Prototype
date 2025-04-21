class CarbonTracker:
    """
    Calculates carbon footprint based on travel choices.
    """
    EMISSIONS_PER_KM = {
        "car": 0.21,    # kg CO2 per km
        "bus": 0.08,
        "bike": 0.0,
        "walk": 0.0
    }

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

