import pandas as pd
import re

token_map = {
    '[PAD]': '[PAD]', '[SOS]': '[SOS]', '[EOS]': '[EOS]',
    'G': 'G', 'A': 'A', 'S': 'S', 'P': 'P', 'V': 'V', 'T': 'T',
    'C': 'C', 'L': 'L', 'I': 'I', 'N': 'N', 'D': 'D', 'Q': 'Q',
    'K': 'K', 'E': 'E', 'M': 'M', 'H': 'H', 'F': 'F', 'R': 'R',
    'Y': 'Y', 'W': 'W', 'M[UNIMOD:35]': 'M[UNIMOD:35]',
    'C[UNIMOD:4]': 'C[UNIMOD:4]', 'N[UNIMOD:7]': 'N[UNIMOD:7]',
    'Q[UNIMOD:7]': 'Q[UNIMOD:7]', 'S[UNIMOD:21]': 'S[UNIMOD:21]',
    'T[UNIMOD:21]': 'T[UNIMOD:21]', 'Y[UNIMOD:21]': 'Y[UNIMOD:21]',
    '[UNIMOD:1]': '[UNIMOD:1]', '[UNIMOD:5]': '[UNIMOD:5]',
    '[UNIMOD:385]': '[UNIMOD:385]'
}



def tokenize(sequence):
    tokens = []
    i = 0
    while i < len(sequence):
        matched = False

        for token in sorted(token_map.keys(), key=lambda x: -len(x)):
            if sequence[i:i + len(token)] == token:
                tokens.append(token)
                i += len(token)
                matched = True
                break

        if not matched:

            tokens.append(sequence[i])
            i += 1

    return ', '.join(tokens)


# Read the Excel file
df = pd.read_excel('Mouse_modified.xlsx')


df['preds_tokenised'] = df['preds'].apply(tokenize)


df.to_excel('Mouse_tokenized.xlsx', index=False)

print(df[['preds', 'preds_tokenised']].head())
