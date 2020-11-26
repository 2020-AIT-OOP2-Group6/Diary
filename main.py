from diaries.DiarySample import DiarySample
from diaries.Toyama_diary import Toyama_diary
from diaries.Iwama_diary import Iwama_diary
from diaries.BabaDiary import BabaDiary
from diaries.DiaryFugaNew import FugaDiaryNew
from diaries.NishizawaDiary import NishizawaDiary


diaries = [DiarySample(), BabaDiary(), FugaDiaryNew(),
           Toyama_diary(), NishizawaDiary(), Iwama_diary()]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
