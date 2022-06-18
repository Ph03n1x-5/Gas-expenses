# importing all functions from myCustomFunctions
from myCustomFunctions import *

# declaring empty lists
gasExpenses35 = []
gasExpenses35And50 = []
gasExpenses50And95 = []
unsortedGasPrices = []
sortedGasPrices = []

fileName,outFile = createOutputFile() # call the function to create the external output file

externalFile="weeklyGasExpenses.txt"

# handling unsorted gas prices
# checks whether the file exists
if fileExists(externalFile):
	# readData function read data from a txt file and converts it to a list of floats
	unsortedGasPrices=readData(externalFile)
	outFile.write("Unsorted List : ".center(60) + "\n")
	

# sorting the gas prices
unsortedGasPrices.sort()
sortedGasPrices=unsortedGasPrices

outFile.write("Sorted List : ".center(60) + "\n")

# writing vaues less than or equal to 35
outFile.write("Gas Expenses >= 35".center(60) + "\n")
gasExpenses35 = writeGas35(sortedGasPrices)

# writing values greater than 35 and less than or equal to 50
outFile.write("Gas Expenses >35 and <= 50".center(60) + "\n")
gasExpenses35And50 = writeGas35and50(sortedGasPrices)

# writing values greater than 50 and less than or equal to 95
outFile.write("Gas Expenses > 50.00 and <= 95.00".center(60) + "\n")
gasExpenses50And95 = writeGas50and95(sortedGasPrices)

# finding maximum gas expenses
maximum = max(sortedGasPrices)
# finding minimum gas prices
minimum = min(sortedGasPrices)
# finding average gas prices
average = round(sum(sortedGasPrices)/len(sortedGasPrices),2)

# writing maximum gas prices
outFile.write("Maximum gas expenses = " + format(max(unsortedGasPrices), "6.2f").center(60) + "\n")

# writing minimum gas prices
outFile.write("Minimum gas expenses = " + format(min(unsortedGasPrices), "6.2f").center(60) + "\n")

# writing average gas prices
outFile.write("Average gas expenses = " + format(average, "6.2f").center(60) + "\n")


# handling price reports
# expenses <= 35
report35 = gasReport35(sortedGasPrices)
# expenses > 35 and <= 50
report35and50 = gasReport35And50(sortedGasPrices)
# expenses > 50 and <= 95
report50and95 = gasReport50And95(sortedGasPrices)


outFile.write("Expenses above 35 = %i \n"%report35)
outFile.write("Expenses above 35 and below or equal to 50 = %i\n"%report35and50)
outFile.write("Expenses above 50 and below or equal to 95= %i\n"%report50and95)

# close external file
outFile.close()

# END PROGRAM
