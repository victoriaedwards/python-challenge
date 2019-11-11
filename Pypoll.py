import os
import csv

csvpath = os.path.join('/Users/Victoria/bootcamp/CU-NYC-DATA-PT-10-2019-U-C/Homework/03-Python/Instructions/PyPoll/Resources', 'election_data.csv')


totalVotes=0
candidateNames=set()
candidateInfo= {}
winner=""
winnerNum=0

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        totalVotes=totalVotes+1

        if row[2] in candidateInfo:
            candidateInfo[row[2]]=candidateInfo[row[2]]+1
        else:
            candidateInfo[row[2]]=1

    for row[2] in candidateInfo:
        if candidateInfo[row[2]] > winnerNum:
            winnerNum=candidateInfo[row[2]]
            winner=row[2]

    print(' ')
    print('Election Results')
    print('--------------------------------------')
    print(f"Total Votes: {totalVotes}")
    print('--------------------------------------')
    for key, value in candidateInfo.items():
        print(f'{key} : {round((value/totalVotes*100),3):.3f}% ({value})')
    print('--------------------------------------')
    print(f'Winner: {winner}')
    print('--------------------------------------')

    #print to txt file
    with open("Pypoll_output.txt", "w") as f:
        print(' ', file=f)
        print('Election Results', file=f)
        print('--------------------------------------', file=f)
        print(f"Total Votes: {totalVotes}", file=f)
        print('--------------------------------------', file=f)
        for key, value in candidateInfo.items():
            print(f'{key} : {round((value/totalVotes*100),3):.3f}% ({value})', file=f)
        print('--------------------------------------', file=f)
        print(f'Winner: {winner}', file=f)
        print('--------------------------------------', file=f)



