# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        # TODO: Store the three values in instance attributes.
        self.name=name
        self.course=course
        self.year_level=year_level


    def get_profile(self):
        # TODO: Return the student's information using HTML-like tags.
        return f"<h1>{self.name}</h1>\n<p>Course: {self.course}</p>\n<p>Year Level: {self.year_level}</p>"
        

# Child class for an IT student.
class ITStudent(Student):
    # TODO: Create a class attribute named skill.
    skill="Python"


    def get_skill(self):
        # TODO: Return the programming skill using a <p> tag.
        return f"<p>Programming Skill: {self.skill}</p>"


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        # TODO: Store the title and student object.
        self.title=title
        self.student=student

    def route(self, path):
        # TODO: Return the correct content for /, /profile, or an invalid route.
        if path=="/":
           return f"<h1>{self.title}</h1>"
        elif path=="/profile":
            return f"{self.student.get_profile()}\n{self.student.get_skill()}"
        else:
            return "<h1>404 - Page Not Found</h1>"
 
    def run(self):
        # TODO: Print the app title and test the required routes.
        print(f"{self.title}")
        print(f"\nGET /")
        print(self.route("/"))
        print(f"\nGET /profile")
        print(self.route("/profile"))
        print(f"\nGET /unknown")
        print(self.route("/unknown"))


# Create the student and application objects.
# TODO: Replace the sample information with your own information.
student = ITStudent("Angelito P. Biandilla", "BS Information Technology", 4)
app = StudentApp("PSU Student Profile App", student)

# Start the application.
app.run()