def translate(words, lang):
    from google.cloud import translate
    project_id = "traffic-sign-detector-319618"
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/projects/a393710e-7e62-47f1-abc5-305c9c32e179/translation/key.json"


    assert project_id
    parent = f"projects/{project_id}"
    client = translate.TranslationServiceClient()

    response = client.get_supported_languages(parent=parent, display_language_code="en")
    languages = response.languages

    #print(f" Languages: {len(languages)} ".center(60, "-"))
    #for language in languages:
        #print(f"{language.language_code}\t{language.display_name}")


    sample_text = words
    target_language_code = lang

    response = client.translate_text (contents=[sample_text], target_language_code=target_language_code, parent=parent)

    for translation in response.translations:
        return translation.translated_text