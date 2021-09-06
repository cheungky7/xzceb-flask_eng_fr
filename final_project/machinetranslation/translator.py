"""Translator module."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    '''Takes in English, returns French'''
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
   # print(translation)
   # print((translation.get('translations'))[0].get('translation'))
   # print(tran_obj)
    french_text=(translation.get('translations'))[0].get('translation')

    return french_text

def frenchToEnglish(french_text):
    '''Takes in French, returns English'''
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    # print(translation)
    # print((translation.get('translations'))[0].get('translation'))
    english_text=(translation.get('translations'))[0].get('translation')
    # print(tran_obj)
    return english_text
