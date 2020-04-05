import pandas as pd

def jaccard_score( value1: list, value2: list ) -> float:
    c = 0
    d = 0
    for value in value1:
        if value in value2:
        	c = c + 1
        d = len( value1 ) + len( value2 )
        score = float( c / d )
    return score

def jaccard_calc( df, col_name ):
    sentences = df[ col_name ].to_numpy( ).tolist( )
    for i in range( len( sentences ) ):
        words1 = sentences[ i ].split( )
        for k in range( i + 1, len( sentences ) ):
            words2 = sentences[ k ].split( )
            score = jaccard_score( words1, words2 )
            yield sentences[ i ], sentences[ k ], score

df = pd.read_excel("data.xlsx")

jacgnrtr = jaccard_calc(df,'Example')

with open("results.csv","w",encoding="utf8") as f:
    for sentence1, sentence2, score in jacgnrtr:
        print( sentence1 + "|" + sentence2 + "|" + str(score) )
        f.write(sentence1 + "," + sentence2 + "," + str(score) + "\n" )
f.close()