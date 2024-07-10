from unittest import TestCase, main
import os

from application import Dogschool
from domain import Dog

class Test(TestCase):
    def test_application(self):
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "dogschool.sqlite"
        
        app = Dogschool()
        fido_id = app.register_dog(name="Fido")
        fido_details = app.get_dog(fido_id)
        self.assertEqual(fido_details["name"], "Fido")
        self.assertEqual(fido_details["tricks"], [])
        app.add_trick(fido_id, "roll over")
        fido_details = app.get_dog(fido_id)
        self.assertEqual(fido_details["tricks"], ["roll over"])
        
        buster_id = app.register_dog(name="Buster")
        buster_details = app.get_dog(buster_id)
        self.assertEqual(buster_details["name"], "Buster")
        self.assertEqual(buster_details["tricks"], [])
        app.add_trick(buster_id,"fetch ball")
        buster_details = app.get_dog(buster_id)
        self.assertEqual(buster_details["tricks"], ["fetch ball"])
    
    def test_aggregate(self):
        dog = Dog(name="Fido")
        self.assertEqual(dog.name, "Fido")
        self.assertEqual(dog.tricks, [])
        
        dog.add_trick(trick="roll over")
        self.assertEqual(dog.tricks, ["roll over"])
        dog.add_trick(trick="fetch")
        self.assertEqual(dog.tricks, ["roll over", "fetch"])
        events = dog.collect_events()
        self.assertEqual(len(events), 3)
        
        copy = None
        for event in events:
            copy = event.mutate(copy)
            
        self.assertEqual(copy.name, "Fido")
        self.assertEqual(copy.tricks, ["roll over", "fetch"])
            
if __name__ == '__main__':
    main()
        
        
        
