from diaries.DiarySample import DiarySample
from diaries.FugaDiaryNew import FugaDiaryNew

diaries = [DiarySample(), FugaDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()