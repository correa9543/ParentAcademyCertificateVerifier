import csv

# Using a dictionary to store the parents IDs, the key will be their IDs 
# and the values will be a list of courses that they took
parentIDs = {}
parentCertificates = {}
courseNames = []

# This function is used to open and read from a CSV file 
def openCSV(file):
    with open('ClassesAttendedReference.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)

        for id, course, date in reader:
            if id in parentIDs:
                parentIDs[id].append(course)
            else:
                parentIDs[id] = []
                parentIDs[id].append(course)
                parentCertificates[id] = []

# This function is used to search the courses from the dictionaries that were created below. 
# We compare the courses in the series dictionaries to the courses the parents actually took
def searchCourses():
    for id in parentIDs:
        for series in courseSeries:
            completed = True
            # print(series)
            for courses in courseSeries[series]:
                if courses not in parentIDs[id]:
                    completed = False
                    break
            if completed:    
                parentCertificates[id].append(reverseCourseAbbreviations[series])

# Use this function in order to store certificates in the parentCertificates dictionary       
def storeCertificateNames():
    for id in parentIDs:
        fullCertNames = []
        for abr in parentCertificates[id]:
            fullCertNames.append(courseAbbreviations[abr])
            # parentCertificates[id].append(courseAbbreviations[abr])
            # print(abr)
        parentCertificates[id] = fullCertNames
            
    

# This function is used to display all the certificates the parents have earned
def displayCertificates():
    for id, certificates in parentCertificates:
        print(id, courseAbbreviations[certificates])


# This dictionary holds all the courses in the LinkedIn series
linkedInCourses = [
    "LinkedIn-1",
    "LinkedIn-2"
]

# This dictionary holds all the courses in the Google Drive series
googleDrive = [
    "Google Drive-1",
    "Google Drive-2",
    "Google Drive-3 Pt. 1",
    "Google Drive-3 Pt. 2",
    "Google Drive-4",
    "Google Docs Practice Session",
    "Google Sheets Practice Session"
]

# This dictionary holds all the courses in the Career Exploration series
careerExploration = [
    "Career Exploration Program of Study Pt. 1",
    "Career Exploration Program of Study Pt. 2",
    "Career Exploration Program of Study Pt. 3"
]

# This dictionary holds all the courses in the Zoom series
zoom = {
    "Zoom-1",
    "Zoom-2"
}

# This dictionary holds all the courses in the Typing series
typing = [
    "Typing-1"
]

# This dictionary holds all the courses in the Math series
basicMath = [
    "Math-1 pt. 1",
    "Math-1 pt. 2",
    "Math Reasoning",
    "Math-2 pt. 1",
    "Math-2 pt. 2"
]

# This dictionary holds all the courses in the Career Development series
careerDevelopment = [
    "SMART Goals Pt. 1",
    "SMART Goals Pt. 2",
    "Time Management Pt. 1",
    "Time Management Pt. 2",
    "Public Speaking Pt. 1",
    "Public Speaking Pt. 2",
    "Managing Difficult Conversations Pt. 1",
    "Managing Difficult Conversations Pt. 2",
    "Resume Writing"
]

# This dictionary holds all the codes and their respective representations
courseAbbreviations = {
    "LI": "LinkedIn Course",
    "GD": "Google Drive Course",
    "CE": "Career Exploration Program Of Study",
    "ZO": "Zoom Course",
    "TY": "Typing Course",
    "BM": "Basic Math Course",
    "CD": "Career Development Program Of Study"
}

# This dictionary holds all the codes and their respective representations
reverseCourseAbbreviations = {
    "LinkedIn Course" : "LI",
    "Google Drive Course": "GD",
    "Career Exploration Program Of Study": "CE",
    "Zoom Course": "ZO",
    "Typing Course": "TY",
    "Basic Math Course": "BM",
    "Career Development Program Of Study": "CD"
}

# This dictionary will hold all of the Series that are in the Parent Academy
courseSeries = {
   "LinkedIn Course": linkedInCourses,
   "Google Drive Course": googleDrive,
   "Career Exploration Program Of Study": careerExploration,
   "Zoom Course": zoom,
   "Typing Course": typing,
   "Basic Math Course": basicMath,
   "Career Development Program Of Study": careerDevelopment
}
    


# Function calls
openCSV("ClassesAttendedReference.csv")
searchCourses()
storeCertificateNames()
# displayCertificates()

print ('\n'.join(parentCertificates["4"]), "\n")
print("-------------------------")
print ('\n'.join(parentIDs["4"]), "\n")


