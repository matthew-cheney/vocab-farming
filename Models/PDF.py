from fpdf import FPDF


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
        """ Format page header """

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
        """ Format page footer """

        self.set_y(-10)

        self.set_font('Arial', 'I', 8)

        # Add page number
        page = 'Page ' + str(self.page_no()) + '/{nb}'
        self.cell(0, 10, page, 0, 0, 'C')

    def set_col(self, col):
        """ Set current column to col (0-based)"""

        self.col = col
        x = 10 + (col * 65)
        self.set_left_margin(x)
        self.set_x(x)

    def accept_page_break(self):
        """ Accept page break if at end of third column """

        if self.col < 2:
            # Go to next column
            self.set_col(self.col + 1)
            # Set ordinate to top
            if self.page_one:
                # Page 1 of dictionary has separate y0
                self.set_y(self.page_one_y0)
            else:
                self.set_y(self.y0)
            return False

        else:
            # Accept page break
            self.set_col(0)
            self.page_one = False
            return True
