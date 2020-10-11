# Start with empty dict
candidate_totals = {}
# mock out some data (this will be from the csv file)
fake_data = [['id', 'county','candidate_a'],
             ['id', 'county','candidate_b'],
             ['id', 'county','candidate_a'],
             ['id', 'county','candidate_a']]
# loop through and fill up the dictionary with counts
for row in fake_data:
    # We alldreay have a key with this candidate (note that row[2] is candidate name, therefore increment the count
    if candidate_totals.get(row[2]):
        candidate_totals[row[2]] += 1
    # we have never seen this candidate, add a new key and initialize count to 1
    else:
        candidate_totals[row[2]] = 1
print(candidate_totals)