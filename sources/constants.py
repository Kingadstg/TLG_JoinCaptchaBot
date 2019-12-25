# -*- coding: utf-8 -*-

'''
Script:
    constants.py
Description:
    Constants values for join_captcha_bot.py.
Author:
    Jose Rios Rubio
Creation date:
    09/09/2018
Last modified date:
    11/12/2019
Version:
    1.6.6
'''

####################################################################################################

### Imported modules ###

from os import path

####################################################################################################

### Constants ###

# Actual constants.py full path directory name
SCRIPT_PATH = path.dirname(path.realpath(__file__))


# General Bots Parameters
CONST = {

    # Bot Token (get it from @BotFather)
    "TOKEN" : "1038324333:AAHfr6iwolaM-TtjU_oCcm3gx6Ss6jdqA9Y",

    # Languages texts files directory path
    "LANG_DIR" : SCRIPT_PATH + "/language",

    # Chats directory path
    "CHATS_DIR" : SCRIPT_PATH + "/data/chats",

    # Directory where create/generate temporary captchas
    "CAPTCHAS_DIR" : SCRIPT_PATH + "/data/captchas",

    # Chat configurations JSON files
    "F_CONF" : "configs.json",

    # Initial chat title at Bot start
    "INIT_TITLE" : "Unknown Chat",

    # Initial chat link at Bot start
    "INIT_LINK" : "Unknown",

    # Initial language at Bot start
    "INIT_LANG" : "EN",

    # Initial enable/disable status at Bot start
    "INIT_ENABLE" : True,

    # Initial captcha solve time (in minutes)
    "INIT_CAPTCHA_TIME_MIN" : 5,

    # Initial captcha difficult level
    "INIT_CAPTCHA_DIFFICULTY_LEVEL" : 2,

    # Initial captcha characters mode (nums, hex or ascci)
    "INIT_CAPTCHA_CHARS_MODE" : "nums",

    # Default time (in mins) to remove self-destruct sent messages from the Bot
    "T_DEL_MSG" : 5,

    # Auto-remove custom welcome message timeout
    "T_DEL_WELCOME_MSG" : 5,

    # Custom Welcome message max length
    "MAX_WELCOME_MSG_LENGTH" : 3968,

    # IANA Top-Level-Domain List (https://data.iana.org/TLD/tlds-alpha-by-domain.txt)
    "F_TLDS" : "tlds-alpha-by-domain.txt",

    # Regular expression to detect URLs in a string based in TLD domains
    "REGEX_URLS" : r"((?<=[^a-zA-Z0-9])*(?:https\:\/\/|[a-zA-Z0-9]{{1,}}\.{{1}}|\b)" \
        r"(?:\w{{1,}}\.{{1}}){{1,5}}(?:{})\b/?(?!@))",

    # String of supported languages shows in "/commands" command
    "SUPPORTED_LANGS" : \
        "en (English) - fr (French / Francais) - de (German / Deutch) - " \
        "it (Italian / Italiano) - id (Indonesian / Indonesia) - es (Spanish / Español) - " \
        "ca (Catalan / Català) - gl (Galician / Galego) - eu (Basque / Euskal) - " \
        "pt_br (Portuguese-Brazil / Português-Brasil) - zh_cn (Chinese-Simplified / 中文)",

    # List string of supported languages commands shows in invalid language set
    "SUPPORTED_LANGS_CMDS" : "\nEnglish / English\n/language en\n" \
        "\nFrench / Francais\n/language fr\n\nGerman / Deutch\n/language de\n" \
        "\nItalian / Italiano\n/language it\n\nIndonesian / Indonesia\n/language id\n" \
        "\nSpanish / Español\n/language es\n\nCatalan / Català\n/language ca\n" \
        "\nBasque / Euskal\n/language eu\n\nGalician / Galego\n/language gl\n" \
        "\nPortuguese-Brazil / Português-Brasil\n/language pt_br\n" \
        "\nChinese-Simplified / 中文\n/language zh_cn",

    # Bot developer
    "DEVELOPER" : "@Leaf_Ninja",

    # Bot code repository
    "REPOSITORY" : "https://github.com/J-Rios/TLG_JoinCaptchaBot",

    # Developer Paypal address
    "DEV_PAYPAL" : "https://www.paypal.me/skumar243",

    # Developer Bitcoin address
    "DEV_BTC" : "3EpNqL7HR3VBZrNQW54XTJ7x8djK7vNygf",

    # Bot version
    "VERSION" : "1.6.6 (11/12/2019)"
}


# Supported languages list
TEXT = {
    "EN" : None, # English
    "DE" : None, # German
    "FR" : None, # French
    "ID" : None, # Indonesian
    "IT" : None, # Italian
    "ES" : None, # Spanish
    "CA" : None, # Catalan
    "GL" : None, # Galician
    "EU" : None, # Basque
    "PT_BR" : None, # Portuguese (Brasil)
    #"FA" : None, # Persian (The json file is broken or json parser library doesn't support it)
    "ZH_CN" : None # Chinese (Mainland)
}
