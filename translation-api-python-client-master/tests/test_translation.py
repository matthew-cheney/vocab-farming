#!/usr/bin/env python
# coding: utf-8

import os
import unittest
import time

import systran_translation_api
import systran_translation_api.configuration

class TranslationApiTests(unittest.TestCase):
    def setUp(self):
        api_key_file = os.path.join(os.path.dirname(__file__), "../", "api_key.txt")
        systran_translation_api.configuration.load_api_key(api_key_file)
        self.api_client = systran_translation_api.ApiClient()
        self.translation_api = systran_translation_api.TranslationApi(self.api_client)

    def test_translation_supported_languages_get(self):
        result = self.translation_api.translation_supported_languages_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_supported_languages_get_with_source_and_target(self):
        source = ["en"]
        target = ["fr"]
        result = self.translation_api.translation_supported_languages_get(source=source, target=target)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_profile_get(self):
        result = self.translation_api.translation_profile_get()
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_profile_get_with_source_and_target(self):
        source = "en"
        target = "fr"
        result = self.translation_api.translation_profile_get(source=source, target=target)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get(self):
        source = "en"
        target = "fr"
        input = ["This is a test"]
        result = self.translation_api.translation_text_translate_get(source=source, target=target, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr(self):
        target = "fr"
        input = ["This is a test"]
        result = self.translation_api.translation_text_translate_get(target=target, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_with_several_inputs(self):
        target = "fr"
        input = ["This is a test", "I like playing football"]
        result = self.translation_api.translation_text_translate_get(target=target, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_with_several_inputs_and_with_source(self):
        target = "fr"
        input = ["This is a test", "I like playing football"]
        with_source = True
        result = self.translation_api.translation_text_translate_get(target=target, input=input, with_source=with_source)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_html(self):
        target = "fr"
        input = ["<html>this is <b>black</b> dog"]
        result = self.translation_api.translation_text_translate_get(target=target, input=input)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_html_with_format(self):
        target = "fr"
        input = ["<html>this is <b>black</b> dog"]
        format = "text/html"
        result = self.translation_api.translation_text_translate_get(target=target, input=input, format=format)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_html_with_format_source_annotations(self):
        target = "fr"
        input = ["<html>this is <b>black</b> dog"]
        format = "text/html"
        with_source = True
        with_annotations = True
        result = self.translation_api.translation_text_translate_get(target=target, input=input, format=format, with_source=with_source, with_annotations=with_annotations)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_get_auto_fr_several_inputs_html_with_format_source_annotations(self):
        target = "fr"
        input = ["<html>this is <b>black</b> dog", "<html>this is <b>white</b> cat"]
        format = "text/html"
        with_source = True
        with_annotations = True
        result = self.translation_api.translation_text_translate_get(target=target, input=input, format=format, with_source=with_source, with_annotations=with_annotations)
        self.assertIsNotNone(result)
        print result.__repr__()

    def test_translation_translate_file_get_auto_fr_with_source_annotations(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "test.html")
        target = "fr"
        with_source = True
        with_annotations = True
        result = self.translation_api.translation_file_translate_get(target=target, input=input_file, with_source=with_source, with_annotations=with_annotations)
        self.assertIsNotNone(result)
        print "detectedLanguage : ", result["detected_language"]["detectedLanguage"]
        print "detectedLanguageConfidence : ", result["detected_language"]["detectedLanguageConfidence"]
        source_file = os.path.join(os.path.dirname(__file__), "", "translation_source.html")
        src_fo = open(source_file, "wb")
        src_fo.write(result["source"])
        src_fo.close()
        print "Source file saved in : ", source_file
        output_file = os.path.join(os.path.dirname(__file__), "", "translation_output.html")
        out_fo = open(output_file, "wb")
        out_fo.write(result["output"])
        out_fo.close()
        print "Translated file saved in : ", output_file

    # translate file async
    def get_status(self, request_id):
        result = self.translation_api.translation_file_status_get(request_id=request_id)
        self.assertIsNotNone(result)
        print "Get translation status : ", result.__repr__()
        if result.status == "finished":
            return 1
        elif result.status == "error":
            return -1
        else:
            return 0

    def get_translation_translate_file_async_auto_fr_with_source_annotations(self, request_id):
        result = self.translation_api.translation_file_result_get(request_id=request_id)
        self.assertIsNotNone(result)
        print "Get translation result : ", result.__repr__()

        if "detected_language" in result:
            print "detectedLanguage : ", result["detected_language"]["detectedLanguage"]
            print "detectedLanguageConfidence : ", result["detected_language"]["detectedLanguageConfidence"]

        if "source" in result:
            source_file = os.path.join(os.path.dirname(__file__), "", "translation_source.html")
            src_fo = open(source_file, "wb")
            src_fo.write(result["source"])
            src_fo.close()
            print "Source file saved in : ", source_file

        if "output" in result:
            output_file = os.path.join(os.path.dirname(__file__), "", "translation_output.html")
            out_fo = open(output_file, "wb")
            out_fo.write(result["output"])
            out_fo.close()
            print "Translated file saved in : ", output_file

    def test_translation_translate_file_get_async_auto_fr_with_source_annotations(self):
        input_file = os.path.join(os.path.dirname(__file__), "", "test.html")
        target = "fr"
        async = True
        with_source = True
        with_annotations = True
        result = self.translation_api.translation_file_translate_get(target=target, input=input_file, async=async, with_source=with_source, with_annotations=with_annotations)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.request_id)
        print result.__repr__()
        print result.request_id

        finished = 0
        while finished == 0:
            time.sleep(5)
            finished = self.get_status(request_id=result.request_id)

        self.assertEqual(finished, 1)
        self.get_translation_translate_file_async_auto_fr_with_source_annotations(result.request_id)

    def test_translation_batch_complete(self):
        # create a batch to do some translations
        new_batch = self.translation_api.translation_file_batch_create_get()
        self.assertIsNotNone(new_batch)
        print "Create new batch response : ", new_batch.__repr__()
        self.assertIsNotNone(new_batch.batch_id)

        # get status for new created batch
        batch_id = new_batch.batch_id
        batch_status = self.translation_api.translation_file_batch_status_get(batch_id=batch_id)
        print "Batch status response : ", batch_status.__repr__()

        # add a translation to the batch
        input_file = os.path.join(os.path.dirname(__file__), "", "test.html")
        source = "en"
        target = "fr"
        async = True
        with_source = True
        with_annotations = True
        result = self.translation_api.translation_file_translate_get(source=source, target=target, input=input_file, async=async, with_source=with_source, with_annotations=with_annotations, batch_id=batch_id)
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.request_id)
        print result.__repr__()
        print result.request_id

        # get status after adding a translation request
        batch_status = self.translation_api.translation_file_batch_status_get(batch_id=batch_id)
        print "Batch status with a translation request : ", batch_status.__repr__()

        finished = 0
        while finished == 0:
            time.sleep(5)
            finished = self.get_status(request_id=result.request_id)

        self.assertEqual(finished, 1)
        self.get_translation_translate_file_async_auto_fr_with_source_annotations(result.request_id)

        # close the batch after getting result of translation
        batch_close = self.translation_api.translation_file_batch_close_get(batch_id=batch_id)
        print "Close the batch after getting translation result : ", batch_close.__repr__()

if __name__ == '__main__':
    unittest.main()