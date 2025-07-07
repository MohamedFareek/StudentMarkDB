student={"student A":{"math":88,"sci":97,"che":75},
        "Student B":{"math":73,"sci":77, "che":92},
        "Student C":{"math":96,"sci":88,"che":77}}

def mark_analizing(data):
    print("Total and average")
    for student, subjects in data.items():
        total=sum(subjects.values())
        avg=total/len(subjects)
        print(f"{student} Total={total}, Average={avg:.2f}")
    print()


def toppers (data):
    print("toppers")
    subjects=list(next(iter(data.values())).keys())
    for subject in subjects:
        topper=max(data.items(),key=lambda item:item[1][subject])
        print(f"{subject}: {topper[0]} with {topper [1] [subject]}marks")
    print()

def display(data):
    for student, marks in data.items():
        print(f" {student}: {marks}")
    print()

display(student)
mark_analizing(student)
toppers (student)