from diaries.AbstractDiary import AbstractDiary


class BabaDiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "何をするのかわからず焦ってます"

    def get_author(self):
        return "Babachan"