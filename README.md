<h1>Infoglobo</h1>

Create a crawler that reads this feed https://revistaautoesporte.globo.com/rss/ultimas/feed.xml and return a Json
<br>
<li>Implemented with Python 3.7

<h4>How to start testing<h4>
<li>A test report has been created by simply opening the index.html file in the htmlcov folder.<br>

In the file tests.py was placed 9 unit tests, and the strings, expected for each of the tests.<br>

To repeat the tests just insert new strings.<br>
Were tested:<br>
-The first 4 headlines of the feed.<br>
-The first 4 links from feeds.<br>
-The first image link from the first article.<br><br>


<li>Running the tests:<br>

In your terminal open the tests application folder.<br>
follow the instructions:<br>
coverage run tests.py &#10140; starts the test file.<br>
coverage g report -m &#10140; will create and display the test report.<br>
coverage html &#10140; will create an html report that will be saved in the folder, htmlcov.

<li> Expected result in json file:

````{
    "feed": [
        {
            "item": {
                "title": "Um avião caça clássico com motor V8 de Chevrolet Corvette",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/08/um-aviao-caca-classico-com-motor-v8-de-chevrolet-corvette.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2BaPR4aZnIqXAF4Iy8s9Z2FWvxA=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/sptifiresolo.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O Supermarine Spitfire foi a grande estrela da Batalha da Grã Bretanha, conflito da Segunda Guerra Mundial que durou de julho a outubro de 1940. Foi o primeiro racha entre os britânicos e os alemães, que massacraram a Inglaterra com bombardeios intensos. E também a primeira batalha lutada apenas por aviões."
                    },
                    {
                        "type": "text",
                        "content": "Embora o Hawker Hurricane tenha sido vital no conflito, foi o recém-lançado e mais rápido Spitfire que ganhou a fama e era até mais reconhecido pela população no solo, talvez pelo seu desenho singular, que inclui asas com pontas elípticas. Eles foram o terror dos Messerschmitt BF 109E."
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2018/11/aviao-com-motor-de-porsche-911.html"
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/06/o-novo-helicoptero-do-donald-trump-e-uma-limusine-aerea.html"
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/05/o-dia-em-que-niki-lauda-provou-que-boeing-estava-errada.html"
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/04/o-dia-que-porsche-levou-o-917-para-conhecer-o-concorde.html"
                    },
                    {
                        "type": "text",
                        "content": "A popularidade não desapareceu ao longo do tempo. Tanto que uma empresa britânica, batizada oportunisticamente como Supermarine, desenvolveu uma réplica moderna do Spitfire."
                    },
                    {
                        "type": "text",
                        "content": "Como toda réplica, avião não é exatamente como o original, uma vez que a sua escala em relação ao caça chega a 90%, no máximo. É algo bem perto, o que não dá aquela impressão de aeronave amadora, por mais que seja vendido em kits para serem montados.\n\tBatizado como MK26B, o modelo maior era acompanhado do MK26 (80% do tamanho) e do MK25 (75% da escala), ambos fora de linha."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/-frai5IBu4_sfNAtnCQs92Ge4QE=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/v8.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Claro que a diferença de tamanho não é a única alteração. O Spitfire mirim tem motor bem diferente daqueles Rolls-Royce Merlin ou Griffo, e aposta em propulsor de automóvel. Os menores MK26 e MK25 podiam vir com o V6 3.5 da Isuzu de 253 cv, mas o MK26B carrega o mesmo LS2 V8 6.0 do antigo Corvette, não muito diferente do propulsor utilizado pelo Camaro."
                    },
                    {
                        "type": "text",
                        "content": "Dado o menor tamanho e peso, aliviado também pela ausência de armas ou blindagem, o Spitfire não faz feio com o seu oito cilindros de 436 cv, capaz de levá-lo além dos 400 km/h.  Sem falar que faz manobras com forças que chegam a até seis gravidades. E tem autonomia de mais de 1.000 km, perfeito para patrulhar o Canal da Mancha por horas."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2ZMAvl1lYgeDuHTQHhHlyhGpn7c=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/sptifire-voo.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Ainda que não consigam perseguir os Supermarines mais avançados da Segunda Guerra, com motores Rolls-Royce V12 de até 37 litros e mais de 2.300 cv e capacidade de ultrapassar os 600 km/h, as réplicas são rápidas e têm uma vantagem que o Spitfire original não tinha: injeção de gasolina. Os caças do passado ainda contavam com carburador e levavam pau do Messerschmitt, com injeção direta e capaz de fazer mergulhos vertiginosos sem medo de ficar sem combustível, enquanto o avião britânico tinha carburador e lidava com o problema de afogamento nesses manobras."
                    },
                    {
                        "type": "text",
                        "content": "Para se aproximar do avião clássico, é possível instalar imitações dos canhões automáticos de 20 mm que lotavam as asas do original, mas nada que faça justiça ao nome do original (Cospe-fogo), felizmente."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2avrzO96sWj616hT33wQfHWoBT8=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/batalha.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Em festivais como o de Velocidade de Goodwood, o Supermarine é idolatrado até hoje. Até mesmo a Ford embarcou no saudosismo no Spitfire: a rival norte-americana fez uma edição especial do Mustang com a mesma padronagem dos caças da Batalha da Grã-Bretanha para o evento britânico. É até curioso, uma vez que uma das fontes do batismo do esportivo foi justamente o caça North American P-51 Mustang, outra estrela da Segunda Guerra."
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2018/07/dez-melhores-coisas-do-festival-de-velocidade-de-goodwood-em-video.html"
                    },
                    {
                        "type": "text",
                        "content": "O V8 Chevrolet já foi utilizado por outras aeronaves, inclusive, um helicóptero: o Vertical Hummingbird, vendido como kit e lançado em 1991. Porém, o grande barato é ver um borbulhante oito cilindros embaixo do enorme “capô” de um caça clássico. Gravado em vídeo em, um Spitfire passa em rasante com um ruído grave e característico. Um verdadeiro muscle plane, por assim dizer."
                    },
                    {
                        "type": "text",
                        "content": "Acompanha tudo de Autoesporte? Agora você pode ler as edições e matérias exclusivas no Globo Mais, o app com conteúdo para todos os momentos do seu dia. Baixe agora!"
                    },
                    {
                        "type": "link",
                        "content": "https://globomais.com.br/"
                    }
                ]
            }
        },
