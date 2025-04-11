# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from rasa_sdk import Action
from rasa_sdk.events import EventType

class ActionSendWelcomeMessage(Action):
    def name(self) -> str:
        return "action_send_welcome_message"

    def run(self, dispatcher, tracker, domain) -> list [EventType]:
        # Στείλτε το μήνυμα καλωσορίσματος
      
        dispatcher.utter_message(text= "Γειά! 👋\n\n"
                                   "Είμαι το LessonBot, το chatbot του μαθήματος Ανάλυση και Σχεδίαση Συστημάτων"
                                    "και είμαι εδώ για να σας βοηθήσω! \n\n"
                                    "Η επικοινωνία μας γίνεται στα ελληνικά.\n\n"
                                    "Μπορώ να σας παρέχω πληροφορίες για βαθμολογίες,\n\n"
                                    "εργασίες, εργαστήρια, προθεσμίες και άλλα. 📚💡\n\n")
        
        # Στείλτε τα κουμπιά με τις επιλογές
        dispatcher.utter_message(
            text="✏️Πληκτρολόγησε την ερώτησή σου ή επίλεξε μία από τις διαθέσιμες επιλογές παρακάτω.",
            buttons=[
                {"title": "Κανονισμός Εργασιών", "payload": "/ask_assignment_info"},
                {"title": "Θεωρία & Εργατήριο", "payload": "/ask_course_info"},
                {"title": "Προθεσμίες Υποβολής εργασιών", "payload": "/deadline_info"},
                {"title": "Οδηγίες Δήλωσης Ομάδας", "payload": "/ask_group_project_info"},
                {"title": "Αντικείμενο Ομαδικής Εργασίας", "payload": "/project_content"},
                {"title": "Πρόγραμμα Μαθημάτων", "payload": "/course_schedule"},
                {"title": "Διδασκοντες Μαθήματος", "payload": "/professor_info"},
                {"title": "Συγγράμματα", "payload": "/book_info"},
                {"title": "Χρήσιμα Βιβλία", "payload": "/ask_useful_book_info"},
                {"title": "Χρήσιμοι Σύνδεσμοι Μαθήματος", "payload": "/ask_useful_link_info"},
                {"title": "Αξιολόγηση Chatbot", "payload": "/chatbot_evaluation"}
            ]
        )
        return []

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#
#
# crasalass ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
