import json
from yandex_geocoder import Client
from geopy import distance


def get_data_from_file():
    with open('bars_data.json', encoding='CP1251') as json_file:
        return json.load(json_file)


def get_user_coords():
    user_location = input('Enter Your current location: ')
    user_lat, user_lon = Client.coordinates(user_location)
    return (user_lon, user_lat)


def get_distance(coords_1, coords_2):
    return distance.distance(coords_1, coords_2).km


def get_bars_list(user_coords):
    bars_list = []

    bars_data = get_data_from_file()
    for bar in bars_data:
        current_bar_data = {
            'title': bar['Name'],
            'latitude': bar['geoData']['coordinates'][0],
            'longitude': bar['geoData']['coordinates'][1],
        }
        bar_coords = (current_bar_data['longitude'], current_bar_data['latitude'])
        current_bar_data['distance'] = get_distance(user_coords, bar_coords)
        bars_list.append(current_bar_data)

    return bars_list


def get_nearest_bars(bars_list):
    return sorted(bars_list, key=lambda bar: bar['distance'])[:5]


def main():
    user_coords = get_user_coords()
    bars_list = get_bars_list(user_coords)
    print(get_nearest_bars(bars_list))


if __name__ == '__main__':
    main()
