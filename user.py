# user class for storing points data for prototype
class User:
  def __init__(self, username, points=0):
    self.username = username
    self.points = 0

# allows points to be added to a user's points (e.g. when using a sustainable transport method)
# user gets notified when they reach a point milestone
  def add_points(self, points):
    self.points += points
    if self.points == 100:
      print(f'You\'ve reached 100 points! Congratulations!')
    if self.points == 250:
      print(f'You\'ve reached 250 points! Congratulations!')
    if self.points == 500:
      print(f'You\'ve reached 500 points! Congratulations!')
    if self.points == 1000:
      print(f'You\'ve reached 1000 points! Congratulations!')

# user can view their points
  def view_points(self):
    print(f'Your current points total is {self.points}.')

# easy way for developers to see the string data rather than object data
  def __str__(self):
    return f'Username: {self.username}, Points: {self.points}'



      
      
