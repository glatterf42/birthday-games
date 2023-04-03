template = """\\documentclass[a4paper, 9pt, DIV=13, onecolumn]{{scrartcl}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{tabularray}}
\\usepackage{{caption}}

\\begin{{document}}
\\thispagestyle{{empty}}

\\begin{{table}}
    \\centering
    \\SetTblrInner{{vspan=even}}
    \\begin{{tblr}}{{width=\\linewidth, colspec={{|X[c]|X[c]|X[c]|X[c]|X[c]|}}, rowspec={{|X[m]|X[m]|X[m]|X[m]|X[m]|}}, colsep=.5cm, rowsep=.5cm}}
    {0} & {1} & {2} & {3} & {4} \\\\
    {5} & {6} & {7} & {8} & {9} \\\\
    {10} & {11} & {12} & {13} & {14} \\\\
    {15} & {16} & {17} & {18} & {19} \\\\
    {20} & {21} & {22} & {23} & {24} \\\\

    \end{{tblr}}
    \caption*{{Kennenlernbingo für {name}: Viel Spass beim Raten :) }}
\end{{table}}

\\end{{document}}
"""
