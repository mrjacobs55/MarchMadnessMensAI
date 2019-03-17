import csv

conferences = []
with open('Conferences.csv') as confDataFile:
    conferencesFile = csv.reader(confDataFile)
    first = True
    for row in conferencesFile:
        if not first:
            conferences.append(row)
        else:
            print(row)
            first = False

teams = []
head = []
with open('TeamConferencesNumerical.csv') as confDataFile:
    teamsFile = csv.reader(confDataFile)
    first = True
    for row in teamsFile:
        if not first:
            teams.append(row)
        else:
            print(row)
            head = row
            first = False
            
head.append("Conf ID")

for row in teams:
    for conf in conferences:
        if conf[1] == row[2]:
            row.append(conf[0])



with open('TeamConferenceID.csv', 'w') as IDdataFile:
    write = csv.writer(IDdataFile)
    first = True
    for row in teams:
        if not first:
            write.writerow(row)
        else:
            write.writerow(head)
            first = False










