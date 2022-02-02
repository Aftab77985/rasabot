from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet 
from rasa_sdk.executor import CollectingDispatcher
from database_connection import feedback

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet('feedback', tracker.latest_message['text'])]
        
class Actionfeedbacksubmit(Action):

    def name(self) -> Text:
        return "action_thanks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        var = tracker.get_slot('feedback')
        feedback(var)
        dispatcher.utter_message(text="Thanks for your valuable feedback")
        return []

        