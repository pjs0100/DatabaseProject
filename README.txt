Priority Queue System
Author: Patrick Straub

The Priority Queue System is an example database management system that employees of a fictional theme park to manage "priority queue" appointments, similar to Disney's Fastpass.

In order to run the priority queue system, first you must run a mysql server on localhost with the user 'root' and the password ''.
Then you need to run PatrickStraub_Generate.sql in order to instantiate the database.

Then you can run source.py which was written in Python 3.8. You will also need tkinter and mysql.connector installed on your machine.
source.py will open a window with 3 query buttons and 3 areas to add/remove from the database.
Employees are able to query the database for a list of appointments for each guest. They are also able to query the database for a list of all available appointments.
Employees are able to query the database for a list of all guests in the park. They can add and remove guests. They can also add/remove entries from the available appointments table and add/remove appointments for each guest.
