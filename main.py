from carbon_footprint.carbon_tracker import CarbonTracker
from user import User


def carbon_footprint_flow(carbon_tracker, user):
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

       # Award points based on CO₂ emission
    if co2_emission == 0:
        points = 10
        print("No emissions! You earn 10 GreenPoints.")
    elif 0 < co2_emission <= 0.05:
        points = 5
        print("Low emissions! You earn 5 GreenPoints.")
    elif 0.05 < co2_emission <= 0.1:
        points = 3
        print("You earn 3 GreenPoints for moderate emissions.")
    else:
        points = 0
        print("No GreenPoints for your journey.")

    if points > 0:
        user.add_points(points)

    # Show users current points total
    user.view_points()


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
