from fpdf import FPDF


testdata = (
    ("Pos.", "Leistung", "Gesamtpreis"),
    ("01", "Programmierung einer Website", "200,00 EUR"),
    ("02", "Programmierung einer Website", "2000,00 EUR")
)

invoicedata = {
    'number':'21004',
    'client': "Joscha Brüning \nTeststraße1 \n24103 Kiel",
    'invoiceHeader': ('NR. 21004','Kunden-Nr.:005','10.08.2021'),
    'invoiceData':(
        ("Pos.", "Leistung", "Gesamtpreis"),
        ("01", "Programmierung einer Website", "200,00 EUR"),
        ("02", "Programmierung einer Website", "2000,00 EUR"),
        ("02", "Programmierung einer Website", "2000,00 EUR"),
    ),
    'sum':'Gesamtbetrag: 2200 '+chr(128)
}

personaldata ={
    'header':'JOSCHA BRÜNING • LEGIENSTRAßE 18 • 24103 KIEL',
    'disclaimer':'Im ausgewiesenen Rechnungsbetrag ist gemäß § 19 UStG keine Umsatzsteuer enthalten.',
    'contact':[
        ('JOSCHA BRÜNING','HELLO@JOSCHABRUENING.EU','FINANZAMT KIEL','SPARKASSE PADERBORN-DETMOLD'),
        ('LEGIENSTRAßE 18','M: +49 (0) 176 200 409 74','STEUERNR 20/014/06328','BIC WELADE3LXXX'),
        ('24103 KIEL-ZENTRUM','','','IBAN DE38 4765 0130 0135 3843 94')
    ]
}



class PDF(FPDF):
    def setup(self):
        self.margin=10
        self.width=210
        self.height=297
        self.innerWidth=self.width-(self.margin*2)
        self.innerHeight=self.height-(self.margin*2)
        self.fs1=10
        self.fs2= .6
    def lines(self):
        self.set_line_width(0.0)
        self.line(self.margin,self.height/2,self.width-self.margin,self.height/2)

    def newInvoice(self,data):
        self.setup()
        self.add_page()
        self.add_font('Founders', '', 'FoundersGroteskMono-Light.ttf', uni=True)
        self.add_font('Founders_m', '', 'FoundersGroteskMono-Medium.ttf', uni=True)
        self.set_font('Founders', '', self.fs1)
        table_line_height = self.font_size * 2.5
        line_height = self.font_size * 1.5

        self.ln(line_height*4)
        topY = self.get_y()
        self.set_font('Founders_m', '', self.fs1*self.fs2)
        self.cell(self.innerWidth/2,line_height,txt=personaldata['header'])
        self.set_font('Founders', '', self.fs1)
        self.ln(line_height*self.fs2*1.3)
        self.multi_cell(self.innerWidth/3,line_height,txt=data['client'])
        bottomY = self.get_y()
        self.set_xy(self.innerWidth/2,topY)
        self.set_font_size(60 )
        self.cell(self.innerWidth/2,self.font_size,txt='JB',align='R')
        self.set_font_size(self.fs1)
        self.set_y(bottomY)
        self.ln(line_height*7)

        col_width = (self.innerWidth / 10,7*(self.innerWidth / 10),2*(self.innerWidth / 10))  # distribute content evenly
        algn = ('L','L','R')
        self.set_font_size(20)
        self.cell(txt='Rechnung')
        self.set_font_size(self.fs1)
        self.ln(table_line_height)

        algn = ('L','C','R')
        for x, dat in enumerate(data['invoiceHeader']):
            self.multi_cell(self.innerWidth/3,table_line_height,dat,align=algn[x], ln=3, max_line_height=self.font_size)

        algn = ('L','L','R')
        self.ln(table_line_height)
        for i,row in enumerate(data['invoiceData']):
            for j,datum in enumerate(row):
                self.multi_cell(col_width[j], table_line_height, datum, border= 'B' if i==0 else 0  , align=algn[j], ln=3, max_line_height=self.font_size)
            self.ln(table_line_height)

        self.ln(table_line_height)
        self.cell(w=0,txt=data['sum'],align='R')

        self.set_y(-50)
        self.cell(0,line_height,txt=personaldata['disclaimer'])
        self.ln(line_height)
        self.cell(0,line_height,txt='–')
        self.ln(line_height*2)
        self.set_font('Founders_m', '', self.fs1*self.fs2)
        col_width = (3*(self.innerWidth / 12),3*(self.innerWidth / 12),3*(self.innerWidth / 12),3*(self.innerWidth / 12))  # distribute content evenly
        for row in personaldata['contact']:
            for ind,value in enumerate(row):
                self.multi_cell(col_width[ind], self.font_size, value, border=0  , ln=3, max_line_height=self.font_size)
            self.ln(self.font_size*1.4)

pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.newInvoice(invoicedata)
pdf.output('test.pdf','F')