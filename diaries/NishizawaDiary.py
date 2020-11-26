from diaries.AbstractDiary import AbstractDiary


class NishizawaDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "めっちゃ疲れた"

    def get_author(self):
        return "nishizawa"