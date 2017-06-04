"""Create views and route them to jinja2 files."""
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound
import os


JOURNAL_ENTRIES_DICT = [
    {
        'id': 13,
        'title': 'James Salamonsen Day 13',
        'creation_date': 'Thursday, 1 June, 2017, 8:17 pm',
        'body': """Today we touched on using SQLand python. We are using a database instead of a local file for our stored information. I am having troubles with my Postgres and MYSQL linking up with the correct versions. That is the only thing thats not letting me pass, other then that my server looks good."""
    },
    {
        'id': 12,
        'title': 'James Salamonsen Day 12',
        'creation_date': 'Thursday, 1 June, 2017, 8:15 am',
        'body': """Today we did more pyramid but learned a few neat tricks. Jinja2 is a lifesaver when working with python and web pages. Its like handlebars on steroids! lol anyway we also looked at binary heap data structure today. I honestly don't understand how to do it without make a left and right child, but more testing will help."""
    },
    {
        'id': 11,
        'title': 'James Salamonsen Day 11',
        'creation_date': 'Thursday, 1 June, 2017, 8:13 am',
        'body': """We started doing pyramid stuff today and it isn't actually that bad. We got our server set up ion python and got our port serving our html pages. Pretty neat to see the difference between python and javascript."""
    },
    {
        'id': 10,
        'title': 'James Salamonsen Day 10',
        'creation_date': ' Friday, 26 May, 2017, 6:59 pm',
        'body': """Today we picked up concurrency and added it to our server. We now have the ability to accept more then one request at a time. Far be it from processing those requests at the same time, but a step in the right direction."""
    },
    {
        'id': 9,
        'title': 'James Salamonsen Day 9',
        'creation_date': 'Thursday, 25 May, 2017, 3:59 pm',
        'body': """Learning how to make a queue out of our double linked list wasn't too difficult. But for some reason I had an issue with setting up step3 on our server. However after some research I was able to see how to get it completed :D"""
    },
    {
        'id': 8,
        'title': 'James Salamonsen Day 8',
        'creation_date': 'Wednesday, 24 May, 2017, 6:56 pm',
        'body': """We worked on double linked lists today and I actually picked up the concept pretty easily. We also implemented step2 to our server and we wrote some tests for it. That also went pretty smoothly as well."""
    },
    {
        'id': 7,
        'title': 'James Salamonsen Day 7',
        'creation_date': 'Tuesday, 23 May, 2017, 5:44 pm',
        'body': """Today was all about HTTP and using its methods. HTTP allows us to send and receive messages from a server so we can use methods like GET, POST, PUT and DELETE. In our code we added the response ok and response error methods. We could then get a response of 200 when we get a correct response back from the server or a response of 500 when we have an internal server error."""
    },
    {
        'id': 6,
        'title': 'James Salamonsen Day 6',
        'creation_date': 'Monday, 22 May, 2017, 8:50 pm',
        'body': """We learned about setting up server and client side sockets so they can communicate. My partner and I were having a little trouble getting the pytest to work. We kept on getting connection refused as our error. I am sure that we will be able to fix it tomorrow."""
    },
    {
        'id': 5,
        'title': 'James Salamonsen Day5',
        'creation_date': 'Friday, 19 May, 2017, 9:21 pm',
        'body': """Today's practice was great! I feel like key points of python and built in aspects got drilled into my brain. I also like the fact that it upped my level on codewars!"""
    },
    {
        'id': 4,
        'title': 'James Salamonsen Day 4',
        'creation_date': 'Friday, 19 May, 2017, 9:08 am',
        'body': """We learned how to use tox today and it was showed to us that it can test over python 2.7 and 3.6. This one is especially handy, definitely saves time. I can't wait to start the KATAS!!!"""
    },
    {
        'id': 3,
        'title': 'James Salamonsen Day3',
        'creation_date': 'Wednesday, 17 May, 2017, 8:06 pm',
        'body': """The only real thing that I need a little work on is setting up packages. I was having trouble working through some of the logic but my partner was able to walk me through the issues. In the end we got nice working code and pass our tests."""
    },
    {
        'id': 2,
        'title': 'Day2',
        'creation_date': 'Tuesday, 16 May, 2017, 5:47 pm',
        'body': """We acquired some good testing skills today. We also learned about using modules and packages, which gave us our testing abilities. As our pair programming for today we defined some functions to find the nth value in the Fibonacci sequence. Eric nd I actually had a little difficulty figuring out how to get our functions to count up to the right value. But we did some research and figured it out. The python section of things really wasn't that difficult, just some logic."""
    },
    {
        'id': 1,
        'title': 'LJ Code 401 Day 1',
        'creation_date': 'Monday, 15 May, 2017, 3:40 pm',
        'body': """We finally got to get started on learning python today! I had some trouble setting up the ENV so I need to work on that. But I am familiar with python so most everything else was easy to understand. I cannot wait to get into some more difficult python situations."""
    }
]


HERE = os.path.dirname(__file__)

@view_config(route_name='list_view', renderer='../templates/listing.jinja2')
def list_view(request):
    """View for the main listing page."""
    return {"journal_entries": JOURNAL_ENTRIES_DICT}


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """Detailed view for one journal entry based on it's id."""
    the_id = int(request.matchdict['id'])
    try:
        # TODO: FIX SO THAT WE GET CORRECT ENTRY!!
        entry = JOURNAL_ENTRIES_DICT[the_id]

    except IndexError:
        raise HTTPNotFound

    return {
        'entry': entry
    }


@view_config(route_name='create_view', renderer='../templates/create.jinja2')
def create_view(request):
    return {}


@view_config(route_name='update_view', renderer='../templates/update.jinja2')
def update_view(request):
    """View to make changes to a journal entry."""
    the_id = int(request.matchdict['id'])
    try:
        # TODO: FIX SO THAT WE GET CORRECT ENTRY!!
        entry = JOURNAL_ENTRIES_DICT[the_id]

    except IndexError:
        raise HTTPNotFound

    return {
        'entry': entry
    }
