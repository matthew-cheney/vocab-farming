# header_footer.py
from glob import glob

from fpdf import FPDF
import json
import os


class PDF(FPDF):

    def __init__(self, book_title):
        super().__init__(format='letter')
        self.book_title = book_title

    def header(self):
        # Set up a logo
        # self.image('snakehead.jpg', 10, 8, 33)
        self.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
        self.add_font('DejaVu', 'B', 'DejaVuSansCondensed-Bold.ttf', True)
        self.set_font('DejaVu', 'B', 15)

        # Add an address
        self.cell(0, 0, self.book_title, align='C', ln=1)

        # Line break
        self.ln(20)

        self.y = self.get_y()

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
            self.set_y(self.y)
            return False
        else:
            self.set_col(0)
            return True

    def chapter_title(self, num, label):

        pass

    def chapter_body(self, file):
        pass

    def print_chapter(self, num, title, file):
        pass


def create_pdf(pdf_path, json_path):
    json_dict = _json_to_dict(json_path)

    pdf = PDF('Wizard of Oz')

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
    pdf.set_font('DejaVu', '', 15)

    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()
    # pdf.set_font('Times', '', 18)
    pdf.cell(0, 0, txt=f'{json_dict["chapter_title"]}', align='C', ln=1)
    # pdf.set_font('Times', '', 12)
    for term in json_dict['featured_words']:
        pdf.cell(0, 10, txt=f'{term} : {json_dict["featured_words"][term]}', ln=1)
    pdf.output(pdf_path)


def _json_to_dict(json_path):
    with open(json_path, 'r') as f:
        json_string = f.read()
        json_dict = json.loads(json_string)
    return json_dict

def create_dictionary(pdf_path, json_path):
    json_dict = _json_to_dict(json_path)

    pdf = PDF('Wizard of Oz')

    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', True)
    pdf.set_font('DejaVu', '', 15)

    pdf.alias_nb_pages()
    pdf.add_page()
    # pdf.set_font('Times', '', 18)
    pdf.cell(0, 0, txt=f'Master Dictionary', align='C', ln=1)
    # pdf.set_font('Times', '', 12)
    for term in json_dict:
        pdf.cell(0, 5, txt=f'{term}:',
                 ln=1)
        pdf.cell(0, 5, txt=f'     {json_dict[term]}',
                 ln=1)
        pdf.cell(0, 2, "", ln=1)
    pdf.output(pdf_path)



if __name__ == '__main__':
    """filenames = glob('Wizard_Of_Oz/ru/study_guides/*.txt')
    # for file in filenames:
    #     create_pdf(f'pdfs/{os.path.basename(file)[:-3]}.pdf', file)
    create_dictionary(f'pdfs/dictionary.pdf', 'Wizard_Of_Oz/ru/master_dictionary.txt')"""
    pdf = PDF('Wizard of Oz')
    pdf.set_title('Wizard of Oz')
    pdf.set_author('L. Frank Baum')
    pdf.print_chapter(1, 'Chapter 1', 'Wizard_Of_Oz/raw_chapters/01_full_text.txt')
    pdf.print_chapter(2, 'Chapter 2', 'Wizard_Of_Oz/raw_chapters/02_full_text.txt')
    pdf.output('test_multi_column.pdf')
