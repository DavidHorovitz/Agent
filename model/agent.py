class Agent:
    def __init__(self, id,codeName , realName, location, status, missionsCompleted):
        self.id=id
        self.codeName=codeName
        self.realName=realName
        self.location=location
        self.status=status
        self.missionsCompleted=missionsCompleted
    def __str__(self):
        return f"Agent {self.codeName} (ID: {self.id}): {self.status}, missions: {self.missionsCompleted}"
