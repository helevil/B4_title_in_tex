import pandas as pd
from make_title import fix_chemical_formula

# Define the output file name
output_file_name = "format_title.txt"

file = "title.csv"
df = pd.read_csv(file)

df = df.sample(frac=1, random_state=None).reset_index(drop=True)  # randomly shuffle all rows

# Apply the fix_chemical_formula function to the relevant columns
df["JP_Topic"] = df["JP_Topic"].apply(fix_chemical_formula)
df["EN_Topic"] = df["EN_Topic"].apply(fix_chemical_formula)

# print("1st check")
# print(df["JP_Topic"])


def format_row(row):
    jp_name = row["JP_Name"]
    jp_topic = row["JP_Topic"]
    jp_lab = row["JP_Lab"]
    en_name = row["EN_Name"]
    en_topic = row["EN_Topic"]
    footnote = row.get("Footnote", "")
    if pd.isna(footnote):
        footnote = ""
    jp_name_with_footnote = f"{jp_name}\\footnote{{{footnote}}}" if footnote else jp_name
    return f"{jp_name_with_footnote}\t&\t{jp_topic}\t&\t{jp_lab}\t\\\\\t&\t{en_name}\t&\t{en_topic}\t&\t\\\\* \\hline"


# Apply the function to all rows
latex_output = "\n".join(df.apply(format_row, axis=1))

# Write the LaTeX output to a new file
with open(output_file_name, "w", encoding="utf-8") as f:
    f.write(latex_output)

print(f"LaTeX formatted table saved to: {output_file_name}")
