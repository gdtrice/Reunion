import csv

with open('pbhsStudentInfo.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    html = "<table><tr><th>First Name</th><th>Last Name</th><th>Email Address</th></tr>"

    for row in reader:
        html = html + "<tr><td>" + row[0] + "</td>" + "<td>" + row[1] + "</td>" + "<td>" + row[2] + "</td></tr>" 
        # print ', '.join(row)

html = html + "</table>"
print html
