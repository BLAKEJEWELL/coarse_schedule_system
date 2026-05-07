from dataclasses import dataclass

@dataclass
class Schedule_Item:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

def print(self):
    print(
        f"{self.subject:<8}"
        f"{self.catalog:<8}"
        f"{self.section:<8}"
        f"{self.componetn:<8}"
        f"{self.session:<8}"
        f"{self.units:<8}"
        f"{self.totenrl:<8}"
        f"{self.capenrl:<8}"
        f"{self.instructor:<8}"
        
        )

def get_key(self):
    return f"{self.subject}_{self.catalog}_{self.section}"