from unittest import TestCase

import holiness

class TestHeadline(TestCase):
    def test_basic_headline(self):
        h = holiness.headline("headline")
        self.assertTrue(h == "==========================  H E A D L I N E  ===========================")
        
    def test_headline_width(self):
        h = holiness.headline("headline", width=42)
        self.assertTrue(h == "===========  H E A D L I N E  ============")
        
    def test_headline_uppercase(self):
        h = holiness.headline("headline", width=42, uppercase=False)
        self.assertTrue(h == "===========  h e a d l i n e  ============")
        
    def test_headline_spaces(self):
        h = holiness.headline("headline", width=42, nr_spaces=0)
        self.assertTrue(h == "=============H E A D L I N E==============")
        
    def test_headline_spaces_max(self):
        """too much nr_spaces should not be ignored"""
        h = holiness.headline("headline", width=42, nr_spaces=20)
        self.assertTrue(h == "=                    H E A D L I N E                    =")
        
    def test_headline_sym(self):
        h = holiness.headline("headline", width=42, border="#")
        self.assertTrue(h == "#==========  H E A D L I N E  ===========#")
        
    def test_headline_sym_pair_tuple(self):
        h = holiness.headline("headline", width=42, border=(">>", "<<"))
        self.assertTrue(h == ">>=========  H E A D L I N E  ==========<<")
        
    def test_headline_sym_pair_list(self):
        h = holiness.headline("headline", width=42, border=["/*", "*/"])
        self.assertTrue(h == "/*=========  H E A D L I N E  ==========*/")
        
    def test_headline_sym_mirror(self):
        h = holiness.headline("headline", width=42, border="# ")
        self.assertTrue(h == "# =========  H E A D L I N E  ========== #")
        
    def test_headline_like_c(self):
        h = holiness.headline("headline", width=42, border="/*", char="*")
        self.assertTrue(h == "/**********  H E A D L I N E  ***********/")
        
    def test_headline_char(self):
        h = holiness.headline("headline", width=42, char="-")
        self.assertTrue(h == "-----------  H E A D L I N E  ------------")
        
    def test_headline_char_sym(self):
        h = holiness.headline("headline", width=42, char="-", border="!")
        self.assertTrue(h == "!----------  H E A D L I N E  -----------!")
        
    def test_headline_char_sym_equal(self):
        h = holiness.headline("headline", width=42, char="-", border="=")
        self.assertTrue(h == "=----------  H E A D L I N E  -----------=")
        
    def test_headline_spacesym(self):
        h = holiness.headline("headline", width=42, spacesym="_")
        self.assertTrue(h == "===========__H_E_A_D_L_I_N_E__============")
        
    def test_headline_surround(self):
        h = holiness.headline("headline", width=42, surround=True)
        self.assertTrue(h == 
                "==========================================\n" +
                "===========  H E A D L I N E  ============\n" +
                "=========================================="
                )
        
    def test_headline_all(self):
        h = holiness.headline(
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
        h = holiness.headline("headline", width=42, char="+-")
        self.assertTrue(h == "+-+-+-+-+-+  H E A D L I N E  +-+-+-+-+-+-")
