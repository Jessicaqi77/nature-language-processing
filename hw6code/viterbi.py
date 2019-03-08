
def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is a size N array of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]

    #initailize the table
    table =  [[0.0 for col in xrange(N)] for row in xrange(L)]
    bp_table =  [[0 for col in xrange(N)] for row in xrange(L)]

    # L rows N cols
    #the first col
    for row in xrange(L) :
        table[row][0] = start_scores[row] + emission_scores[0][row]
        #bp_table =  start_scores[row] + emission_scores[0][row]
    #remain cols

    for col in xrange (1,N) :
        for row in xrange(L) :
            temp_max = -float('inf')
            temp_index = -float('inf')
            for index in xrange(L) :
                temp =  table[index][col-1] + trans_scores[index][row]
                if temp > temp_max :
                    temp_max = temp
                    temp_index = index
            table[row][col] = temp_max + emission_scores[col][row]
            bp_table[row][col]= temp_index

    #end
    max_score = -float('inf')
    last_index = -1
    for row in xrange(L) :
        table[row][-1] = table[row][N-1] + end_scores[row]
        if table[row][-1]> max_score :
            max_score = table[row][-1]
            last_index = row

    #back track
    y = []
    for col in range (N-1, -1, -1) :
        y = [int(last_index)] + y
        last_index = bp_table[int(last_index)][col]


    return (max_score, y)

