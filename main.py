import pandas as pd
listOfSignedUp = pd.read_csv("maile1.csv")
listOfRunners = pd.read_csv("maile2.csv")
 
listOfSignedUp.rename( columns={'Unnamed: 0':'runnerId'}, inplace=True )
listOfSignedUp.rename( columns={'Unnamed: 1':'emailAddress'}, inplace=True )
hasStarted = listOfSignedUp.numer.isin(listOfRunners['1'])
emailAddressesOfRunners = listOfSignedUp[hasStarted]
emailAddressesOfRunners.to_csv('emailAddressesOfRunners.csv')

