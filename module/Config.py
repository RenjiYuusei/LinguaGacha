import dataclasses
import json
import os
import threading
from enum import StrEnum
from typing import Any
from typing import ClassVar
from typing import Self

from base.BaseLanguage import BaseLanguage
from base.LogManager import LogManager
from module.Localizer.Localizer import Localizer

@dataclasses.dataclass
class Config():

    class Theme(StrEnum):

        DARK = "DARK"
        LIGHT = "LIGHT"

    # Application
    theme: str = Theme.LIGHT
    app_language: BaseLanguage.Enum = BaseLanguage.Enum.ZH

    # PlatformPage
    activate_platform: int = 0
    platforms: list[dict[str, Any]] = None

    # AppSettingsPage
    expert_mode: bool = False
    proxy_url: str = ""
    proxy_enable: bool = False
    font_hinting: bool = True
    scale_factor: str = ""

    # BasicSettingsPage
    token_threshold: int = 384
    max_workers: int = 0
    rpm_threshold: int = 0
    request_timeout: int = 120
    max_round: int = 16

    # ExpertSettingsPage
    preceding_lines_threshold: int = 0
    enable_preceding_on_local: bool = False
    clean_ruby: bool = True
    deduplication_in_trans: bool = True
    deduplication_in_bilingual: bool = True
    write_translated_name_fields_to_file: bool = True
    result_checker_retry_count_threshold: bool = False

    # ProjectPage
    source_language: BaseLanguage.Enum = BaseLanguage.Enum.AUTO
    target_language: BaseLanguage.Enum = BaseLanguage.Enum.ZH
    input_folder: str = "./input"
    output_folder: str = "./output"
    output_folder_open_on_finish: bool = False
    traditional_chinese_enable: bool = False

    # GlossaryPage
    glossary_enable: bool = True
    glossary_data: list[Any] = dataclasses.field(default_factory = list)

    # TextPreservePage
    text_preserve_enable: bool = False
    text_preserve_data: list[Any] = dataclasses.field(default_factory = list)

    # PreTranslationReplacementPage
    pre_translation_replacement_enable: bool = True
    pre_translation_replacement_data: list[Any] = dataclasses.field(default_factory = list)

    # PostTranslationReplacementPage
    post_translation_replacement_enable: bool = True
    post_translation_replacement_data: list[Any] = dataclasses.field(default_factory = list)

    # CustomPromptZHPage
    custom_prompt_zh_enable: bool = False
    custom_prompt_zh_data: str = None

    # CustomPromptENPage
    custom_prompt_en_enable: bool = False
    custom_prompt_en_data: str = None

    # LaboratoryPage
    auto_glossary_enable: bool = False
    mtool_optimizer_enable: bool = False

    # 类属性
    CONFIG_PATH: ClassVar[str] = "./resource/config.json"
    CONFIG_LOCK: ClassVar[threading.Lock] = threading.Lock()

    def load(self, path: str = None) -> Self:
        if path is None:
            path = __class__.CONFIG_PATH

        with __class__.CONFIG_LOCK:
            try:
                os.makedirs(os.path.dirname(path), exist_ok = True)
                if os.path.isfile(path):
                    with open(path, "r", encoding = "utf-8-sig") as reader:
                        config: dict = json.load(reader)
                        for k, v in config.items():
                            if hasattr(self, k):
                                setattr(self, k, v)
            except Exception as e:
                LogManager.get().error(f"{Localizer.get().log_read_file_fail}", e)

        return self

    def save(self, path: str = None) -> Self:
        if path is None:
            path = __class__.CONFIG_PATH

        with __class__.CONFIG_LOCK:
            try:
                os.makedirs(os.path.dirname(path), exist_ok = True)
                with open(path, "w", encoding = "utf-8") as writer:
                    json.dump(dataclasses.asdict(self), writer, indent = 4, ensure_ascii = False)
            except Exception as e:
                LogManager.get().error(f"{Localizer.get().log_write_file_fail}", e)

        return self

    # 重置专家模式
    def reset_expert_settings(self) -> None:
        # ExpertSettingsPage
        self.preceding_lines_threshold: int = 0
        self.enable_preceding_on_local: bool = False
        self.clean_ruby: bool = True
        self.deduplication_in_trans: bool = True
        self.deduplication_in_bilingual: bool = True
        self.write_translated_name_fields_to_file: bool = True
        self.result_checker_retry_count_threshold: bool = False

        # TextPreservePage
        self.text_preserve_enable: bool = False
        self.text_preserve_data: list[Any] = []

    # 获取平台配置
    def get_platform(self, id: int) -> dict[str, Any]:
        item: dict[str, str | bool | int | float | list[str]] = None
        for item in self.platforms:
            if item.get("id", 0) == id:
                return item

    # 更新平台配置
    def set_platform(self, platform: dict[str, Any]) -> None:
        for i, item in enumerate(self.platforms):
            if item.get("id", 0) == platform.get("id", 0):
                self.platforms[i] = platform
                break