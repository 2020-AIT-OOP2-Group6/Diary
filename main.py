from diaries.DiarySample import DiarySample
from diaries.Toyama_diary import Toyama_diary
from diaries.Iwama_diary import Iwama_diary

diaries = [DiarySample(),Toyama_diary(), Iwama_diary() ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()