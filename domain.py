from eventsourcing.domain import Aggregate, event


class Dog(Aggregate):
    @event("Registered")
    def __init__(self, name):
         self.name = name
         self.tricks = []

    @event("Trick Added")
    def add_trick(self,trick):
        self.tricks.append(trick)