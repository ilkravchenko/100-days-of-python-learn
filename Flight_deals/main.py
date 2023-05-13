from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
import datetime

ORIGIN_CITY_IATA = "LON"
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_all_data()

if sheet_data[0]['iataCode'] == '':
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)

    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data}

today = datetime.date.today()
tommorow = today + datetime.timedelta(days=1)
end_date_for_search = tommorow + datetime.timedelta(days=180)

tommorow = tommorow.strftime('%d/%m/%Y')
end_date_for_search = end_date_for_search.strftime('%d/%m/%Y')

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tommorow,
        to_time=end_date_for_search
    )

    ################
    if flight is None:
        continue
    ################

    if flight.price < destinations[destination_code]["price"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        MESSAGE = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            MESSAGE += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, MESSAGE)
