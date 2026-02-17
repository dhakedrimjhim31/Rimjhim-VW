# Import ABC and abstractmethod to create abstract base classes
from abc import ABC, abstractmethod


# --------------------------------------------------------
# Abstract Base Class (Template Pattern Implementation)
# --------------------------------------------------------
class Report(ABC):
    """
    This is the base abstract class.
    It defines the TEMPLATE METHOD that controls
    the sequence of report generation.
    """

    # Template Method
    # This method defines the fixed sequence of steps.
    # Subclasses cannot change this order.
    def generate_report(self):
        self.parse()                  # Step 1: Parse file
        self.validate()               # Step 2: Validate data
        self.additional_validation()  # Step 3: Optional step (hook method)
        self.save()                   # Step 4: Save file
        print("Report generation completed.\n")

    # Abstract method: Must be implemented by subclasses
    @abstractmethod
    def parse(self):
        pass

    # Abstract method: Must be implemented by subclasses
    @abstractmethod
    def validate(self):
        pass

    # Abstract method: Must be implemented by subclasses
    @abstractmethod
    def save(self):
        pass

    # Hook method (default implementation)
    # Standard reports will use this empty method.
    # Special reports will override this.
    def additional_validation(self):
        pass


# --------------------------------------
# STANDARD REPORTS
# Sequence: Parse → Validate → Save
# --------------------------------------
class StandardReport(Report):
    """
    This class represents standard reports.
    It inherits from Report.
    No extra validation is required.
    """

    # Override hook method but keep it empty
    # This ensures no revalidation step is executed.
    def additional_validation(self):
        pass


# Concrete class for PDF report
class PDFReport(StandardReport):

    # Parsing logic specific to PDF
    def parse(self):
        print("Parsing PDF file...")

    # Validation logic specific to PDF
    def validate(self):
        print("Validating PDF data...")

    # Save logic specific to PDF
    def save(self):
        print("Saving PDF report...")


# Concrete class for DOCX report
class DOCXReport(StandardReport):

    def parse(self):
        print("Parsing DOCX file...")

    def validate(self):
        print("Validating DOCX data...")

    def save(self):
        print("Saving DOCX report...")


# Concrete class for TXT report
class TXTReport(StandardReport):

    def parse(self):
        print("Parsing TXT file...")

    def validate(self):
        print("Validating TXT data...")

    def save(self):
        print("Saving TXT report...")


# --------------------------------------------------
# SPECIAL REPORTS
# Sequence: Parse → Validate → Revalidate → Save
# --------------------------------------------------
class SpecialReport(Report):
    """
    Special reports require an additional revalidation step.
    """

    # Override hook method
    # This ensures revalidate() is called between validate and save.
    def additional_validation(self):
        self.revalidate()

    # Force subclasses to implement revalidation
    @abstractmethod
    def revalidate(self):
        pass


# Concrete class for CSV report
class CSVReport(SpecialReport):

    def parse(self):
        print("Parsing CSV file...")

    def validate(self):
        print("Validating CSV data...")

    # Additional revalidation step
    def revalidate(self):
        print("Revalidating CSV data for consistency...")

    def save(self):
        print("Saving CSV report...")


# Concrete class for JSON report
class JSONReport(SpecialReport):

    def parse(self):
        print("Parsing JSON file...")

    def validate(self):
        print("Validating JSON structure...")

    # Additional revalidation step
    def revalidate(self):
        print("Revalidating JSON schema...")

    def save(self):
        print("Saving JSON report...")


# ---------------------
# CLIENT FUNCTION
# ---------------------
def client_code(report: Report):
    """
    This function demonstrates polymorphism.
    It accepts any object of type Report.
    """
    report.generate_report()


# -------------------------------------
# MAIN PROGRAM (User Interaction)
# -------------------------------------
if __name__ == "__main__":

    # Display available options
    print("Choose Report Type:")
    print("1. PDF")
    print("2. DOCX")
    print("3. TXT")
    print("4. CSV")
    print("5. JSON")

    # Take user input
    choice = input("Enter your choice: ")

    # Dictionary mapping user choice to corresponding class object
    report_map = {
        "1": PDFReport(),
        "2": DOCXReport(),
        "3": TXTReport(),
        "4": CSVReport(),
        "5": JSONReport()
    }

    # Get selected report object
    selected_report = report_map.get(choice)

    # Check if input is valid
    if selected_report:
        client_code(selected_report)  # Polymorphic call
    else:
        print("Invalid choice!")
