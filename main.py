from diaries.DiarySample import DiarySample
from diaries.BabaDiary import BabaDiary

diaries = [DiarySample(), BabaDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()