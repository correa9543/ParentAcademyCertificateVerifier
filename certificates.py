import csv

# Using a dictionary to store the parents IDs, the key will be their IDs 
# and the values will be a list of courses that they took
parentIDs = {}
parentCertificates = {}
courseNames = []

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

# this function is checking if the courses the parents took are in the list of series
#I need to compare the items in the lists of series to the list of courses parents took
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
            
    


def displayCertificates():
    for id, certificates in parentCertificates:
        print(id, courseAbbreviations[certificates])


linkedInCourses = [
    "LinkedIn-1",
    "LinkedIn-2"
]

googleDrive = [
    "Google Drive-1",
    "Google Drive-2",
    "Google Drive-3 Pt. 1",
    "Google Drive-3 Pt. 2",
    "Google Drive-4",
    "Google Docs Practice Session",
    "Google Sheets Practice Session"
]

careerExploration = [
    "Career Exploration Program of Study Pt. 1",
    "Career Exploration Program of Study Pt. 2",
    "Career Exploration Program of Study Pt. 3"
]

zoom = {
    "Zoom-1",
    "Zoom-2"
}

typing = [
    "Typing-1"
]

basicMath = [
    "Math-1 pt. 1",
    "Math-1 pt. 2",
    "Math Reasoning",
    "Math-2 pt. 1",
    "Math-2 pt. 2"
]

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

courseAbbreviations = {
    "LI": "LinkedIn Course",
    "GD": "Google Drive Course",
    "CE": "Career Exploration Program Of Study",
    "ZO": "Zoom Course",
    "TY": "Typing Course",
    "BM": "Basic Math Course",
    "CD": "Career Development Program Of Study"
}

reverseCourseAbbreviations = {
    "LinkedIn Course" : "LI",
    "Google Drive Course": "GD",
    "Career Exploration Program Of Study": "CE",
    "Zoom Course": "ZO",
    "Typing Course": "TY",
    "Basic Math Course": "BM",
    "Career Development Program Of Study": "CD"
}


courseSeries = {
   "LinkedIn Course": linkedInCourses,
   "Google Drive Course": googleDrive,
   "Career Exploration Program Of Study": careerExploration,
   "Zoom Course": zoom,
   "Typing Course": typing,
   "Basic Math Course": basicMath,
   "Career Development Program Of Study": careerDevelopment
}
    



openCSV("ClassesAttendedReference.csv")
searchCourses()
storeCertificateNames()
# displayCertificates()

print ('\n'.join(parentCertificates["4"]), "\n")
# print(courseAbbreviations["CD"])
# print(parentCertificates)
print ('\n'.join(parentIDs["4"]), "\n")


