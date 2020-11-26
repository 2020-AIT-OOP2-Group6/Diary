from diaries.DiarySample import DiarySample
from diaries.BabaDiary import BabaDiary
from diaries.DiaryFugaNew import FugaDiaryNew
from diaries.Toyama_diary import Toyama_diary

diaries = [DiarySample(), BabaDiary(), FugaDiaryNew(), Toyama_diary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
