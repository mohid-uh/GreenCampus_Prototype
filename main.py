from carbon_footprint.carbon_tracker import CarbonTracker
from user import User


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

    # example users
    users = {
        '1': User('John'),
        '2': User('Jane'),
        '3': User('Jack')
    }

    current_user = None

    while True:
        # Main menu loop
        print("\n=== GreenCampus Prototype ===")
        print("1) Select User")
        print("2) Carbon Footprint Tracker")
        print("3) View Points")
        print("0) Exit")

        choice = input("Enter option number: ").strip()

        if choice == '1':
            print("Select User:")
            for key, user in users.items():
                print(f"{key}: {user.username}")
            selected = input("Enter user number: ").strip()
            if selected in users:
                current_user = users[selected]
                print(f"You are logged in as {current_user.username}.")
            else:
                print("Invalid user selection.")

        elif choice == '2':
            if current_user:
                carbon_footprint_flow(carbon_tracker, current_user)
            else:
                print("Please select a user first.")

        elif choice == '3':
            if current_user:
                current_user.view_points()
            else:
                print("Please select a user first.")

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter one of the menu numbers.")


if __name__ == "__main__":
    main()
