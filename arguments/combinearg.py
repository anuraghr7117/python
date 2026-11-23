def employee(name, department,*skills, salary=20000, **details):

    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Skills:", skills)
    print("Additional Details:", details)


employee(
    "Anuragh",
    "ISE",
    "Python",
    "Linux",
    "Git",
    city="Bangalore",
    experience="Beginner"
)