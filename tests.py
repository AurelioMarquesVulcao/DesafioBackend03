import unittest
from crawler import feed


class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(feed['feed'][0]['item']['title'], test_01)


    def test_02(self):
        self.assertEqual(feed['feed'][1]['item']['title'], test_02)


    def test_03(self):
        self.assertEqual(feed['feed'][2]['item']['title'], test_03)


    def test_04(self):
        self.assertEqual(feed['feed'][3]['item']['title'], test_04)


    def test_05(self):
        self.assertEqual(feed['feed'][0]['item']['link'], test_05)


    def test_06(self):
        self.assertEqual(feed['feed'][1]['item']['link'], test_06)


    def test_07(self):
        self.assertEqual(feed['feed'][2]['item']['link'], test_07)


    def test_08(self):
        self.assertEqual(feed['feed'][3]['item']['link'], test_08)


    def test_09(self):
        self.assertEqual(feed['feed'][0]['item']['description'][0]['content'], test_09)



#insert title of page do you need test.
test_01 = 'Congresso americano pede ajuda da indústria para legislar sobre carros autônomos'
test_02 = 'Vídeo: Harley-Davidson Fat Bob devora o asfalto com torque de Hyundai HB20 Turbo'
test_03 = 'Dodge dá US$ 10 de desconto por cv para Challenger, Charger e Durango'
test_04 = 'Nova RAM 2500 é flagrada no Brasil e chegará ainda em 2019'
#insert html do you need test.
test_05 = 'https://revistaautoesporte.globo.com/Noticias/noticia/2019/08/congresso-americano-pede-ajuda-da-industria-para-legislar-sobre-carros-autonomos.html'
test_06 = 'https://revistaautoesporte.globo.com/Videos/noticia/2019/08/video-harley-davidson-fat-bob-devora-o-asfalto-com-torque-de-hyundai-hb20-turbo.html'
test_07 = 'https://revistaautoesporte.globo.com/Noticias/noticia/2019/08/dodge-da-us-10-de-desconto-por-cv-para-challenger-charger-e-durango.html'
test_08 = 'https://revistaautoesporte.globo.com/Noticias/noticia/2019/08/nova-ram-2500-e-flagrada-no-brasil-e-chegara-ainda-em-2019.html'
# insert o html de uma imagem
test_09 = 'https://s2.glbimg.com/a_guseUbSA7YEnQLWvIvnNK-lh8=/620x413/e.glbimg.com/og/ed/f/original/2019/07/12/db2017al01216_large.jpg'
#if you want to unit test, with pytest remove the '#'
if __name__ == '__main__':
        unittest.main()