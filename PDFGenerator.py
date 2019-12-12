# header_footer.py
from glob import glob

from fpdf import FPDF
import json
import os

class PDFGenerator:

    MAX_WORDS_PER_COLUMN = 21

    def create_pdf(self, pdf_path, json_path, pdf):
        json_dict = self._json_to_dict(json_path)

        # Create the special value {nb}
        pdf.alias_nb_pages()
        pdf.add_page()
        # pdf.set_font('Times', '', 18)
        pdf.set_col(0)
        pdf.set_y(pdf.get_y() + 5)
        pdf.cell(0, 0, txt=f'{json_dict["chapter_title"]}', align='C', ln=1)
        pdf.set_y(pdf.get_y() + 5)
        y = pdf.get_y()
        # pdf.set_font('Times', '', 12)

        # New words to learn
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='New words to learn:', ln=1)
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('DejaVu', '', 15)
        word_counter = 0
        for term in json_dict['featured_words']:
            if word_counter >= self.MAX_WORDS_PER_COLUMN:
                continue
            pdf.cell(0, 10, txt=f'{term} : {json_dict["featured_words"][term]}',
                     ln=1)
            word_counter += 1
        if word_counter == 0:
            pdf.cell(0, 10, txt='No new words to feature!',
                     ln=1)

        # Previously featured words
        pdf.set_col(1.5)
        pdf.set_y(y)
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='Remember these words:', ln=1)
        pdf.set_font('DejaVu', '', 15)
        pdf.set_y(pdf.get_y() + 5)
        word_counter = 0
        for term in json_dict['previously_featured']:
            if word_counter >= self.MAX_WORDS_PER_COLUMN:
                continue
            pdf.cell(0, 10, txt=f'{term} : {json_dict["previously_featured"][term]}',
                     ln=1)
            word_counter += 1
        if word_counter == 0:
            pdf.cell(0, 10, txt='No previously featured words',
                     ln=1)

        pdf.set_col(0)


    def _json_to_dict(self, json_path):
        with open(json_path, 'r') as f:
            json_string = f.read()
            json_dict = json.loads(json_string)
        return json_dict


    def create_dictionary(self, pdf_path, json_path, pdf):
        json_dict = self._json_to_dict(json_path)

        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
        pdf.set_font('DejaVu', '', 15)

        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('Arial', 'B', 15)
        pdf.cell(0, 0, txt='Dictionary', align='C', ln=1)
        pdf.set_font('DejaVu', '', 15)
        pdf.set_page_one_y0(30)
        pdf.set_y(30)
        # pdf.set_font('Times', '', 18)
        # pdf.cell(0, 0, txt=f'Master Dictionary', align='C', ln=1)
        # pdf.set_font('Times', '', 12)
        for term in json_dict:
            term_parts = term.split(" : ")
            pdf.cell(0, 5, txt=f'{term_parts[0]} ({term_parts[1]}):',
                     ln=1)
            pdf.cell(0, 5, txt=f'     {json_dict[term]}',
                     ln=1)
            pdf.cell(0, 2, "", ln=1)
        # pdf.output(pdf_path)


    def generate_pdf(self, book_name, project_name, language_code):
        pdf = PDF(book_name)
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
        pdf.set_font('DejaVu', '', 15)

        filenames = glob(f'Projects/{project_name}/{language_code}/study_guides/*.txt')
        for file in sorted(filenames):
            # print(file)
            self.create_pdf(f'pdfs/{os.path.basename(file)[:-3]}.pdf', file, pdf)
        self.create_dictionary(f'pdfs/dictionary.pdf', f'Projects/{project_name}/{language_code}/master_dictionary.txt', pdf)
        pdf.output(f'Projects/{project_name}/{language_code}/{project_name}_{language_code}.pdf')

class PDF(FPDF):

    def __init__(self, title):
        super().__init__(format='letter')
        self.col = 0
        self.y0 = 10
        self.title = title
        self.page_one = True
        self.page_one_y0 = self.y0

    def set_page_one_y0(self, page_one_y0):
        self.page_one_y0 = page_one_y0

    def header(self):
        self.set_font('Arial', 'B', 15)
        w = len(self.title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(255, 255, 255)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(0, 0, 0)
        self.set_line_width(1)
        self.cell(w, 9, self.title, 1, 1, 'C', True)
        self.set_line_width(10)
        self.y0 = self.get_y()

    def footer(self):
        self.set_y(-10)

        self.set_font('Arial', 'I', 8)

        # Add a page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

    def set_col(self, col):
        self.col = col
        x = 10 + (col * 65)
        self.set_left_margin(x)
        self.set_x(x)

    def accept_page_break(self):
        if self.col < 2:
            # Go to next column
            self.set_col(self.col + 1)
            # Set ordinate to top
            if self.page_one:
                self.set_y(self.page_one_y0)
                print(f"page_one: {self.page_one_y0}, y0: {self.y0}")
            else:
                self.set_y(self.y0)
            return False
        else:
            self.set_col(0)
            self.page_one = False
            return True

    def chapter_title(self, num, label):

        pass

    def chapter_body(self, file):
        pass

    def print_chapter(self, num, title, file):
        pass