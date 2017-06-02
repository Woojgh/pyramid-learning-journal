# Expense Tracker

A simple Pyramid app for listing and displaying expenses.

**Authors**:

- James Salamonsen
- Miguel Pena

## Routes:

- `/` - the home page and a listing of all journal entries
- `/journal/{id:\d+}` - a detail view of one journal entry
- `/journal/new-entry` - the page to create a new journal entry
- `/journal/{id:\d+}/edit-entry` - the page to edit an existing entry

## Set Up and Installation:

- Clone this repository to your local machine.

- Once downloaded, `cd` into the `pyramid-learning-journal` directory.

- Begin a new virtual environment with Python 3 and activate it.

- `cd` into the next `pyramid-learning-journal` directory. It should be at the same level of `setup.py`

- `pip install` this package as well as the `testing` set of extras into your virtual environment.

- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

## To Test

- If you have the `testing` extras installed, testing is simple. If you're in the same directory as `setup.py` type the following:

```
$ tox
```