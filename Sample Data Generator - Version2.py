import csv #for manipulating csv files
import random #for generating random numbers
import os #for creating files and directories
import re #for creating search patterns for matching
import datetime #for manipulating dates
import twilio #for sending text messages


#Set Python Working Directory
baseDirectory = '/Users/Keith_Macbook/Desktop/Big Data Stuff/Python/'

# Create a Directory for the output files (if it doesn't exist)
outputDirectory = baseDirectory + 'Sample Files/'
if os.path.exists(outputDirectory) == False:
    os.makedirs(outputDirectory)
    print('Directory Created')
else:
    print('Directory Exists')

#Create the Dummy Data

#Create the Order Number
orderNumber = 1

#Create Dummy Customers
customer = [
    'ABC Motors',
    'DC Telecom',
    'FG Engineering',
    'MGK Entertainment',
    'ZZ Topps',
    'XYZ Furniture',
    'HH Smith and Sons',
    'PP Driving Instructors',
    'S&T Computers',
    'Querty Keyboards'
    ]

#Create Dummy Products
product = [
    'Hammer',
    'Screwdriver',
    'Drill',
    'Pliers',
    'Box of 100 Nails',
    'Box of 250 Screws'
    ]
    
#Create Dummy Customer Locations
location = [
    'Aberdeen,Scotland',
    'Edinburgh,Scotland',
    'London,England',
    'Manchester,England',
    'Newcastle,England',
    'Cardiff,Wales',
    'Dublin,Ireland'
    ]

#Create Dummy Order Date
orderDate = [
    '10/09/2014',
    '05/11/2014',
    '25/12/2014',
    '01/01/2015',
    '14/02/2015',
    '17/03/2015',
    '01/04/2015',
    '04/07/2015'
    ]

#Create the Output File and Add the Column Headers (overwrite it if it already exists using 'w' argument vs 'a')
fileName = 'output.csv' #creates a comma delimited file with line breaks
outputFile = open(outputDirectory + str(fileName), 'w') #file created if it doesn't exist (and overwritten if it does)
outputWriter = csv.writer(outputFile, delimiter=',', lineterminator='\n')
outputWriter.writerow(['Order Number', 'Customer Name', 'Shipping City', 'Shipping Country', 'Product Name', 'Quantity Ordered', 'Order Date'])

#Create the dummy data
for i in range (50): #set this equal to the number of records to be created
    orderNumber = i + 1 #increment order number (vs random where you could get duplicates)
    customerName = random.choice(customer) #select customer randomly from list
    productName = random.choice(product) #select product randomly from list
    orderQuantity = random.randint(10,50) #select a random order quantity
    shippingLocation = random.choice(location) #select a location randomly from list
    productOrderDate = random.choice(orderDate) #select a data randomly from list

#Parse the Shipping Location Into City and Country
    shippingLocation = shippingLocation.split(',')
    shippingCity = shippingLocation[0]
    shippingCountry = shippingLocation[1]

#Write the new record to the file
    outputWriter.writerow([orderNumber, customerName, shippingCity, shippingCountry, productName, orderQuantity, productOrderDate])

#Close the file when the loop completes
outputFile.close()

print('Sample Data File Created')
    
#Select a subset of records from the file (outputfile overwritten using 'w' arg)
inputFileName = fileName
outputFileName = 'extract.csv'
inputFile = open(outputDirectory + inputFileName, 'r')
outputFile = open(str(outputDirectory) + str(outputFileName), 'w')
fileReader = csv.reader(inputFile)
outputWriter = csv.writer(outputFile, delimiter=',',lineterminator = '\n')

for row in fileReader:
    rowNum = fileReader.line_num
    if (rowNum == 1):
        outputWriter.writerow(row)

    else:

# Add row if it is less than specified value        
#        if int(row[5]) < 30:
#            outputWriter.writerow(row)

# Add row if order is on specified date (string needs same delimiters as input (i.e.%d/%m/%Y for 01/03/2015))
         if datetime.datetime.strptime(row[6], '%d/%m/%Y') == datetime.datetime(2015,3,17): #datetime needs to be YMD, etc. NO LEADING ZEROS
#         if datetime.datetime.strptime(row[6], '%d/%m/%Y') < datetime.datetime(2015,3,17):
#         if datetime.datetime.strptime(row[6], '%d/%m/%Y') > datetime.datetime(2015,3,17):     
            outputWriter.writerow(row)


# Add row if it matches specific text        
#       if row[3] == 'Scotland': 
#           outputWriter.writerow(row)

#Search for text matches
#        wildcardName = re.compile (r'.*Eng.*', re.I) # Looks for the string value 'Eng' (not case sensitive) anywhere in the input row
#        nameSearch = re.compile(wildcardName)
#        result = nameSearch.findall(str(row))
#        if len(result) != 0:
#            outputWriter.writerow(row)

#Close Output File
outputFile.close()

#Count the records written to the output file (need to reopen the file as readable (not writable))
outputFile = open(outputDirectory + outputFileName, 'r')
fileReader = csv.reader(outputFile)
i = 0
for row in fileReader: 
    i = i + 1
dt = datetime.datetime.now()
timeNow = dt.strftime('%b %d, %Y (%H:%M:%S)')
message = 'Completed: ' + timeNow + '. ' + 'Number of Records written to output file = ' + str(i-1) + ' (excluding the header row)'
print(message)

#Send text message to my phone
#accountSID = "ACbcfe4e730439280aa4c52f4d20fab521" 
#authToken = "f93f22ff12201861a005b8f99f6ed162" 
#twilioCli = twilio.rest.TwilioRestClient(accountSID, authToken)
#myTwilioNumber = '+441158243338'
#myCellPhone = '+447795314893'
#stextMessage = twilioCli.messages.create(body= message, from_=myTwilioNumber, to=myCellPhone)

outputFile.close()


     
            
            
 
 
    
    
    

