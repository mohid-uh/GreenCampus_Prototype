from carbon_footprint.carbon_tracker import CarbonTracker


def carbon_footprint_flow(carbon_tracker):
    print("\n=== Carbon Footprint Tracker ===\n")

    # Prompt for travel choice
    modes = list(CarbonTracker.EMISSIONS_PER_KM.keys())
    print("Available transport modes:", ", ".join(modes))
    transport_type = input("Enter your mode of travel: ").strip().lower()

    # Prompt for distance
    try:
        distance = float(input("Enter distance traveled (in km): ").strip())
    except ValueError:
        print("Invalid distance. Please enter a numeric value.")
        return

    # Calculate CO2 and display
    try:
        co2_emission = carbon_tracker.calculate_co2(transport_type, distance)
        print(f"\nYou traveled by {transport_type} for {distance} km.")
        print(f"Estimated CO₂ emissions: {co2_emission} kg")
    except ValueError as e:
        print(f"Error: {e}")
        return


def main():
    carbon_tracker = CarbonTracker()

    # Main menu
    print("=== GreenCampus Prototype ===")
    print("1) Carbon Footprint Tracker")
    print("0) Exit")

    choice = input("Enter option number: ").strip()

    if choice == '1':
        carbon_footprint_flow(carbon_tracker)
    else:
        print("Goodbye!")
        return

if __name__ == "__main__":
    main()
