# Fishing for Vocab

## Purpose
This tool aims to help those learning English at a mid to advanced level enlarge their vocabulary. It processes text, mainly from books, and returns study guides customized for each chapter. These study guides feature new words the learner might not know, as well as definitions for other potentially unfamiliar words.

## How to Use
The tool is run from the driver file called <addr>Tester.py</addr>

Before running the tool, the user must create the following file structure. Follow these steps. We will use Tom Sawyer as our example book and definitions as our language code.

In the same directory as Tester.py, create a directory called Tom_Sawyer

In the directory Tom_Sawyer, create a directory called chapters

Place each chapter to be processed in the directory chapters. Each chapter must be in JSON format, with 3 entries: chapter_number, chapter_title, and body. The file names do not matter, but must have .txt extension. Example:

{
    "chapter_number": 2,
    "chapter_title": "3. How Dorothy Saved the Scarecrow",
    "body": "\nWhen Dorothy was left alone she began to feel hungry...."
}
