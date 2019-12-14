# Vocab Farming
#Previously known as Book Metadata Study Guides

## Purpose
Vocab Farming aims to help those learning English at a mid to advanced level enlarge their vocabulary. It processes text, mainly from books, and returns study guides customized for each chapter. These study guides feature new words the learner might not know, as well as definitions for other potentially unfamiliar words.

## How to Use
Vocab Farming is run from the driver file called <addr>ProcessBook.py</addr>

Before running the tool, the user must create the following file structure. We will use the Wizard of Oz as our example book and es (Spanish) as our language code.

In the directory Projects, create a directory called Wizard_Of_Oz

In the directory Wizard_Of_Oz, create a directory called chapters

Place each chapter to be processed in the directory chapters. Each chapter must be in JSON format, with 3 entries: chapter_number, chapter_title, and body. The file names do not matter, but must have .txt extension. See below for tips on getting chapters into this format. Example:

{
    "chapter_number": 2,
    "chapter_title": "3. How Dorothy Saved the Scarecrow",
    "body": "\nWhen Dorothy was left alone she began to feel hungry...."
}

Once everything is set up, run the program with the following command (from the top directory):

<addr>python3 ProcessBook.py Wizard_Of_Oz es

The script will create a new directory title as the chosen language code within the book's directory in Projects. Within that directory, the script will create 3 things:

1. <b>master_dictionary.txt</b>: This JSON file contains all potentially unfamiliar words for the entire book, along with their approximate translations.
2. <b>study_guides</b>: This directory contains a JSON file for each chapter. Each file contains new words to learn for that chapter, word to remember from previous chapters, as well as other potentially unfamiliar words.
3. <b>directory_languageCode.pdf</b>: This is a pdf representation of the JSON files listed above, for more convenient printing. In our example, this file is called Wizard_Of_Oz_es.pdf.

Currently, the only supported language codes are definitions, ru (Russian), and es (Spanish).</br>
Definitions are primarily used for development, and may contain more bugs. More comprehensive support will be added in the future.</br>
PDF creation only supports Russian and Spanish.

## Google Translate API
In order to use language codes other than 'definitions', you must set up a project with the Google Translate API. They currently offer a free tier of 500,000 characters per month.

How to: https://cloud.google.com/translate/docs/basic/setup-basic

After you set up the API, you will have to set the GOOGLE_APPLICATION_CREDENTIALS environment variable every time you start a new terminal session:

export GOOGLE_APPLICATION_CREDENTIALS=\<path_to_api_key\>

## Preprocessing Chapters
The Utils directory contains 2 scripts to help prepare texts for this project. They are called Full_Text_To_Raw_Chapters_Template.py and Raw_Chapters_To_Formatted_Template.py. However, these files are simply templates, and will likely need to be modified slightly to work with any specific book.
