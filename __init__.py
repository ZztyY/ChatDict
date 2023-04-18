"""
ChatDict
==========

Provides:
    1. Explanation of specific words from ChatGPT
"""

import os
import json

import openai

from ChatDict.util import is_alphabet


class Dict:
    """
    base class
    """
    ENV_PATH = './env/env.json'

    def __init__(self):
        if not os.path.exists(self.ENV_PATH):
            if not os.path.exists('./env'):
                os.makedirs('./env')
            with open(self.ENV_PATH, 'w+', encoding='utf-8') as env_f:
                json.dump({"OPENAI_API_KEYS": False}, env_f)

        with open(self.ENV_PATH, 'r', encoding='utf-8') as env_f:
            self.env = json.load(env_f)

        if self.env['OPENAI_API_KEYS']:
            self.openai_api_key = self.env['OPENAI_API_KEYS']
            self.chatgpt_haskey = True
        else:
            self.chatgpt_haskey = False

    def query(self, word):
        """
        word query
        :param word: A specified word (str)
        :return: explanation of word (str)
        """
        translate_to = "Chinese"
        if word:
            if not is_alphabet(word[0]):
                translate_to = "English"

        if self.chatgpt_haskey:
            openai.api_key = self.openai_api_key
            print("To " + translate_to)
            messages = [
                {"role": "system", "content": "You are a encyclopedia scholar who is proficient in all the languages."},
                {"role": "user", "content": f"Could you explain the meaning of \"{word}\" in {translate_to}?"
                                            + "Make sure to be short, precise, and easy to understand. Give two common examples, which must be *bilingual*. Reply must use the format: Meaning: \nExample 1:\nExample 2:"}
            ]
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            chat_info = response.choices[0].message.content
            return chat_info
        else:
            return "no openai_api_key"
