import time
from abc import ABC, abstractmethod
from contextlib import contextmanager


# --------------------------------------------
# DECORATORS (Logging + Timing + Validation)
# --------------------------------------------

# Decorator for logging
def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished '{func.__name__}'.\n")
        return result
    return wrapper


# Decorator for measuring execution time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] Execution took {end - start:.4f} seconds.")
        return result
    return wrapper


# Decorator to validate before saving
def validate_before_save(func):
    def wrapper(self, *args, **kwargs):
        if not self.is_valid:
            raise ValueError("Report data is not valid. Cannot save.")
        return func(self, *args, **kwargs)
    return wrapper


# ----------------------------------------
# CONTEXT MANAGER (Safe File Handling)
# ----------------------------------------

@contextmanager
def managed_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()
        print("[RESOURCE] File closed safely.")


# ------------------------
# ABSTRACT BASE CLASS
# ------------------------

class Report(ABC):
    """
    Abstract base class for all reports.
    """

    def __init__(self, filename):
        self.filename = filename
        self.is_valid = False

    @abstractmethod
    def generate_data(self):
        """
        Generator method to produce report data lazily.
        Must be implemented by subclasses.
        """
        pass

    def validate(self):
        """
        Basic validation logic.
        """
        print("Validating report data...")
        self.is_valid = True

    @log_operation
    @measure_time
    def generate_report(self):
        """
        Template method controlling report generation.
        """
        self.validate()

        with managed_file(self.filename, "w") as file:
            for chunk in self.generate_data():  # Generator usage
                file.write(chunk + "\n")

        self.save()

    @validate_before_save
    def save(self):
        print(f"Report saved successfully as '{self.filename}'.")


# --------------------------------------
# TEXT REPORT (Line-by-line generator)
# --------------------------------------

class TextReport(Report):

    def generate_data(self):
        """
        Yields lines lazily.
        Simulates large file generation.
        """
        for i in range(1, 6):
            yield f"Text Report Line {i}"


# -------------------------------------------
# STRUCTURED REPORT (Chunk-based generator)
# -------------------------------------------

class StructuredReport(Report):

    def generate_data(self):
        """
        Yields structured data lazily.
        """
        data = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"},
        ]

        for record in data:
            yield str(record)


# ----------------
# CLIENT CODE
# ----------------

def client_request(report_type, filename):

    report_classes = {
        "text": TextReport,
        "structured": StructuredReport
    }

    report_class = report_classes.get(report_type.lower())

    if not report_class:
        print("Invalid report type selected.")
        return

    report = report_class(filename)
    report.generate_report()


# --------------
# MAIN PROGRAM
# --------------

if __name__ == "__main__":

    print("Available Reports:")
    print("1. Text Report")
    print("2. Structured Report")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        client_request("text", "text_report.txt")
    elif choice == "2":
        client_request("structured", "structured_report.txt")
    else:
        print("Invalid selection.")
