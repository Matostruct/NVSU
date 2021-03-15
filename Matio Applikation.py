import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1
from ibm_watson import ToneAnalyzerV3

authenticator = IAMAuthenticator(
    'YqreNfgTltnFZc7hPkpy24VjZwXmq_xx9Jme73R_6dpa')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/b1f37d3c-7774-421e-844f-9a3f1c189369')

print("Eingabe:")
toTranslate = input()
print("Sprache von-zu:")
langFromTo = input()
translation = language_translator.translate(
    text=toTranslate,
    model_id=langFromTo).get_result()
print(json.dumps(translation, ensure_ascii=False))

langToSpeech = langFromTo.split('-')[1]

authenticator = IAMAuthenticator(
    '3htRynxsNzqk2I82xV2pYHaXLG06yYSTur8ZpEo6V4Ye')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(
    'https://api.eu-de.text-to-speech.watson.cloud.ibm.com/instances/c7f28685-9c45-4c5b-8d20-c4837274e85a')

if langToSpeech == "ar":
    langToSpeech = "ar-MS_OmarVoice"
elif langToSpeech == "de":
    langToSpeech = "de-DE_DieterVoice"
elif langToSpeech == "en":
    langToSpeech = "en-GB_JamesV3Voice"
elif langToSpeech == "es":
    langToSpeech = "es-ES_EnriqueVoice"
elif langToSpeech == "fr":
    langToSpeech = "fr-FR_NicolasV3Voice"
elif langToSpeech == "it":
    langToSpeech = "it-IT_FrancescaV3Voice"
elif langToSpeech == "ja":
    langToSpeech = "ja-JP_EmiV3Voice"
elif langToSpeech == "ko":
    langToSpeech = "ko-KR_SiWooVoice"
elif langToSpeech == "pt":
    langToSpeech = "pt-BR_IsabellaV3Voice"
elif langToSpeech == "zh":
    langToSpeech = "zh-CN_ZhangJingVoice"

text = translation.__str__().split('{')[2].split('}')[0].split(':')[
    1].replace('\'', '').strip()
print(text)
with open('translate.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text,
            voice=langToSpeech,
            accept='audio/wav'
        ).get_result().content)

authenticator = IAMAuthenticator(
    'fAzrt6CXh8aZN2KA8zEMmj8wanU-J73ATmvE9jO-y7hp')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url(
    'https://api.eu-de.tone-analyzer.watson.cloud.ibm.com/instances/2588bf17-6b9a-4034-b2da-5b2a0345f65c')

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()
print(json.dumps(tone_analysis, indent=2))
