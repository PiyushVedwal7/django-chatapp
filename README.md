Django Discord-Like Web Application

Overview -->
This project is a web application inspired by Discord, developed using Django. The application includes functionality for users to join rooms, participate in discussions, and manage topics. It serves as a real-time communication platform where users can interact seamlessly.

Features :-
User Authentication:
Register, Login, and Logout.
User-specific features like creating and managing messages.

Room Management:
Create, edit, and delete chat rooms.
Join discussions in various topics.

Topic Browsing:
View a list of available topics.
Search and filter discussions based on topics.

Real-Time Updates:
Messages update dynamically for better communication.

Responsive Design:
Mobile-friendly and desktop-compatible interface.

Tech Stack
Backend: Django 4.x-
Frontend: HTML, CSS, JavaScript (optional frameworks like Bootstrap)
Database: SQLite (default, can be switched to PostgreSQL/MySQL)
Deployment: Compatible with platforms like Heroku, AWS, or any server supporting Django.

Installation
Clone the repository:
git clone https://github.com/yourusername/discord-like-app.git
cd discord-like-app
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Open the application in your browser at http://127.0.0.1:8000/.

Usage

Register a User:

Sign up on the platform to create an account.

Explore Rooms and Topics:

Browse available topics and join rooms for discussions.

Post Messages:

Contribute to discussions by posting messages in rooms.

Manage Content:

Users can delete their own messages or manage rooms they created.

Folder Structure

project_root/
|-- buddy/                     # Main Django app directory
|   |-- templates/             # HTML templates
|   |   |-- base/              # Shared components (navbar, footer)
|   |   |-- rooms/             # Room-specific templates
|   |   `-- users/             # User-related templates
|   |-- static/                # Static files (CSS, JS, images)
|   `-- views.py               # Views for handling requests
|-- manage.py                  # Django management script
|-- requirements.txt           # Python dependencies
|-- db.sqlite3                 # SQLite database (default)

Known Issues

Some UI elements might not display properly on very small screens.

Real-time updates require refreshing the page (if WebSocket support is not implemented).

Future Enhancements

Add WebSocket support for true real-time messaging.

Improve search and filtering capabilities.

Implement user profiles with avatars and bio.

Deploy the application on a live server.
