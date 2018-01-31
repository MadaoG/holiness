from unittest import TestCase

import headline

class TestHeadline(TestCase):
    def test_basic_headline(self):
        h = headline.headline("headline")
        self.assertTrue(h == "==========================  H E A D L I N E  ===========================")
        
    def test_headline_width(self):
        h = headline.headline("headline", width=42)
        self.assertTrue(h == "===========  H E A D L I N E  ============")
        
    def test_headline_uppercase(self):
        h = headline.headline("headline", width=42, uppercase=False)
        self.assertTrue(h == "===========  h e a d l i n e  ============")
        
    def test_headline_spaces(self):
        h = headline.headline("headline", width=42, nr_spaces=0)
        self.assertTrue(h == "=============H E A D L I N E==============")
        
    def test_headline_spaces_max(self):
        """too much nr_spaces should not be ignored"""
        h = headline.headline("headline", width=42, nr_spaces=20)
        self.assertTrue(h == "=                    H E A D L I N E                    =")
        
    def test_headline_sym(self):
        h = headline.headline("headline", width=42, border="#")
        self.assertTrue(h == "#==========  H E A D L I N E  ===========#")
        
    def test_headline_sym_pair_tuple(self):
        h = headline.headline("headline", width=42, border=(">>", "<<"))
        self.assertTrue(h == ">>=========  H E A D L I N E  ==========<<")
        
    def test_headline_sym_pair_list(self):
        h = headline.headline("headline", width=42, border=["/*", "*/"])
        self.assertTrue(h == "/*=========  H E A D L I N E  ==========*/")
        
    def test_headline_sym_mirror(self):
        h = headline.headline("headline", width=42, border="# ")
        self.assertTrue(h == "# =========  H E A D L I N E  ========== #")
        
    def test_headline_like_c(self):
        h = headline.headline("headline", width=42, border="/*", char="*")
        self.assertTrue(h == "/**********  H E A D L I N E  ***********/")
        
    def test_headline_char(self):
        h = headline.headline("headline", width=42, char="-")
        self.assertTrue(h == "-----------  H E A D L I N E  ------------")
        
    def test_headline_char_sym(self):
        h = headline.headline("headline", width=42, char="-", border="!")
        self.assertTrue(h == "!----------  H E A D L I N E  -----------!")
        
    def test_headline_char_sym_equal(self):
        h = headline.headline("headline", width=42, char="-", border="=")
        self.assertTrue(h == "=----------  H E A D L I N E  -----------=")
        
    def test_headline_spacesym(self):
        h = headline.headline("headline", width=42, spacesym="_")
        self.assertTrue(h == "===========__H_E_A_D_L_I_N_E__============")
        
    def test_headline_surround(self):
        h = headline.headline("headline", width=42, surround=True)
        self.assertTrue(h == 
                "==========================================\n" +
                "===========  H E A D L I N E  ============\n" +
                "=========================================="
                )
        
    def test_headline_all(self):
        h = headline.headline(
            "headline",
            width=42,
            surround=True,
            border="% ",
            char="~",
            spacesym="~",
            nr_spaces=4,
            uppercase=False

        )
        self.assertTrue(h == 
                "% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %\n" +
                "% ~~~~~~~~~~~h~e~a~d~l~i~n~e~~~~~~~~~~~~ %\n" +
                "% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ %")

    def test_headline_char_multiple(self):
        h = headline.headline("headline", width=42, char="+-")
        self.assertTrue(h == "+-+-+-+-+-+  H E A D L I N E  +-+-+-+-+-+-")
