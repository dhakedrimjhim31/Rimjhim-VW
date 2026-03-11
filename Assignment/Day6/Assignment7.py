# -----------------------------
# 1️⃣ Base Class: Company
# -----------------------------
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show_details(self):
        print("\nCompany Name:", self.name)
        print("Location:", self.location)


# -----------------------------
# 2️⃣ Base Class: Employee
# -----------------------------
class Employee:
    def __init__(self, emp_id, emp_name, designation, **kwargs):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation
        super().__init__(**kwargs)

    def show_details(self):
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.emp_name)
        print("Designation:", self.designation)


# -----------------------------
# 3️⃣ Company Acquisition
# -----------------------------
class CompanyAcquisition(Company):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_details(self):
        super().show_details()
        print("\nTotal Employees After Acquisition:", len(self.employees))
        print("\n===== Employee Details =====")
        for emp in self.employees:
            emp.show_details()


# -----------------------------
# 4️⃣ Multi-level Inheritance
# -----------------------------
class NewEmployee(Employee):
    def __init__(self, joining_date, previous_company, **kwargs):
        self.joining_date = joining_date
        self.previous_company = previous_company
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Joining Date:", self.joining_date)
        print("Previous Company:", self.previous_company)


# -----------------------------
# 5️⃣ Specialized Roles
# -----------------------------
class Manager(NewEmployee):
    def __init__(self, team_size, **kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Team Size:", self.team_size)


class HR(NewEmployee):
    def __init__(self, policies_handled, **kwargs):
        self.policies_handled = policies_handled
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Policies Handled:", self.policies_handled)


class Developer(NewEmployee):
    def __init__(self, programming_languages, **kwargs):
        self.programming_languages = programming_languages
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Programming Languages:", ", ".join(self.programming_languages))


class Intern(NewEmployee):
    def __init__(self, duration, **kwargs):
        self.duration = duration
        super().__init__(**kwargs)

    def show_details(self):
        super().show_details()
        print("Internship Duration:", self.duration)


# -----------------------------
# 6️⃣ Multiple Inheritance
# -----------------------------
class HRManager(Manager, HR):
    def __init__(self, team_size, policies_handled, **kwargs):
        super().__init__(team_size=team_size,
                         policies_handled=policies_handled,
                         **kwargs)

    def show_details(self):
        super().show_details()


class DeveloperIntern(Developer, Intern):
    def __init__(self, programming_languages, duration, **kwargs):
        super().__init__(programming_languages=programming_languages,
                         duration=duration,
                         **kwargs)

    def show_details(self):
        super().show_details()


# -----------------------------
# 7️⃣ MAIN PROGRAM WITH INPUT
# -----------------------------
if __name__ == "__main__":

    company_name = input("Enter Company Name After Acquisition: ")
    location = input("Enter Company Location: ")

    merged_company = CompanyAcquisition(company_name, location)

    n = int(input("\nEnter number of employees: "))

    for i in range(n):
        print(f"\nEnter details for Employee {i+1}")
        role = input("Role (Manager/HR/Developer/Intern/HRManager/DeveloperIntern): ")

        emp_id = input("Employee ID: ")
        emp_name = input("Employee Name: ")
        designation = input("Designation: ")
        joining_date = input("Joining Date: ")
        previous_company = input("Previous Company: ")

        common_data = {
            "emp_id": emp_id,
            "emp_name": emp_name,
            "designation": designation,
            "joining_date": joining_date,
            "previous_company": previous_company
        }

        if role.lower() == "manager":
            team_size = int(input("Team Size: "))
            emp = Manager(team_size=team_size, **common_data)

        elif role.lower() == "hr":
            policies = int(input("Policies Handled: "))
            emp = HR(policies_handled=policies, **common_data)

        elif role.lower() == "developer":
            langs = input("Programming Languages (comma separated): ").split(",")
            emp = Developer(programming_languages=[l.strip() for l in langs],
                            **common_data)

        elif role.lower() == "intern":
            duration = input("Internship Duration: ")
            emp = Intern(duration=duration, **common_data)

        elif role.lower() == "hrmanager":
            team_size = int(input("Team Size: "))
            policies = int(input("Policies Handled: "))
            emp = HRManager(team_size=team_size,
                            policies_handled=policies,
                            **common_data)

        elif role.lower() == "developerintern":
            langs = input("Programming Languages (comma separated): ").split(",")
            duration = input("Internship Duration: ")
            emp = DeveloperIntern(programming_languages=[l.strip() for l in langs],
                                  duration=duration,
                                  **common_data)

        else:
            print("Invalid role! Skipping...")
            continue

        merged_company.add_employee(emp)

    # Show Final Output
    merged_company.show_details()
