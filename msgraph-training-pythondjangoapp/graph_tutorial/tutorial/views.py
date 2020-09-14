# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from tutorial.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from tutorial.graph_helper import get_user, get_calendar_events, get_sharepoint_sites, get_sharepoint_site, get_teams
import dateutil.parser

# <HomeViewSnippet>

def home(request):
    context = initialize_context(request)

    return render(request, 'tutorial/home.html', context)
# </HomeViewSnippet>

# <InitializeContextSnippet>


def initialize_context(request):
    context = {}

    # Check for any errors in the session
    error = request.session.pop('flash_error', None)

    if error != None:
        context['errors'] = []
        context['errors'].append(error)

    # Check for user in the session
    context['user'] = request.session.get('user', {'is_authenticated': False})
    return context
# </InitializeContextSnippet>

# <SignInViewSnippet>


def sign_in(request):
    # Get the sign-in URL
    sign_in_url, state = get_sign_in_url()
    # Save the expected state so we can validate in the callback
    request.session['auth_state'] = state
    # Redirect to the Azure sign-in page
    return HttpResponseRedirect(sign_in_url)
# </SignInViewSnippet>

# <SignOutViewSnippet>


def sign_out(request):
    # Clear out the user and token
    remove_user_and_token(request)

    return HttpResponseRedirect(reverse('home'))
# </SignOutViewSnippet>

# <CallbackViewSnippet>


def callback(request):
    # Get the state saved in session
    expected_state = request.session.pop('auth_state', '')
    # Make the token request
    token = get_token_from_code(request.get_full_path(), expected_state)

    # Get the user's profile
    user = get_user(token)

    # Save token and user
    store_token(request, token)
    store_user(request, user)

    return HttpResponseRedirect(reverse('home'))
# </CallbackViewSnippet>

# <CalendarViewSnippet>


def calendar(request):
    context = initialize_context(request)

    token = get_token(request)

    events = get_calendar_events(token)

    if events:
        # Convert the ISO 8601 date times to a datetime object
        # This allows the Django template to format the value nicely
        for event in events['value']:
            event['start']['dateTime'] = dateutil.parser.parse(
                event['start']['dateTime'])
            event['end']['dateTime'] = dateutil.parser.parse(
                event['end']['dateTime'])

        context['events'] = events['value']

    return render(request, 'tutorial/calendar.html', context)
# </CalendarViewSnippet>

# <SharePointViewSnippet>
def sharepoint(request):
    context = initialize_context(request)

    token = get_token(request)

    sites = get_sharepoint_sites(token)

    if sites:
        context['sites'] = sites['value']

    return render(request, 'tutorial/sharepoint.html', context)
# </SharePointViewSnippet>


#
def site_details(request, id):
    context = initialize_context(request)
    token = get_token(request)
    # firstComma = id.find(',')
    # secondComma = id.find(',')
    siteId = id.split(",")[1]
    site = get_sharepoint_site(token, siteId)
    if site:
        context['site'] = site

    return render(request, 'tutorial/site_details.html', context)


# <TeamsViewSnippet>


def msteams(request):
    context = initialize_context(request)

    token = get_token(request)

    teams = get_teams(token)

    if teams:
        context['teams'] = teams['value']

    return render(request, 'tutorial/teams.html', context)
# </TeamsViewSnippet>
