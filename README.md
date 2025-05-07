**1. System description:**

    **A CLI-based sustainability engagement app**
    
    The GreenCampus prototype system is designed to simulate the key features within the proposed GreenCampus app. This system prototypes the carbon footprint tracker, points and 
    leaderboard system, and the energy resource tracker feature. The carbon footprint tracker allows the user to input their mode of transport and the distance the user has travelled,      and calculates the amount of carbon emmissions were outputted based on this data. The user gains points for using low-emmision travel methods. These points are stored to the user's     account, and the user can compete with other users using the points leaderboard, to encourage environmentally-friendly actions. The energy resource tracker... 

    It uses the Publish/Subscribe (Observer) pattern to decouple "event generators" (trackers) from the "PointsManager" subscriber, which awards points.

   **Key Classes & Relationships:**
   
      Publisher / Subscriber (Observer pattern):
   
      - CarbonTracker & EnergyTracker inherit from Publisher
      - PointsManager implements Subscriber
   
      Inheritance: Trackers ← Publisher; PointsManager ← Subscriber
   
      Association: User passed in event data; Tracker holds config dicts

**3. Instructions:**

     The prototype is ran via a menu in the command line interface, the user should follow the prompts to observe the functionalities.

**4. Programming Languages, Frameworks & Tools:**
    - Python
    - PyCharm IDE

**4. Summary of implemented functionalities:**

   User Management
    – CLI-based user selection and session handling

   Carbon Footprint Tracker
    – Enter transport mode & distance → calculate CO₂ → tiered GreenPoints (0 kg→10; ≤5 kg→5; ≤10 kg→3; >10 kg→0)

   Energy Usage Tracker
    – Browse departments/buildings → compute GREEN/YELLOW/RED rating → award GreenPoints (GREEN→5; YELLOW→2)

   Rewards System
    – Publisher/Subscriber pattern decouples trackers from the PointsManager
    – Milestone notifications at 100, 250, 500, 1000 points

   Leaderboard
    – Ranks all users by points with proper ordinal suffixes


**6. Contribution:**
   
    - Mohid (2190944) - carbon tracker functionality; main.py; implemented Publish/Subscribe design pattern; README.
    - Keren - created user.py file, implemented user selection code into main.py, part of README
    - Jonah - user leaderboard code
    - Phoebe - energy resource tracker
    - Liam - energy resource tracker
  
   Contribution is split even (1/5 each).
