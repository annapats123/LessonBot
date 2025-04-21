LessonBot is a conversational chatbot developed to offer administrative support to university students. It was created by Anna Patsourakou, a postgraduate student as part of a master's thesis in the field of Information Systems at the Hellenic Open University, under the supervision of Professor Efthymios Tampouris, for the course "Analysis and Design of Systems".

The chatbot was built using the Rasa platform, an open-source framework for building AI assistants. Rasa was chosen for its flexibility, transparency, and strong support for natural language understanding, making it ideal for creating a customized solution tailored to the needs of a university environment.

LessonBot was specifically created for the students of the University of Macedonia, with the goal of providing immediate and consistent access to essential academic and administrative information, especially outside of regular office hours. It helps students find answers to common queries without delays, while also reducing the workload of administrative and academic staff.

Specifically, LessonBot can:

•	Answer frequently asked questions about course structures and schedules

•	Provide information about assignments, grading, and exam dates

•	Share details about instructors, office hours, and contact info

•	Direct students to useful links and official resources

•	Offer updates on lab schedules and textbook requirements

The chatbot is focused solely on administrative support, not on teaching or tutoring, and is available 24/7 through a user-friendly web H

How to train the Chatbot

The models folder is not included in the project file. Therefore, after downloading the project, you need to train the chatbot manually.

To do this, open a terminal inside the project directory and run:

rasa train

This command will generate a new models/ folder containing the trained model, based on the data provided in the data/ and domain.yml files.



