def echo(toPrint, wherePrint):
    for i in toPrint:
        cells[wherePrint] = toNumber(i)
        wherePrint += 1
