# ==========================================
# Base Class: Company
# ==========================================
class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    # Private Financial Report
    def __financial_report(self):
        return "Confidential Financial Report: Revenue = $5M"

    # Controlled access method
    def get_financial_report(self, role):
        if role in ["Manager", "HR", "ManagerHR"]:
            return self.__financial_report()
        else:
            return "Access Denied: Financial Report is Restricted"

    def add_employee(self, emp):
        self.employees.append(emp)

    def show_details(self):
        print(f"\nCompany Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Total Employees: {len(self.employees)}")


# ==========================================
# Base Class: Employee
# ==========================================
class Employee:
    def __init__(self, emp_id, emp_name, designation):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.designation = designation

    # Protected method
    def _policy_update(self):
        return "Company Policy Updated Successfully"

    def show_details(self):
        print(f"\nEmployee ID: {self.emp_id}")
        print(f"Name: {self.emp_name}")
        print(f"Designation: {self.designation}")


# ==========================================
# Multi-Level Inheritance
# ==========================================
class NewEmployee(Employee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company):
        super().__init__(emp_id, emp_name, designation)
        self.joining_date = joining_date
        self.previous_company = previous_company

    def show_details(self):
        super().show_details()
        print(f"Joining Date: {self.joining_date}")
        print(f"Previous Company: {self.previous_company}")


# ==========================================
# Role Classes
# ==========================================
class Manager(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, team_size):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.team_size = team_size

    def access_financial_report(self, company):
        print(company.get_financial_report("Manager"))

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")


class HR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, policies_handled):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.policies_handled = policies_handled

    def update_policy(self):
        print(self._policy_update())

    def access_financial_report(self, company):
        print(company.get_financial_report("HR"))

    def show_details(self):
        super().show_details()
        print(f"Policies Handled: {self.policies_handled}")


class Developer(NewEmployee):
    def access_financial_report(self, company):
        print(company.get_financial_report("Developer"))

    def show_details(self):
        super().show_details()
        print("Role: Developer")


class Intern(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company, duration):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.duration = duration

    def show_details(self):
        super().show_details()
        print(f"Internship Duration: {self.duration} months")


# ==========================================
# Multiple Inheritance
# ==========================================
class ManagerHR(NewEmployee):
    def __init__(self, emp_id, emp_name, designation,
                 joining_date, previous_company,
                 team_size, policies_handled):
        super().__init__(emp_id, emp_name, designation,
                         joining_date, previous_company)
        self.team_size = team_size
        self.policies_handled = policies_handled

    def access_financial_report(self, company):
        print(company.get_financial_report("ManagerHR"))

    def update_policy(self):
        print(self._policy_update())

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")
        print(f"Policies Handled: {self.policies_handled}")


class DeveloperIntern(Intern):
    pass


# ==========================================
# Hybrid Inheritance (Acquisition)
# ==========================================
class CompanyAcquisition(Company):
    def __init__(self, existing_company, acquired_company):
        merged_name = existing_company.name + " + " + acquired_company.name
        super().__init__(merged_name, existing_company.location)

        self.existing_company = existing_company
        self.acquired_company = acquired_company

        # Merge Employees
        self.employees = existing_company.employees + acquired_company.employees

    def show_details(self):
        print("\n========== COMPANY ACQUISITION ==========")
        print(f"Existing Company: {self.existing_company.name}")
        print(f"Acquired Company: {self.acquired_company.name}")
        print(f"Merged Company: {self.name}")
        print(f"Total Employees After Merger: {len(self.employees)}")

        print("\nEmployee Details:")
        for emp in self.employees:
            emp.show_details()
            print("----------------------------------")


# ==========================================
# MAIN PROGRAM (USER INPUT)
# ==========================================
if __name__ == "__main__":

    # Company Input
    name1 = input("Enter Existing Company Name: ")
    loc1 = input("Enter Existing Company Location: ")
    existing = Company(name1, loc1)

    name2 = input("Enter Acquired Company Name: ")
    loc2 = input("Enter Acquired Company Location: ")
    acquired = Company(name2, loc2)

    # Employee Input
    n = int(input("\nEnter total number of employees to add: "))

    for i in range(n):
        print("\nChoose Employee Type:")
        print("1. Manager")
        print("2. HR")
        print("3. Developer")
        print("4. Intern")
        print("5. ManagerHR")

        choice = int(input("Enter choice: "))

        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        joining = input("Enter Joining Date: ")
        prev = input("Enter Previous Company: ")

        if choice == 1:
            team_size = int(input("Enter Team Size: "))
            emp = Manager(emp_id, emp_name, designation,
                          joining, prev, team_size)

        elif choice == 2:
            policies = input("Enter Policies Handled: ")
            emp = HR(emp_id, emp_name, designation,
                     joining, prev, policies)

        elif choice == 3:
            emp = Developer(emp_id, emp_name, designation,
                            joining, prev)

        elif choice == 4:
            duration = int(input("Enter Internship Duration (months): "))
            emp = Intern(emp_id, emp_name, designation,
                         joining, prev, duration)

        elif choice == 5:
            team_size = int(input("Enter Team Size: "))
            policies = input("Enter Policies Handled: ")
            emp = ManagerHR(emp_id, emp_name, designation,
                            joining, prev, team_size, policies)
        else:
            print("Invalid Choice")
            continue

        # Add to existing company by default
        existing.add_employee(emp)

    # Perform Acquisition
    merged_company = CompanyAcquisition(existing, acquired)

    # Show Details
    merged_company.show_details()

    # Access Demonstration
    print("\n--- Access Demonstration ---")
    for emp in merged_company.employees:
        if hasattr(emp, "access_financial_report"):
            emp.access_financial_report(merged_company)
        if hasattr(emp, "update_policy"):
            emp.update_policy()

