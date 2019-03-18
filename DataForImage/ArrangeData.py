import csv

# with open('newFile.csv' , "wb") as newFile: writes new file
#    writer = csv.writer(newFile)
#

season = []
with open('RegularSeasonDetailedResults.csv') as file:
    read = csv.reader(file)
    first = True

    for row in read:
        if not first:
            season.append(row)
        else:
            print(row)
            first = False

with open('NCAATourneyDetailedResults.csv') as file:
    read = csv.reader(file)
    first = True

    for row in read:
        if not first:
            season.append(row)
        else:
            print(row)
            first = False

for row in season:
    with open("Season+TeamID/" + row[0] + "+" + row[2] + ".csv", 'w') as winningTeam:
        write = csv.writer(winningTeam)
        winGame = [row[1], row[3], row[6], row[7], row[8], row[9], row[10], row[11],
                   row[12], row[13], row[14], row[15], row[16], row[17],
                   row[18], row[19], row[20], 1]
        write.writerow(winGame)
    with open("Season+TeamID/" + row[0] + "+" + row[4] + ".csv", 'w') as losingTeam:
        write = csv.writer(losingTeam)
        location = row[6]
        if location == 72:
            location = 65
        else:
            if location == 65:
                location = 72
            else:
                location = 78
        lossGame = [row[3], location, row[7], row[21], row[22],
                    row[23], row[24], row[25], row[26], row[27],
                    row[28], row[29], row[30], row[31],
                    row[32], row[33], -1]
        write.writerow(lossGame)
