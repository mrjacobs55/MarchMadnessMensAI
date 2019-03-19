import csv

# with open('newFile.csv' , "wb") as newFile: writes new file
#    writer = csv.writer(newFile)
#

season = []
with open('WRegularSeasonDetailedResults.csv') as file:
    read = csv.reader(file)
    first = True

    for row in read:
        if not first:
            season.append(row)
        else:
            game = [row[1], row[3], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                    row[15],
                    row[16], row[17], row[18], row[19], row[20], "-1 loss, 1 win"]
            print(game)
            game = [row[1], row[3], row[6], row[7], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                    row[28], row[29], row[30], row[31], row[32], row[33], "-1 loss, 1 win"]
            print(game)
            first = False

with open('WNCAATourneyDetailedResults.csv') as file:
    read = csv.reader(file)
    first = True

    for row in read:
        if not first:
            season.append(row)
        else:
            game = [row[1], row[3], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                    row[15],
                    row[16], row[17], row[18], row[19], row[20], "-1 loss, 1 win"]
            print(game)
            game = [row[1], row[3], row[6], row[7], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                    row[28], row[29], row[30], row[31], row[32], row[33], "-1 loss, 1 win"]
            print(game)
            print("\n\n")
            game = [row[1], row[3][1:], row[6][1:], row[7], row[21][1:], row[22][1:], row[23][1:], row[24][1:],
                    row[25][1:], row[26][1:], row[27][1:], row[28][1:], row[29][1:], row[30][1:], row[31][1:],
                    row[32][1:], row[33][1:], "-1 loss, 1 win"]
            print(game)
        with open('WSeason+TeamID/header.csv', 'w') as headerFile:
            write = csv.writer(headerFile)
            write.writerow(game)

            first = False


# Only Uncomment if you want to edit/create the data files
'''
for row in season:
    with open("WSeason+TeamID/" + row[0] + "+" + row[2] + ".csv", 'a') as winningTeam:
        write = csv.writer(winningTeam)
        winGame = [row[1], row[3], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15],
                   row[16], row[17], row[18], row[19], row[20], 1]
        write.writerow(winGame)
    with open("WSeason+TeamID/" + row[0] + "+" + row[4] + ".csv", 'a') as losingTeam:
        write = csv.writer(losingTeam)
        location = row[6]
        if location == 72:
            location = 65
        else:
            if location == 65:
                location = 72
            else:
                location = 78
        lossGame = [row[1], row[3], location, row[7], row[21], row[22], row[23], row[24], row[25], row[26], row[27],
                    row[28], row[29], row[30], row[31], row[32], row[33], -1]
        write.writerow(lossGame)
'''
