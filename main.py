''' GET UPDATED WITH THE COVID-19 VACCINATION CENTERS IN INDIA
    You can run the .exe file attached in the files
    -- PROJECT BY PRANAV ARORA

    STAY HOME. STAY SAFE
'''

from cowin_api import CoWinAPI
from datetime import datetime

cowin = CoWinAPI()

try:
    def display_centers(available_centers):
        '''Function used to store and display vaccination centers'''
        if len(available_centers['centers']) != 0:
            for center in available_centers['centers']:
                print('\n\n\n')
                f.write('-------------------------------\n')

                print(f'Center ID: {center["center_id"]}')
                f.write(f'Center ID: {center["center_id"]}\n')

                print(f'Name: {center["name"]}')
                f.write(f'Name: {center["name"]}\n')

                print(f'Address: {center["address"]}')
                f.write(f'Address: {center["address"]}\n')

                print(f'State Name: {center["state_name"]}')
                f.write(f'State Name: {center["state_name"]}\n')

                print(f'District Name: {center["district_name"]}')
                f.write(f'District Name: {center["district_name"]}\n')

                print(f'Block Name: {center["block_name"]}')
                f.write(f'Block Name: {center["block_name"]}\n')

                print(f'PINCODE: {center["pincode"]}')
                f.write(f'PINCODE: {center["pincode"]}\n')

                print(f'Latitude: {center["lat"]}')
                f.write(f'Latitude: {center["lat"]}\n')

                print(f'Longitude: {center["long"]}')
                f.write(f'Longitude: {center["long"]}\n')

                print(f'From: {center["from"]}')
                f.write(f'From: {center["from"]}\n')

                print(f'To: {center["to"]}')
                f.write(f'To: {center["to"]}\n')

                print(f'Fee Type: {center["fee_type"]}')
                f.write(f'Fee Type: {center["fee_type"]}\n')
                for session in center['sessions']:
                    print(f'Session ID: {session["session_id"]}')
                    f.write(f'Session ID: {session["session_id"]}\n')

                    print(f'Date: {session["date"]}')
                    f.write(f'Date: {session["date"]}\n')

                    print(f'Available Capacity: {session["available_capacity"]}')
                    f.write(f'Available Capacity: {session["available_capacity"]}\n')

                    print(f'Minimum Age Limit: {session["min_age_limit"]}')
                    f.write(f'Minimum Age Limit: {session["min_age_limit"]}\n')

                    print(f'Vaccine: {session["vaccine"]}')
                    f.write(f'Vaccine: {session["vaccine"]}\n')

                    print(f'Slots: {session["slots"]}')
                    f.write(f'Slots: {session["slots"]}\n')
                    print('\n\n')
                    f.write('\n\n\n')
            f.write('Stay Home. Stay Safe!!')
            f.close()
            print('This information has been stored in your computer. Search "cowin" to find the file.')
        else:
            print('Data Not Available')

    # Getting the States
    states = cowin.get_states()
    for state in states.values():
        try:
            for id in state:
                print(f'{id.get("state_id")} - {id.get("state_name")}')
        except TypeError:
            pass
    state_id = input('Enter the State Code (ex - 2 is the State Code for Andhra Pradesh): ')

    # Getting the Districts
    districts = cowin.get_districts(state_id)
    for district in districts.values():
        try:
            for id in district:
                print(f'{id.get("district_id")} - {id.get("district_name")}')
        except TypeError:
            pass
    # Implementing the given input values to query the vaccination centers
    district_id = input('Enter the District Code: ')
    date = input('Enter the date (DD-MM-YYYY): ')  # Optional. Takes today's date by default
    available_centers = cowin.get_availability_by_district(district_id, date)
    f = open(f'cowin-{datetime.timestamp(datetime.now())}.txt', 'w')
    f.write('CENTER AVAILABILITY BY DISTRICT\n')
    display_centers(available_centers)

    # Getting the vaccination centers data through PINCODE
    query = input('Do you want to search the vaccine center with your pincode (yes/no)? ')
    if 'yes' in query:
        pin_code = input("Enter your pincode: ")
        date = input("Enter the date (DD-MM-YYYY): ")  # Optional. Default value is today's date
        available_centers = cowin.get_availability_by_pincode(pin_code, date)
        f = open(f'cowin-{datetime.timestamp(datetime.now())}.txt', 'w')
        f.write('CENTER AVAILABILITY BY PINCODE\n')
        display_centers(available_centers)
    else:
        print('Sure. Stay Safe. Stay Healthy')

    while True:
        quit = input('Press "q" to quit: ')
        if 'q' in quit:
            break
except Exception:
    print('Sorry!! An error occured!!')
    while True:
        quit = input('Press "q" to quit: ')
        if 'q' in quit:
            break