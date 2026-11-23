def student_details(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])
    print("Department:", details["department"])

student_details(
    name="Anuragh",
    age=21,
    department="ISE"
)