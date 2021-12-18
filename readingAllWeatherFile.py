import csv,statistics
def main():
    names = []
    fname = 'weatherFiles.txt'
    with open(fname) as fname:
        lines = fname.readlines()
        for line in lines:
            names.append(line.strip())
    for name in names:
        date,maxT,minT,avgT,snow,windS,relH = [],[],[],[],[],[],[]
        with open(name,'r',newline='') as file_name:
            file = csv.reader(file_name,delimiter = ',')
            headers = next(file)
            for line in file:
                for i in range(len(line)):
                    if line[i] == '':
                        line[i] = 0.0
                date.append(line[1])
                maxT.append(float(line[2]))
                minT.append(float(line[3]))
                avgT.append(float(line[4]))
                snow.append(float(line[8]))
                windS.append(float(line[9]))
                relH.append(float(line[14]))

main()