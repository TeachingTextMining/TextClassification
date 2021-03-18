import pandas as pd

def load_data_tripadvisor(path:str):
    '''
    Funcion que procesa la base de datos a partir de la ruta en que se encuentra
    '''  
    df = pd.read_csv(path, sep='\t', index_col=0, names=['text', 'score'])
    df['Opinion'] = df['text'].str.split('_PROS_Liked_—_').str.get(0)
    df['PROS'] = df['text'].str.split('_PROS_Liked_—_').str.get(1).str.split('_CONS_Disliked_—_').str.get(0).str.replace('_', ' ')
    df['CONS'] = df['text'].str.split('_PROS_Liked_—_').str.get(1).str.split('_CONS_Disliked_—_').str.get(1).str.replace('_', ' ')
    df['Sentiment'] = df.apply(lambda row: get_score_tripadvisor(row),axis=1)
    return df
    
    
def get_score_tripadvisor(row):
    '''
    Funcion para reducir el abanico de puntuaciones a predecir.
    0: Negativa
    1: Neutral
    
    2: Positiva
    '''
    score = int(row['score'])
    if score < 3:
        return 0
    elif score < 4:
        return 1
    else:
        return 2