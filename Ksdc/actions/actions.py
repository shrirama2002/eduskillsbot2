# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
from rasa_sdk.types import DomainDict
import re
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,UserUtteranceReverted
import csv



class ActionTellDetails(Action):

    def name(self) -> Text:
        return "action_tell_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot('name')
        pno=tracker.get_slot('ph_no')
        email=tracker.get_slot('email')
        with open("./info.csv",mode="a",newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name,pno,email])
        # print(name,pno,email) #this line prints slot values in action server cmd
        return []

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_name(
                    self,
                    slot_value: Any,
                    dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                    domain: DomainDict,) -> List[Dict[Text, Any]]:
        # print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value)<= 2:
            dispatcher.utter_message(text=f"Thats a very short name. I'm assuming you mis-spelled")
            return {"name": None}
        else:
            if not re.match(r"^[A-Za-z - ]+$",slot_value):
              dispatcher.utter_message(text=f"Thats not a valid name.") 
              return{"name":None}
            else: 
                return{"name": slot_value}
    
    def validate_ph_no(
                    self,
                    slot_value: Any,
                    dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                    domain: DomainDict,) -> List[Dict[Text, Any]]:
        # print(f"Name given = {slot_value} length = {len(slot_value)}")
        if not re.match(r"^[0-9]{10}$",slot_value):
            dispatcher.utter_message(text=f"Thats not a valid number.")
            return {"ph_no": None}
        else:
            return{"ph_no": slot_value}
    
    def validate_email(
                    self,
                    slot_value: Any,
                    dispatcher: CollectingDispatcher,
                     tracker: Tracker,
                    domain: DomainDict,) -> List[Dict[Text, Any]]:
        # print(f"Name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value)<= 5:
            dispatcher.utter_message(text=f"Thats a very short mail. I'm assuming you mis-spelled")
            return {"email": None}
        else:
            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$",slot_value):
              dispatcher.utter_message(text=f"Thats not a valid mail address.") 
              return{"email":None}
            else: 
                return{"email": slot_value}
        
    


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_L1"
    
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Building Supervisory Relationship",
                        "subtitle": "FREE Short Course",
                        "image_url": "http://myeduskills.com/assets/images/dad3bf3d018e6f709238caa03ec385de.jpg",
                        "buttons": [ 
                         
                            {
                            "title": "View",
                            "url": " http://myeduskills.com/coursedetails/index/9",
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": "Sustaining The Supervisory Working Partnership",
                        "subtitle": "FREE Short Course",
                        "image_url": "http://myeduskills.com/assets/images/fc16f4196e456780ea46c007b57111b2.jpg",
                        "buttons": [ 
                            {
                            "title": "View",
                            "url": "http://myeduskills.com/coursedetails/index/10",
                            "type": "web_url"
                            }
                        ]
                    }
                    

                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []


