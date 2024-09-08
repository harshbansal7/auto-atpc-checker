# Model File for Placement Data

class PlacementData: 
    def __init__(self, company_name, job_profile, ctc, date_of_visit, eligibility, selection_process, remarks):
        self.company_name = company_name
        self.job_profile = job_profile
        self.ctc = ctc
        self.date_of_visit = date_of_visit
        self.eligibility = eligibility
        self.selection_process = selection_process
        self.remarks = remarks

    def __str__(self):
        return f"Company Name: {self.company_name}\nJob Profile: {self.job_profile}\nCTC: {self.ctc}\nDate of Visit: {self.date_of_visit}\nEligibility: {self.eligibility}\nSelection Process: {self.selection_process}\nRemarks: {self.remarks}\n"

    def to_dict(self):
        return {
            "Company Name": self.company_name,
            "Job Profile": self.job_profile,
            "CTC": self.ctc,
            "Date of Visit": self.date_of_visit,
            "Eligibility": self.eligibility,
            "Selection Process": self.selection_process,
            "Remarks": self.remarks
        }

    def from_dict(self, data):
        self.company_name = data["Company Name"]
        self.job_profile = data["Job Profile"]
        self.ctc = data["CTC"]
        self.date_of_visit = data["Date of Visit"]
        self.eligibility = data["Eligibility"]
        self.selection_process = data["Selection Process"]
        self.remarks = data["Remarks"]
        return self