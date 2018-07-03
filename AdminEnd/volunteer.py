def assign_volunteer():

volunteer_Forecast = 10
volunteer_Interested = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
volunteer_Maybe =['I', 'J', 'K', 'L']
volunteer_selected = []

if volunteer_Forecast <= len(volunteer_Interested):
    for i in range(volunteer_Forecast):
        volunteer_selected.append(volunteer_Interested[i])
    print (volunteer_selected)

elif volunteer_Forecast > len(volunteer_Interested):
    c = volunteer_Interested + volunteer_Maybe
    for i in range(volunteer_Forecast):
        volunteer_selected.append(c[i])
    print (volunteer_selected)

