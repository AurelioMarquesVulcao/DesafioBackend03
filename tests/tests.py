import unittest
from crawler import crawler


class TestCrawler(unittest.TestCase):
    def test_01(self):
        self.assertEqual(crawler.feed['feed'][0]['item']['title'], test_01)

    def test_02(self):
        self.assertEqual(crawler.feed['feed'][1]['item']['title'], test_02)

    def test_03(self):
        self.assertEqual(crawler.feed['feed'][2]['item']['title'], test_03)

    def test_04(self):
        self.assertEqual(crawler.feed['feed'][3]['item']['title'], test_04)

    def test_05(self):
        self.assertEqual(crawler.feed['feed'][0]['item']['link'], test_05)

    def test_06(self):
        self.assertEqual(crawler.feed['feed'][1]['item']['link'], test_06)

    def test_07(self):
        self.assertEqual(crawler.feed['feed'][2]['item']['link'], test_07)

    def test_08(self):
        self.assertEqual(crawler.feed['feed'][3]['item']['link'], test_08)

    def test_09(self):
        self.assertEqual(crawler.feed['feed'][0]['item']['description'][0]['content'], test_09)


# insert title of page do you need test.
test_01 = 'Um avião caça clássico com motor V8 de Chevrolet Corvette'
test_02 = 'Audi Q8 estreia com motor de Porsche e tem quase R$ 80 mil em opcionais'
test_03 = 'Produção de veículos tem o melhor mês de julho desde 2014'
test_04 = 'Teste: Fiat Cronos HGT é um sedã esportivo apenas para os olhos'
# insert html do you need test.
test_05 = 'https://revistaautoesporte.globo.com/' \
          'Noticias/noticia/2019/08/um-aviao-caca-classico' \
          '-com-motor-v8-de-chevrolet-corvette.html'
test_06 = 'https://revistaautoesporte.globo.com/' \
          'Noticias/noticia/2019/08/audi-q8-estreia-com' \
          '-motor-de-porsche-e-tem-quase-r-80-mil-em-opcionais.html'
test_07 = 'https://revistaautoesporte.globo.com/' \
          'Publicidade/Valor-Investe-producao-de-veiculos/' \
          'noticia/2019/08/producao-de-veiculos-tem-o-' \
          'melhor-mes-de-julho-desde-2014.html'
test_08 = 'https://revistaautoesporte.globo.com/' \
          'testes/noticia/2019/08/teste-fiat-cronos-hgt-' \
          'e-um-seda-esportivo-apenas-para-os-olhos.html'
# insert o html de uma imagem
test_09 = 'https://s2.glbimg.com/2BaPR4aZnIqXAF4Iy8s9Z2FWvxA=/' \
          '620x413/e.glbimg.com/og/ed/f/original/2019/08/06/sptifiresolo.jpg'
# if you want to unit test, with pytest remove the '#'
if __name__ == '__main__':
    unittest.main()
