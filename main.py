from diaries.DiarySample import DiarySample
from diaries.NishizawaDiary import NishizawaDiary
diaries = [
    DiarySample(), 
    NishizawaDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()