from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    from urllib.parse import parse_qs
    from urllib.parse import urlparse
except ImportError:
    from urlparse import parse_qs
    from urlparse import urlparse

from builtins import input

from example.utils import create_uber_client
from example.utils import fail_print
from example.utils import import_oauth2_credentials
from example.utils import paragraph_print
from example.utils import response_print
from example.utils import success_print

from uber_rides.client import SurgeError
from uber_rides.errors import ClientError
from uber_rides.errors import ServerError

# uber pool
UFP_PRODUCT_ID = '26546650-e557-4a7b-86e7-6a3942445247'

# uber black
SURGE_PRODUCT_ID = 'd4abaae7-f4d6-4152-91cc-77523e8165a4'

# California Academy of Sciences
START_LAT = 37.770
START_LNG = -122.466

# Uber HQ
END_LAT = 37.7752315
END_LNG = -122.418075


def estimate_ride(api_client):
    """Use an UberRidesClient to fetch a ride estimate and print the results.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.
    """
    try:
        estimate = api_client.estimate_ride(
            product_id=SURGE_PRODUCT_ID,
            start_latitude=START_LAT,
            start_longitude=START_LNG,
            end_latitude=END_LAT,
            end_longitude=END_LNG,
            seat_count=1
        )

    except (ClientError, ServerError) as error:
        fail_print(error)

    else:
        success_print(estimate.json)


def update_surge(api_client, surge_multiplier):
    """Use an UberRidesClient to update surge and print the results.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.
        surge_mutliplier (float)
            The surge multiple for a sandbox product. A multiplier greater than
            or equal to 2.0 will require the two stage confirmation screen.
    """
    try:
        update_surge = api_client.update_sandbox_product(
            SURGE_PRODUCT_ID,
            surge_multiplier=surge_multiplier,
        )

    except (ClientError, ServerError) as error:
        fail_print(error)

    else:
        success_print(update_surge.status_code)


def update_ride(api_client, ride_status, ride_id):
    """Use an UberRidesClient to update ride status and print the results.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.
        ride_status (str)
            New ride status to update to.
        ride_id (str)
            Unique identifier for ride to update.
    """
    try:
        update_product = api_client.update_sandbox_ride(ride_id, ride_status)

    except (ClientError, ServerError) as error:
        fail_print(error)

    else:
        message = '{} New status: {}'
        message = message.format(update_product.status_code, ride_status)
        success_print(message)


def request_ufp_ride(api_client):
    """Use an UberRidesClient to request a ride and print the results.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.

    Returns
        The unique ID of the requested ride.
    """
    try:

        estimate = api_client.estimate_ride(
            product_id=UFP_PRODUCT_ID,
            start_latitude=START_LAT,
            start_longitude=START_LNG,
            end_latitude=END_LAT,
            end_longitude=END_LNG,
            seat_count=2
        )
        fare = estimate.json.get('fare')

        request = api_client.request_ride(
            product_id=UFP_PRODUCT_ID,
            start_latitude=START_LAT,
            start_longitude=START_LNG,
            end_latitude=END_LAT,
            end_longitude=END_LNG,
            seat_count=2,
            fare_id=fare['fare_id']
        )

    except (ClientError, ServerError) as error:
        fail_print(error)
        return

    else:
        success_print(estimate.json)
        success_print(request.json)
        return request.json.get('request_id')


def request_surge_ride(api_client, surge_confirmation_id=None):
    """Use an UberRidesClient to request a ride and print the results.

    If the product has a surge_multiple greater than or equal to 2.0,
    a SurgeError is raised. Confirm surge by visiting the
    surge_confirmation_url and automatically try the request again.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.
        surge_confirmation_id (string)
            Unique identifer received after confirming surge.

    Returns
        The unique ID of the requested ride.
    """
    try:
        request = api_client.request_ride(
            product_id=SURGE_PRODUCT_ID,
            start_latitude=START_LAT,
            start_longitude=START_LNG,
            end_latitude=END_LAT,
            end_longitude=END_LNG,
            surge_confirmation_id=surge_confirmation_id,
            seat_count=2
        )

    except SurgeError as e:
        surge_message = 'Confirm surge by visiting: \n{}\n'
        surge_message = surge_message.format(e.surge_confirmation_href)
        response_print(surge_message)

        confirm_url = 'Copy the URL you are redirected to and paste here: \n'
        result = input(confirm_url).strip()

        querystring = urlparse(result).query
        query_params = parse_qs(querystring)
        surge_id = query_params.get('surge_confirmation_id')[0]

        # automatically try request again
        return request_surge_ride(api_client, surge_id)

    except (ClientError, ServerError) as error:
        fail_print(error)
        return

    else:
        success_print(request.json)
        return request.json.get('request_id')


def get_ride_details(api_client, ride_id):
    """Use an UberRidesClient to get ride details and print the results.

    Parameters
        api_client (UberRidesClient)
            An authorized UberRidesClient with 'request' scope.
        ride_id (str)
            Unique ride identifier.
    """
    try:
        ride_details = api_client.get_ride_details(ride_id)

    except (ClientError, ServerError) as error:
        fail_print(error)

    else:
        success_print(ride_details.json)


if __name__ == '__main__':
    """Run the example.

    Create an UberRidesClient from OAuth 2.0 Credentials, update a sandbox
    product's surge, request and complete a ride.
    """
    credentials = import_oauth2_credentials()
    api_client = create_uber_client(credentials)

    # ride request with upfront pricing flow

    paragraph_print("Request a ride with upfront pricing product.")
    ride_id = request_ufp_ride(api_client)

    paragraph_print("Update ride status to accepted.")
    update_ride(api_client, 'accepted', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)
    update_ride(api_client, 'in_progress', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)

    paragraph_print("Update ride status to completed.")
    update_ride(api_client, 'completed', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)

    # ride request with surge flow

    paragraph_print("Ride estimates before surge.")
    estimate_ride(api_client)

    paragraph_print("Activate surge.")
    update_surge(api_client, 2.0)

    paragraph_print("Ride estimates after surge.")
    estimate_ride(api_client)

    paragraph_print("Request a ride with surging product.")
    ride_id = request_surge_ride(api_client)

    paragraph_print("Update ride status to accepted.")
    update_ride(api_client, 'accepted', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)
    update_ride(api_client, 'in_progress', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)

    paragraph_print("Update ride status to completed.")
    update_ride(api_client, 'completed', ride_id)

    paragraph_print("Updated ride details.")
    get_ride_details(api_client, ride_id)

    paragraph_print("Deactivate surge.")
    update_surge(api_client, 1.0)
