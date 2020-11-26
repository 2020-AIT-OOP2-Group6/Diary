from diaries.DiarySample import DiarySample
from diaries.BabaDiary import BabaDiary
from diaries.FugaDiaryNew import FugaDiaryNew
from diaries.NishizawaDiary import NishizawaDiary

diaries = [DiarySample(), BabaDiary(), NishizawaDiary(), FugaDiaryNew()]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()