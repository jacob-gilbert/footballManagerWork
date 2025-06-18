# turns football manager squad data into a pandas dataframe

import pandas as pd

def create_player_df():
    line_list = []
    with open("squad_text.rtf") as file: # add name of file if in the same folder; if not in same folder include file path
        count = 0
        for line in file:
            if count % 2 == 0: # only want even lines because odds ones are full lines of "-"
                stripped_line = line.strip() # remove white space
                if stripped_line != "": # if an entire line is all whitespace ignore it
                    line_list.append(stripped_line.split("|")) # add the lines to a list after splitting each one by |
            count += 1

    # create initial dataframe
    df = pd.DataFrame(line_list, columns = ["Index", "Sel Pos", "Inf", "Name", "Pos", "Best Pos", "Best Role", "Age", "Nat", "Agr Play Time", "Ablty", "Pot", "Sal", "TV", "Extra"])
    df = df.drop(0) # first row has repeat column names

    # construct new dataframe with only essential information
    df = df[["Name", "Pos", "Best Pos"]]
    return df