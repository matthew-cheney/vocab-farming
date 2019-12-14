from glob import glob

from Models.PDF import PDF
from Utils.JSON_Utils import json_to_dict


class PDFGenerator:

    MAX_WORDS_PER_COLUMN = 20

    def generate_pdf(self, book_name, project_name, language_code):
        """ Generate PDF study guide for project_name in language_code """

        pdf = PDF(book_name)

        # DejaVu font supports Cyrillic and Spanish special characters
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
        pdf.set_font('DejaVu', '', 15)

        # Add page for each file (study guide)
        filenames = glob(f'Projects/{project_name}/{language_code}/study_guides/*.txt')  # noqa: E501
        for file in sorted(filenames):
            self._create_pdf(file, pdf)

        # Add dictionary at end of PDF study guide
        self._create_dictionary(
            f'Projects/{project_name}/{language_code}/master_dictionary.txt', pdf)  # noqa: E501

        # Write the pdf to appropriate directory
        pdf.output(f'Projects/{project_name}/{language_code}/{project_name}_{language_code}.pdf')  # noqa: E501

    def _create_pdf(self, json_path, pdf):
        """ Create page in pdf for specified chapter study guide """

        json_dict = self._json_to_dict(json_path)

        # Initial page set up
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_col(0)
        pdf.set_y(pdf.get_y() + 5)

        # Add chapter title to header
        pdf.cell(0, 0, txt=f'{json_dict["chapter_title"]}', align='C', ln=1)
        pdf.set_y(pdf.get_y() + 5)

        # Establish new y (top of content, below header)
        y = pdf.get_y()

        # New words to learn

        # Print heading of column 1
        pdf.set_y(pdf.get_y() + 5)  # Add space before heading
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='New words to learn:', ln=1)
        pdf.set_y(pdf.get_y() + 5)  # Add space after heading

        line_cutoff = 35  # Max characters that fit on a line

        # Print each word to column 1
        pdf.set_font('DejaVu', '', 15)
        word_counter = 0
        for term in json_dict['featured_words']:
            if word_counter >= self.MAX_WORDS_PER_COLUMN:
                continue
            term_to_print = f'{term} : {json_dict["featured_words"][term]}'
            if len(term_to_print) > line_cutoff:
                # Term is longer than allowed limit, split to two lines
                pdf.cell(0, 10,
                         txt=f'{term_to_print[:line_cutoff]}-',
                         ln=1)
                pdf.cell(0, 10,
                         txt=f'          -{term_to_print[line_cutoff:]}',
                         ln=1)
            else:
                # Term is shorter than allowed limit
                pdf.cell(0, 10, txt=term_to_print,
                         ln=1)
            word_counter += 1
        if word_counter == 0:
            pdf.cell(0, 10, txt='No new words to feature!',
                     ln=1)

        # Previously featured words

        # Print heading of column 2
        pdf.set_col(1.5)
        pdf.set_y(y)  # Reset y to top of content, below header
        pdf.set_y(pdf.get_y() + 5)  # Add space before heading
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='Remember these words:', ln=1)
        pdf.set_y(pdf.get_y() + 5)  # Add space after heading

        # Print each word to column 2
        pdf.set_font('DejaVu', '', 15)
        word_counter = 0
        for term in json_dict['previously_featured']:
            if word_counter >= self.MAX_WORDS_PER_COLUMN:
                continue
            term_to_print = \
                f'{term} : {json_dict["previously_featured"][term]}'
            if len(term_to_print) > line_cutoff:
                # Term is longer than allowed limit, split to two lines
                pdf.cell(0, 10,
                         txt=f'{term_to_print[:line_cutoff]}-',
                         ln=1)
                pdf.cell(0, 10,
                         txt=f'          -{term_to_print[line_cutoff:]}',
                         ln=1)
            else:
                # Term is shorter than allowed limit
                pdf.cell(0, 10, txt=term_to_print, ln=1)
            word_counter += 1
        if word_counter == 0:
            pdf.cell(0, 10, txt='No previously featured words',
                     ln=1)

        # Reset column for footer and next page
        pdf.set_col(0)

    def _json_to_dict(self, json_path):
        """ Open file at json_path and return python dict form """

        with open(json_path, 'r') as f:
            json_string = f.read()
        return json_to_dict(json_string)

    def _create_dictionary(self, json_path, pdf):
        """ Create master dictionary at end of pdf study guide """

        json_dict = self._json_to_dict(json_path)

        # pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
        # pdf.set_font('DejaVu', '', 15)

        # pdf.alias_nb_pages()

        pdf.add_page()

        # Add heading: Dictionary
        pdf.set_y(pdf.get_y() + 5)  # Add space before heading
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='Dictionary', align='C', ln=1)

        # Add dictionary contents
        pdf.set_font('DejaVu', '', 15)

        # Set separate y0 for page 1 to fit content beneath heading
        pdf.set_page_one_y0(30)
        pdf.set_y(30)

        # Print each term and translation

        line_cutoff = 17

        for term in json_dict:
            term_parts = term.split(" : ")
            term_to_print = f'{json_dict[term]}'
            pdf.cell(0, 5, txt=f'{term_parts[0]} ({term_parts[1]}):',
                     ln=1)
            while len(term_to_print) > 0:
                # Split translation to multiple lines as needed
                pdf.cell(0, 5, txt=f'     {term_to_print[:line_cutoff]}',
                         ln=1)
                term_to_print = term_to_print[line_cutoff:]
            pdf.cell(0, 2, "", ln=1)
