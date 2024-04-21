import pandas as pd

df = pd.read_csv("OHDC_26\\nato_phonetic_alphabet.csv")

phrase_input = input("What word or phrase would you like to convert to nato phonetic?: ")

def phrase_to_nato(input:str) -> list:
    return [df[df.letter == letter].iloc[0]["code"] for letter in input if len(df[df.letter == letter]) == 1]

print(phrase_to_nato(input=phrase_input.upper().replace(" ","")))