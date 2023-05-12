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
print(sheet_data)

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    # print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.date.today()
tommorow = today + datetime.timedelta(days=1)
end_date_for_search = tommorow + datetime.timedelta(days=180)

tommorow = tommorow.strftime('%d/%m/%Y')
end_date_for_search = end_date_for_search.strftime('%d/%m/%Y')

for row in sheet_data:
    flight = flight_search.check_flights(
        sheet_data,
        ORIGIN_CITY_IATA,
        row['iataCode'],
        from_time=tommorow,
        to_time=end_date_for_search
    )

    if flight.price < row['lowestPrice']:
        MESSAGE = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        notification_manager.send_sms(MESSAGE)
