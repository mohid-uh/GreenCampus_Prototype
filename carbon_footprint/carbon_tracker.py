class CarbonTracker:
    """
    Calculates carbon footprint based on travel choices.
    """
    EMISSIONS_PER_KM = {
        "car": 0.21,    # kg CO2 per km (example)
        "bus": 0.08,
        "bike": 0.0,
        "walk": 0.0
    }
