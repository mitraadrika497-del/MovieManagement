Movie Ticket Booking System

This is a simple Python project for booking movie tickets using the command line.

In this project, the user can:

Select a city

Select a theater

Select a movie

Select a screen

Enter the number of tickets

Select a movie timing

Requirements

You only need:

Python 3

A terminal or command prompt

No extra libraries are required.

Project Structure
movie-ticket-booking/
├── README.md
└── movie_booking.py

How to Run
1. Install Python

Download Python from:

https://www.python.org/downloads/

Check if Python is installed:

python --version


If that doesn't work, try:

python3 --version

2. Open the Project Folder

Open the terminal in the folder where movie_booking.py is present.

Example:

cd movie-ticket-booking

3. Run the Program

On Windows:

python movie_booking.py


On macOS/Linux:

python3 movie_booking.py

How It Works

When the program starts, it asks you to select a city:

1. Ranchi
2. Jamshedpur
3. Delhi


Then you can select a theater:

1. INOX
2. IMAX
3. PJP Cinepolis
4. Back


After that, select a movie:

1. The Batman
2. No Country for Old Men
3. Obsession
4. Back


Finally, select the screen, number of tickets, and show timing.

If everything is selected correctly, the program shows a message like:

Successful!!! Enjoy movie at 1:10-4:10

Dependencies

There are no external dependencies. The project only uses basic Python features like:

Functions

if-else

Dictionaries

User input

print()

Note

This is a basic beginner-level project. It does not store bookings in a database or handle real payments. It is mainly made to practice Python functions and conditional statements.
