from dataclasses import dataclass

@dataclass
class Schedule_Item:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    totenrl: int
    capenrl: int
    instructor: str

    def print(self):
        print(
            f"{self.subject:<8}"
            f"{self.catalog:<10}"
            f"{self.section:<10}"
            f"{self.component:<11}"
            f"{self.session:<10}"
            f"{self.units:<7}"
            f"{self.totenrl:<10}"
            f"{self.capenrl:<10}"
            f"{self.instructor:<8}"
        
            )

    def get_key(self):
        return f"{self.subject}_{self.catalog}_{self.section}"