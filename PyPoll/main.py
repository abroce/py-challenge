import csv
import os

path = os.path.join("Resources", "election_data.csv")

def analysis():
    with open(path, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=",")

        total_votes = 0
        candidates = []
        vote_numbers = []
        vote_percentages = []
        winner =  ""
        

        next(data, None)
        for i in data:
            if i[-1] not in candidates:
                candidates.append(i[-1])
                vote_numbers.append(1)
            else:
                index = candidates.index(i[-1])
                vote_numbers[index] += 1
            total_votes += 1
        for j in vote_numbers:
            percentages = "{0:.3f}".format(round((j/total_votes)*100, 2))
            vote_percentages.append(percentages) 
        
        winner_index = vote_percentages.index(max(vote_percentages))
        winner = candidates[winner_index]
            

        output = ''
        output += 'Election results \n-------------------------\n'
        output += 'Total votes: ' + str(total_votes) + '\n-------------------------\n'
        output += str(candidates[0]) + ': ' + str(vote_percentages[0]) + '% ' + '(' + str(vote_numbers[0]) + ')\n'
        output += str(candidates[1]) + ': ' + str(vote_percentages[1]) + '% ' + '(' + str(vote_numbers[1]) + ')\n' 
        output += str(candidates[2]) + ': ' + str(vote_percentages[2]) + '% ' + '(' + str(vote_numbers[2]) + ')\n' 
        output += str(candidates[3]) + ': ' + str(vote_percentages[3]) + '% ' + '(' + str(vote_numbers[3]) + ')\n'
        output += '-------------------------\nWinner: ' + str(winner)  

        print(output)

    text_file = open('Analysis/Election_Results.txt', 'w')
    text_file.write(output)
    text_file.close()



def main():
    analysis()

main()