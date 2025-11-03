#ProcessData.py
#Name:tatiana
#Date:11/2/25
#Assignment:

import csv

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
    writer = csv.writer (outFile)
    writer.writerow([ "Last name", "First name"])
  for line inFile:
    parts = line.strip().split
    if len(parts) !=5
    continue

    first=parts[0]
    last=parts[1]
    student_id=parts[2]
    major=parts[3]
    year=parts[4]

    userid=first[0].lower()+ last.lower()
    if lens(last) <5: 
      userid="x"
    userid + student_id[-3]

    major_code=major[:3].Capitilize()
    if year == "Freshman":
      year_abbr = "FR"
      if year == "Sophmore":
      year_abbr = "SO"
      if year == "Junior":
      year_abbr = "JR"
      if year = "Senior":
      year_abbr = "SR"

      majoryear = major_code + "-" + year_abbr
    
    writer.writerow([last, first, userid, majoryear])
  inFile.close()
  outFile.close()
  print("done")

if __name__ == '__main__':
  main()
