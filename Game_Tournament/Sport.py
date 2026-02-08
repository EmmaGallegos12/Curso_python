"""Sport class rpresents a sport in the tournament, It has a name and a league."""
class Sport:
    """Sport class represents a sport in the tournament. It has a name and a league"""
    def __init__(self, name, num_players, league):
        """Custom constructor for sport class."""
        self.name = name
        self.league = league
        self.num_player = num_players
    def __str__(self):
        """String representation of the sport object."""
        return f"Sport name is {self.name}, League: {self.league}, Number of players: {self.num_player}"
    
    def __repr__(self):
        """String representation of the Sport class."""
        return f"Sport(name='{self.name}', league='{self.league}', num_players={self.num_player})"
    
    def to_json(self):
        """Convert the sport object to a JSON-serializable dictionary."""
        return {
            'name': self.name,
            'league': self.league,
            'num_players': self.num_player
        }
    

if __name__ == "__main__":
    sport1 = Sport("Football", 11, "Premier League")
    sport2 = Sport("Basketball", 10, "NBA")
    print(sport2)
    print(repr(sport2))
    print(sport2.to_json())
    print(sport1)
    print(repr(sport1))
    print(sport1.to_json())
