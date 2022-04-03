import requests

response = requests.get("https://cdn-api.co-vin.in/api/v4/appointment/sessions/public/calendarByDistrict?district_id=395&date=02-04-2022")

pinCode = int(input("Enter pincode:"))
age = int(input("Enter minimum age:"))

dict_response = response.json()
# print(dict_response)

#fetching lists of centers
list_of_center = dict_response["centers"]
for center in list_of_center:    
    if center["pincode"] == pinCode:
        for session in center["sessions"]:
            if session["min_age_limit"] == age:
                print("\n")
                print("Name of Hospital: " + str(center["name"]))
                print("Pincode: " +str(center["pincode"]))
                print("date: " +str(session["date"]))
                print("vaccine: " +str(session["vaccine"]))
                print("Availbility of dose 1: " +str(session["available_capacity_dose1"]))
                print("Availbility of dose 2: " +str(session["available_capacity_dose2"]))