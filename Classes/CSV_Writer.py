import csv
import time


# NOTE: MAY TAKE REFRESH OR 2 PROGRAM STARTS FOR CSV FILE TO SHOW
class CSV_Writer:
    def __init__(self):
        self.fieldnames = ['move', 'wFrom', 'wTo', 'bFrom', 'bTo']
        self.currentMove = 1
        self.filename = "chessMoves"
        self.init_Write()

    # I struggled on how to make this OOP-Like

    # This is appalling code but again, I did really struggle on how to make the with statement integrated into OOP

    # Create file in write mode with headers
    def init_Write(self):
        datetime_str = time.strftime("%Y%m%d-%H%M%S")
        self.filename = f"{self.filename}{datetime_str}.csv"

        try:
            with open(self.filename, 'w') as new_file:
                writer = csv.DictWriter(new_file, fieldnames=self.fieldnames, delimiter=',')
                writer.writeheader()
        except Exception as e:
            print(f"{e} : CSV writer has failed, most likely write permissions")

    # row write function takes a pre-headered dict and writes to the corresponding headers (Keys) associated to the
    # column
    def row_write(self, _row2write: dict[str, str]):
        # Add instance current move
        _row2write['move'] = str(self.currentMove)

        try:
            with open(self.filename, 'a') as existing_file:
                writer = csv.DictWriter(existing_file, fieldnames=self.fieldnames, delimiter=',')
                writer.writerow(_row2write)
                # Add Optional Kill statement of each team?
                self.currentMove += 1
        except Exception as e:
            print(f"{e} : CSV writer has failed, most likely write permissions")
