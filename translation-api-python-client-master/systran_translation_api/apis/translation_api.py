#!/usr/bin/env python
# coding: utf-8

"""
Copyright 2015 SYSTRAN Software, Inc. All rights reserved.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from .. import configuration
from ..api_client import ApiClient

class TranslationApi(object):

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            if not configuration.api_client:
                configuration.api_client = ApiClient('https://api-platform.systran.net')
            self.api_client = configuration.api_client
    
    
    def translation_file_batch_cancel_get(self, batch_id, **kwargs):
        """
        Batch Cancel
        Cancel a translation batch\n

        :param str batch_id: Batch Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: BatchCancel
        """
        
        # verify the required parameter 'batch_id' is set
        if batch_id is None:
            raise ValueError("Missing the required parameter `batch_id` when calling `translation_file_batch_cancel_get`")
        
        all_params = ['batch_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_batch_cancel_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/batch/cancel'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'batch_id' in params:
            query_params['batchId'] = params['batch_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='BatchCancel', auth_settings=auth_settings)
        
        return response
        
    def translation_file_batch_close_get(self, batch_id, **kwargs):
        """
        Batch Close
        Close a translation batch\n

        :param str batch_id: Batch Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: BatchClose
        """
        
        # verify the required parameter 'batch_id' is set
        if batch_id is None:
            raise ValueError("Missing the required parameter `batch_id` when calling `translation_file_batch_close_get`")
        
        all_params = ['batch_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_batch_close_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/batch/close'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'batch_id' in params:
            query_params['batchId'] = params['batch_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='BatchClose', auth_settings=auth_settings)
        
        return response
        
    def translation_file_batch_create_get(self, **kwargs):
        """
        Batch Create
        Create a new translation batch\n

        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: BatchCreate
        """
        
        all_params = ['callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_batch_create_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/batch/create'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='BatchCreate', auth_settings=auth_settings)
        
        return response
        
    def translation_file_batch_status_get(self, batch_id, **kwargs):
        """
        Batch Status
        Get the status of a translation batch\n

        :param str batch_id: Batch Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: BatchStatus
        """
        
        # verify the required parameter 'batch_id' is set
        if batch_id is None:
            raise ValueError("Missing the required parameter `batch_id` when calling `translation_file_batch_status_get`")
        
        all_params = ['batch_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_batch_status_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/batch/status'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'batch_id' in params:
            query_params['batchId'] = params['batch_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='BatchStatus', auth_settings=auth_settings)
        
        return response
        
    def translation_file_cancel_get(self, request_id, **kwargs):
        """
        Translate Cancel
        Cancel an asynchronous translation request\n

        :param str request_id: Request Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: TranslationCancel
        """
        
        # verify the required parameter 'request_id' is set
        if request_id is None:
            raise ValueError("Missing the required parameter `request_id` when calling `translation_file_cancel_get`")
        
        all_params = ['request_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_cancel_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/cancel'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'request_id' in params:
            query_params['requestId'] = params['request_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='TranslationCancel', auth_settings=auth_settings)
        
        return response
        
    def translation_file_result_get(self, request_id, **kwargs):
        """
        Translate Result
        Get the result of an asynchronous translation request\n\nDepending on the initial request, the response can have multiple formats:\n  * The **translated document**, directly, if `source` parameters was not `auto` and `withSource` was not true\n  * A `multipart/mixed` document with the following parts:\n\n    1. **Detected language**, if request was done with `auto` source language\n\n      * Header:\n\n        `part-name: detectedLanguage`\n\n      * Body: JSON document\n        ```\n        {\n          detectedLanguage: \"string\"\n          detectedLanguageConfidence : number\n        }\n        ```\n\n    2. **Source document**, if request was done with `withSource`:\n\n      * Header: `part-name: source`\n      * Body: Source document\n\n    3. **Translated document**\n\n      * Header: `part-name: output`\n\n      * Body: Translated document\n\nAn error can occur in the following cases:\n* Invalid request ID\n* No result available (see request status for more information)\n* Unable to retrieve the result\n* ...\n

        :param str request_id: Request Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: TranslationFileResponse
        """
        
        # verify the required parameter 'request_id' is set
        if request_id is None:
            raise ValueError("Missing the required parameter `request_id` when calling `translation_file_result_get`")
        
        all_params = ['request_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_result_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/result'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'request_id' in params:
            query_params['requestId'] = params['request_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'multipart/mixed', '*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='TranslationFileResponse', auth_settings=auth_settings)
        
        return response
        
    def translation_file_status_get(self, request_id, **kwargs):
        """
        Translate Status
        Get the status of an asynchronous translation request\n\nThe translation result is available when the value of the status field is `finished`.\n\nThe translation request is unsuccessful when the value of the status field is `error`.\n

        :param str request_id: Request Identifier\n (required)
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: TranslationStatus
        """
        
        # verify the required parameter 'request_id' is set
        if request_id is None:
            raise ValueError("Missing the required parameter `request_id` when calling `translation_file_status_get`")
        
        all_params = ['request_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_status_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/status'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'request_id' in params:
            query_params['requestId'] = params['request_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='TranslationStatus', auth_settings=auth_settings)
        
        return response
        
    def translation_file_translate_get(self, input, target, **kwargs):
        """
        Translate File
        Translate a file from source language to target language\n\n\n* In asynchronous mode (async=true), the response will be a JSON containing a request identifier. This identifier can then be used to poll the request status and its result when completed.\n\n  ```\n  {\n     \"requestId\": \"54a3d860e62ea467b136eddb\" /* Request identifier to use to get the status,\n                                                the result of the request and to cancel it */\n     \"error\": {\n       \"message\": \"\" /* Error at request level */\n       \"info\": {}\n     }\n  }\n  ```\n\n* In synchronous mode, the response will be either:\n\n  * The **translated document**, directly, if `source` parameters was not `auto` and `withSource` was not true\n  * A `multipart/mixed` document with the following parts:\n\n    1. **Detected language**, if request was done with `auto` source language\n\n      * Header:\n\n        `part-name: detectedLanguage`\n\n      * Body: JSON document\n        ```\n        {\n          detectedLanguage: \"string\"\n          detectedLanguageConfidence : number\n        }\n        ```\n\n    2. **Source document**, if request was done with `withSource`:\n\n      * Header: `part-name: source`\n      * Body: Source document\n\n    3. **Translated document**\n\n      * Header: `part-name: output`\n\n      * Body: Translated document\n

        :param File input: Input file\n (required)
        :param str source: Source language code ([details](#description_langage_code_values)) or `auto`.\n\nWhen the value is set to `auto`, the language will be automatically detected, used to enhance the translation, and returned in output.\n 
        :param str target: Target language code ([details](#description_langage_code_values)) (required)
        :param str format: Format of the source text.\n\nValid values are `text` for plain text, `html` for HTML pages, and `auto` for automatic detection. The MIME type of file format supported by SYSTRAN can also be used (application/vnd.openxmlformats, application/vnd.oasis.opendocument, ...)\n 
        :param int profile: Profile id\n 
        :param bool with_source: If `true`, the source will also be sent back in the response message. It can be useful when used with the withAnnotations option to align the source document with the translated document\n 
        :param bool with_annotations: If `true`, different annotations will be provided in the translated document. If the option 'withSource' is used, the annotations will also be provided in the source document. It will provide segments, tokens, not found words,...\n 
        :param str with_dictionary: User Dictionary or/and Normalization Dictionary ids to be applied to the translation result. Each dictionary 'id' has to be separate by a comma.\n 
        :param str with_corpus: Corpus to be applied to the translation result. Each corpus 'id' has to be separate by a comma.\n 
        :param list[str] options: Additional options.\n\nAn option can be a JSON object containing a set of key/value generic options supported by the translator. It can also be a string with the syntax '<key>:<value>' to pass a key/value generic option to the translator.\n 
        :param str encoding: Encoding. `base64` can be useful to send binary documents in the JSON body. Please note that another alternative is to use translateFile\n 
        :param bool async: If `true`, the translation is performed asynchronously.\n\nThe \"/translate/status\" service must be used to wait for the completion of the request and the \"translate/result\" service must be used to get the final result. The \"/translate/cancel\" can be used to cancel the request.\n 
        :param str batch_id: Batch Identifier\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: TranslationFileResponse
        """
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `translation_file_translate_get`")
        
        # verify the required parameter 'target' is set
        if target is None:
            raise ValueError("Missing the required parameter `target` when calling `translation_file_translate_get`")
        
        all_params = ['input', 'source', 'target', 'format', 'profile', 'with_source', 'with_annotations', 'with_dictionary', 'with_corpus', 'options', 'encoding', 'async', 'batch_id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_file_translate_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/file/translate'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'format' in params:
            query_params['format'] = params['format']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'with_source' in params:
            query_params['withSource'] = params['with_source']
        
        if 'with_annotations' in params:
            query_params['withAnnotations'] = params['with_annotations']
        
        if 'with_dictionary' in params:
            query_params['withDictionary'] = params['with_dictionary']
        
        if 'with_corpus' in params:
            query_params['withCorpus'] = params['with_corpus']
        
        if 'options' in params:
            query_params['options'] = params['options']
        
        if 'encoding' in params:
            query_params['encoding'] = params['encoding']
        
        if 'async' in params:
            query_params['async'] = params['async']
        
        if 'batch_id' in params:
            query_params['batchId'] = params['batch_id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        if 'input' in params:
            files['input'] = params['input']
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'multipart/mixed', '*/*'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['multipart/form-data', 'application/x-www-form-urlencoded', '*/*'])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='TranslationFileResponse', auth_settings=auth_settings)
        
        return response
        
    def translation_profile_get(self, **kwargs):
        """
        List of profiles
        List of profiles available for translation.\n

        :param str source: Source language code of the profile 
        :param str target: Target Language code of the profile\n 
        :param list[int] id: Identifier of the profile\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: ProfilesResponse
        """
        
        all_params = ['source', 'target', 'id', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_profile_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/profile'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'id' in params:
            query_params['id'] = params['id']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='ProfilesResponse', auth_settings=auth_settings)
        
        return response
        
    def translation_supported_languages_get(self, **kwargs):
        """
        Supported Languages
        List of language pairs in which translation is supported.\n\nThis list can be limited to a specific source language or target language.\n

        :param list[str] source: Language code of the source text\n 
        :param list[str] target: Language code into which to translate the source text\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: SupportedLanguageResponse
        """
        
        all_params = ['source', 'target', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_supported_languages_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/supportedLanguages'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='SupportedLanguageResponse', auth_settings=auth_settings)
        
        return response
        
    def translation_text_translate_get(self, input, target, **kwargs):
        """
        Translate
        Translate text from source language to target language\n

        :param list[str] input: Input text (this parameter can be repeated)\n (required)
        :param str source: Source language code ([details](#description_langage_code_values)) or `auto`.\n\nWhen the value is set to `auto`, the language will be automatically detected, used to enhance the translation, and returned in output.\n 
        :param str target: Target language code ([details](#description_langage_code_values)) (required)
        :param str format: Format of the source text.\n\nValid values are `text` for plain text, `html` for HTML pages, and `auto` for automatic detection. The MIME type of file format supported by SYSTRAN can also be used (application/vnd.openxmlformats, application/vnd.oasis.opendocument, ...)\n 
        :param int profile: Profile id\n 
        :param bool with_source: If `true`, the source will also be sent back in the response message. It can be useful when used with the withAnnotations option to align the source document with the translated document\n 
        :param bool with_annotations: If `true`, different annotations will be provided in the translated document. If the option 'withSource' is used, the annotations will also be provided in the source document. It will provide segments, tokens, not found words,...\n 
        :param str with_dictionary: User Dictionary or/and Normalization Dictionary ids to be applied to the translation result. Each dictionary 'id' has to be separate by a comma.\n 
        :param str with_corpus: Corpus to be applied to the translation result. Each corpus 'id' has to be separate by a comma.\n 
        :param bool back_translation: If `true`, the translated text will be translated back in source language\n 
        :param list[str] options: Additional options.\n\nAn option can be a JSON object containing a set of key/value generic options supported by the translator. It can also be a string with the syntax '<key>:<value>' to pass a key/value generic option to the translator.\n 
        :param str encoding: Encoding. `base64` can be useful to send binary documents in the JSON body. Please note that another alternative is to use translateFile\n 
        :param str callback: Javascript callback function name for JSONP Support\n 
        
        :return: TranslationResponse
        """
        
        # verify the required parameter 'input' is set
        if input is None:
            raise ValueError("Missing the required parameter `input` when calling `translation_text_translate_get`")
        
        # verify the required parameter 'target' is set
        if target is None:
            raise ValueError("Missing the required parameter `target` when calling `translation_text_translate_get`")
        
        all_params = ['input', 'source', 'target', 'format', 'profile', 'with_source', 'with_annotations', 'with_dictionary', 'with_corpus', 'back_translation', 'options', 'encoding', 'callback']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s' to method translation_text_translate_get" % key)
            params[key] = val
        del params['kwargs']

        resource_path = '/translation/text/translate'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}
        
        query_params = {}
        
        if 'input' in params:
            query_params['input'] = params['input']
        
        if 'source' in params:
            query_params['source'] = params['source']
        
        if 'target' in params:
            query_params['target'] = params['target']
        
        if 'format' in params:
            query_params['format'] = params['format']
        
        if 'profile' in params:
            query_params['profile'] = params['profile']
        
        if 'with_source' in params:
            query_params['withSource'] = params['with_source']
        
        if 'with_annotations' in params:
            query_params['withAnnotations'] = params['with_annotations']
        
        if 'with_dictionary' in params:
            query_params['withDictionary'] = params['with_dictionary']
        
        if 'with_corpus' in params:
            query_params['withCorpus'] = params['with_corpus']
        
        if 'back_translation' in params:
            query_params['backTranslation'] = params['back_translation']
        
        if 'options' in params:
            query_params['options'] = params['options']
        
        if 'encoding' in params:
            query_params['encoding'] = params['encoding']
        
        if 'callback' in params:
            query_params['callback'] = params['callback']
        
        header_params = {}
        
        form_params = {}
        files = {}
        
        body_params = None
        
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type([])

        # Authentication setting
        auth_settings = ['accessToken', 'apiKey']

        response = self.api_client.call_api(resource_path, method, path_params, query_params, header_params,
                                            body=body_params, post_params=form_params, files=files,
                                            response='TranslationResponse', auth_settings=auth_settings)
        
        return response
        









