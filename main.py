from diaries.DiarySample import DiarySample
from diaries.BabaDiary import BabaDiary
from diaries.FugaDiaryNew import FugaDiaryNew

diaries = [DiarySample(), BabaDiary(), FugaDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()