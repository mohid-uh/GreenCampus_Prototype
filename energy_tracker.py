class EnergyTracker:
    def __init__(self):
        # List to hold subscribers (e.g., PointsManager) for the Observer pattern
        self.subscribers = []

        # Hard coded building data with realistic university buildings
        self.building_dict = {
            'building_1': {
                'name': 'Maths Lecture Hall',
                'department': 'Watson Building of Mathematics',
                'energy': 120,  # kW per day
                'hours_open': 12  # Hours per day
            },
            'building_2': {
                'name': 'Central Library',
                'department': 'General',
                'energy': 250,
                'hours_open': 24
            },
            'building_3': {
                'name': 'The Guild of Students',
                'department': 'UOB Student Union',
                'energy': 80,
                'hours_open': 18
            },
            'building_4': {
                'name': 'Chemistry Lab',
                'department': 'Chemistry, Molecular Sciences Building',
                'energy': 200,
                'hours_open': 10
            },
            'building_5': {
                'name': 'Computer Science Building',
                'department': 'School of Engineering; Computer Science',
                'energy': 150,
                'hours_open': 14
            },
            'building_6': {
                'name': 'Physics Lab',
                'department': 'School of Physics and Astronomy',
                'energy': 180,
                'hours_open': 10
            },
            'building_7': {
                'name': 'Engineering Workshop',
                'department': 'School of Engineering',
                'energy': 300,
                'hours_open': 8
            },
            'building_8': {
                'name': 'Chemical, environmental, biomedical science greenhouses/labs',
                'department': 'Molecular Sciences Building',
                'energy': 250,
                'hours_open': 9
            },
            'building_9': {
                'name': 'Maths Tutorial Rooms',
                'department': 'Watson Building, School of Mathematics',
                'energy': 60,
                'hours_open': 10
            },
            'building_10': {
                'name': 'School of History and Cultures Lecture Theatre 2',
                'department': 'Arts Building',
                'energy': 100,
                'hours_open': 10
            }
        }

    def subscribe(self, subscriber):
        """Add a subscriber (e.g., PointsManager) to receive notifications."""
        self.subscribers.append(subscriber)

    def notify(self, event, data):
        """Notify all subscribers of an event (e.g., points earned)."""
        for subscriber in self.subscribers:
            subscriber.update(event, data)

    def get_energy_rating(self, building_key):
        """Calculate energy rating based on energy usage per hour."""
        building = self.building_dict[building_key]
        energy = building['energy']
        hours_open = building['hours_open']
        if hours_open == 0:
            return "UNKNOWN/NA"
        energy_per_hour = energy / hours_open
        if energy_per_hour <= 5:
            return "GREEN"
        elif energy_per_hour <= 15:
            return "YELLOW"
        else:
            return "RED"

    def get_departments(self):
        """Return a sorted list of unique departments."""
        departments = set(building['department'] for building in self.building_dict.values())
        return sorted(list(departments))

    def select_building(self, user):
        """Allow user to select a building and provide feedback with points."""
        print("\n=== Energy Tracker ===")

        # Display departments
        departments = self.get_departments()
        print("Available departments:")
        for i, dept in enumerate(departments, 1):
            print(f"{i}. {dept}")

        # Get department selection
        try:
            dept_choice = int(input("Select a department number: ")) - 1
            selected_dept = departments[dept_choice]
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
            return

        # Get buildings in the selected department
        buildings_in_dept = [key for key, val in self.building_dict.items() if val['department'] == selected_dept]
        if not buildings_in_dept:
            print("No buildings found in this department.")
            return

        # Display buildings with ratings
        print(f"\nBuildings in {selected_dept}:")
        for i, key in enumerate(buildings_in_dept, 1):
            building = self.building_dict[key]
            rating = self.get_energy_rating(key)
            print(f"{i}. {building['name']} ({rating})")

        # Get building selection
        try:
            building_choice = int(input("Select a building number: ")) - 1
            selected_building_key = buildings_in_dept[building_choice]
            selected_building = self.building_dict[selected_building_key]
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
            return

        # Display building details
        energy = selected_building['energy']
        hours_open = selected_building['hours_open']
        rating = self.get_energy_rating(selected_building_key)
        print(f"\nYou selected {selected_building['name']}.")
        print(f"Daily energy usage: {energy} kW")
        print(f"Hours open: {hours_open}")
        print(f"Energy rating: {rating}")

        # Award points based on rating
        if rating == "colour code: GREEN":
            points = 5
            print("You chose an energy-efficient building! You earn 5 GreenPoints.")
        elif rating == "colour code: YELLOW":
            points = 2
            print("You chose a moderately efficient building. You earn 2 GreenPoints.")
        else:
            points = 0
            print("This building has high energy usage. No GreenPoints earned.")

        if points > 0:
            self.notify("ENERGY_EFFICIENT_CHOICE", {"user": user, "points": points})

        # Provide feedback and tips
        if rating == "colour code: GREEN":
            print("Great choice! Keep using energy-efficient buildings.")
        elif rating == "colour code: YELLOW":
            print("Tip: Consider turning off lights and equipment when not in use by students, staff or guests to save energy.")
        else:
            print("Tip: Minimise time in high-energy buildings or explore alternatives in the same department.")
