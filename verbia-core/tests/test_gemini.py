import os

from langcodes import Language

from verbia_core.dictionary.gemini.dictionary import GeminiDictionary


def test_lookup_en():
    dictionary = GeminiDictionary()
    word = dictionary.lookup(
        word="go",
        word_language=Language.get("en"),
        native_language=Language.get("zh"),
    )
    assert word.word == "go"
    assert word.word_language == Language.get("en")
    assert word.native_language == Language.get("zh")
    assert word.source == "Gemini"
    assert word.lemma == "go"
    assert word.forms.past_tense == "went"
    assert word.forms.past_participle == "gone"
    assert word.forms.present_participle == "going"
    assert word.forms.third_person_singular == "goes"


def test_lookup_ja():
    dictionary = GeminiDictionary()
    word = dictionary.lookup(
        word="勉強",
        word_language=Language.get("ja"),
        native_language=Language.get("en"),
    )
    assert word.word == "勉強"
    assert word.word_language == Language.get("ja")
    assert word.native_language == Language.get("en")
    assert word.source == "Gemini"
    assert "べんきょう" in word.reading.hiragana
    assert "勉強する" in word.conjugation.present
    assert "勉強した" in word.conjugation.past
    assert "勉強します" in word.conjugation.polite
    assert "勉強しない" in word.conjugation.negative
    assert "勉強して" in word.conjugation.te_form
    assert "勉強できる" in word.conjugation.potential
