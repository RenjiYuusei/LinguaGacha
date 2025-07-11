from base.BaseLanguage import BaseLanguage
from module.Localizer.LocalizerZH import LocalizerZH
from module.Localizer.LocalizerEN import LocalizerEN
from module.Localizer.LocalizerVI import LocalizerVI

class Localizer():

    APP_LANGUAGE: BaseLanguage.Enum = BaseLanguage.Enum.ZH

    @classmethod
    def get(cls) -> LocalizerZH | LocalizerEN | LocalizerVI:
        if cls.APP_LANGUAGE == BaseLanguage.Enum.EN:
            return LocalizerEN
        elif cls.APP_LANGUAGE == BaseLanguage.Enum.VI:
            return LocalizerVI
        else:
            return LocalizerZH

    @classmethod
    def get_app_language(cls) -> BaseLanguage.Enum:
        return cls.APP_LANGUAGE

    @classmethod
    def set_app_language(cls, app_language: BaseLanguage.Enum) -> None:
        cls.APP_LANGUAGE = app_language