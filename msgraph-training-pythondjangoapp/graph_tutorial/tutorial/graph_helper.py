# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <FirstCodeSnippet>
from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'


def get_user(token):
    graph_client = OAuth2Session(token=token)
    # Send GET to /me
    user = graph_client.get('{0}/me'.format(graph_url))
    # Return the JSON result
    return user.json()
# </FirstCodeSnippet>

# <GetCalendarSnippet>


def get_calendar_events(token):
    graph_client = OAuth2Session(token=token)

    # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'subject,organizer,start,end',
        '$orderby': 'createdDateTime DESC'
    }

    # Send GET to /me/events
    events = graph_client.get(
        '{0}/me/events'.format(graph_url), params=query_params)
    # Return the JSON result
    return events.json()
# </GetCalendarSnippet>

# <GetSharePointSnippet>


def get_sharepoint_sites(token):
    graph_client = OAuth2Session(token=token)

    # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'id, displayName,webUrl,createdDateTime,lastModifiedDateTime',
        '$orderby': 'createdDateTime DESC'
    }

    # Send GET to /sites
    sites = graph_client.get(
        # '{0}/me/followedSites'.format(graph_url), params=query_params)
        '{0}/sites?search=*'.format(graph_url), params=query_params)
    # Return the JSON result
    return sites.json()
# </GetSharePointSnippet>

def get_sharepoint_site(token, id):
    graph_client = OAuth2Session(token=token)

    # Send GET to /sites
    querystring = '{0}/sites/' + id
    print(querystring)
    site = graph_client.get(
        querystring.format(graph_url))
    # Return the JSON result
    return site.json()

# <GetTeamsSnippet>


def get_teams(token):
    graph_client = OAuth2Session(token=token)

    # Configure query parameters to
    # modify the results
    query_params = {
        '$select': 'displayName,description,id'
    }

    # Send GET to /me/events
    teams = graph_client.get(
        '{0}/me/joinedTeams'.format(graph_url), params=query_params)
    # Return the JSON result
    return teams.json()
# </GetTeamsSnippet>
