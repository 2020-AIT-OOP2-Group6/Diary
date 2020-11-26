from diaries.AbstractDiary import AbstractDiary


class Toyama_diary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "ゲームした"

    def get_author(self):
        return "Sample"
