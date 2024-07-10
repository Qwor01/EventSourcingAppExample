from domain import Dog


from eventsourcing.application import Application


class Dogschool(Application):
    def register_dog(self,name):
        dog = Dog(name=name)
        self.save(dog)
        return dog.id

    def get_dog(self, dog_id):
        dog = self.repository.get(dog_id)
        return {"name": dog.name, "tricks": (dog.tricks)}

    def add_trick(self, dog_id, trick):
        dog = self.repository.get(dog_id)
        dog.add_trick(trick)
        self.save(dog)