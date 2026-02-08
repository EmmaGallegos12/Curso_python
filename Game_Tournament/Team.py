from Athelete import Athlete
from Sport import Sport

class Team:
    """ Team class represent a team in the tournament, It has a name, a sport and a list of athletes."""

    def __init__(self, name, sport:Sport):
        """Custom constructor for Team class."""
        self.name = ""
        self.sport = None
        self.athletes = []

    def add_athlete(self, athlete):
        """Add an athlete to the team."""
        if isinstance(athlete, Athlete):
            self.athletes.append(athlete)
        else:
            raise TypeError("Only Athelete objects can be added to the team.")
        

if __name__ == "__main__":
    team1 = Team("Lakers", "Basketball")
    team1.name = "Lakers"
    sport1 = Sport("Basketball", 10, "NBA")
    athlete1 = Athlete("Michael Jordan")
    athlete2 = Athlete("LeBron James")
    
    team1.add_athlete(athlete1)
    team1.add_athlete(athlete2)
    
    print(f"Team Name: {team1.name}")
    print(f"Sport: {sport1}")
    print("Athletes in the team:")
    for athlete in team1.athletes:
        print(athlete)
        

