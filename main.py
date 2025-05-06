from carbon_footprint.carbon_tracker import CarbonTracker
from user import User
from gamification.points_manager import PointsManager
from energy_tracker import EnergyTracker

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
    elif 0 < co2_emission <= 0.1:
        points = 5
        print("Low emissions! You earn 5 GreenPoints.")
    elif 0.1 < co2_emission <= 0.5:
        points = 3
        print("You earn 3 GreenPoints for moderate emissions.")
    else:
        points = 0
        print("No GreenPoints for your journey.")

    # publishes an event for PointsManager.
    if points > 0:
        carbon_tracker.notify(
            event="ECO_TRAVEL_LOG",
            data={"user": user, "points": points}
        )

    # Show users current points total
    user.view_points()


def select_user(users):
    print("\nSelect User:")
    for key, user in users.items():
        print(f"{key}: {user.username}")
    selected = input("Enter user number: ").strip()
    if selected in users:
        current_user = users[selected]
        print(f"You are logged in as {current_user.username}.")
        return current_user
    else:
        print("Invalid user selection.")
        return None


def get_user_points(user):
    return user[1]


def display_leaderboard(users):
    users = users
    user_tuples = []
    for user in users.values():
        user_tuples.append((user.username, user.points))

    sorted_users = sorted(user_tuples, key=get_user_points, reverse=True)

    print(f"\n=== Green Points Leaderboard ===")
    i = 1
    for user in sorted_users:
        suffix = str(i)[-1]
        second_figure = None
        if i > 10:
            second_figure = str(i)[-2]
            if second_figure != "1":
                second_figure = None

        if suffix == "1" and not second_figure:
            place = str(i) + "st"
        elif suffix == "2" and not second_figure:
            place = str(i) + "nd"
        elif suffix == "3" and not second_figure:
            place = str(i) + "rd"
        else:
            place = str(i) + "th"

        print(f"{place} place is {user[0]}: {user[1]} green points")
        i += 1

def main():
    carbon_tracker = CarbonTracker()
    points_manager = PointsManager()
    energy_tracker = EnergyTracker()

    carbon_tracker.subscribe(points_manager)
    energy_tracker.subscribe(points_manager)

    # example users
    users = {
        '1': User('John', 20),
        '2': User('Jane', 25),
        '3': User('Jack', 45),
        '4': User('Amy', 150),
        '5': User('Adam', 63),
        '6': User('Bob', 81),
        '7': User('Alex', 5),
        '8': User('Lucy', 108),
        '9': User('Jake', 0),
        '10': User('Paula', 207),
    }

    current_user = None

    while True:
        # Main menu loop
        print("\n=== GreenCampus Prototype ===")
        print("1) Select User")
        print("2) Carbon Footprint Tracker")
        print("3) View Points")
        print("4) Energy Usage Tracker")
        print("5) View Leaderboard")
        print("0) Exit")

        choice = input("Enter option number: ").strip()

        if choice == '1':
            current_user = select_user(users)

        elif choice == '2':
            if current_user:
                carbon_footprint_flow(carbon_tracker, current_user)
            else:
                print("Please select a user first.")
                current_user = select_user(users)

        elif choice == '3':
            if current_user:
                current_user.view_points()
            else:
                print("Please select a user first.")
                current_user = select_user(users)

        elif choice == '4':
            if current_user:
                energy_tracker.select_building(current_user)
            else:
                print("Please select a user first.")

        elif choice == '5':
            display_leaderboard(users)

        elif choice == '0':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter one of the menu numbers.")

if __name__ == "__main__":
    main()
