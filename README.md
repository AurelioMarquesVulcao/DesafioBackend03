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
                "title": "Um avi�o ca�a cl�ssico com motor V8 de Chevrolet Corvette",
                "link": "https://revistaautoesporte.globo.com/Noticias/noticia/2019/08/um-aviao-caca-classico-com-motor-v8-de-chevrolet-corvette.html",
                "description": [
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2BaPR4aZnIqXAF4Iy8s9Z2FWvxA=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/sptifiresolo.jpg"
                    },
                    {
                        "type": "text",
                        "content": "O Supermarine Spitfire foi a grande estrela da Batalha da Gr� Bretanha, conflito da Segunda Guerra Mundial que durou de julho a outubro de 1940. Foi o primeiro racha entre os brit�nicos e os alem�es, que massacraram a Inglaterra com bombardeios intensos. E tamb�m a primeira batalha lutada apenas por avi�es."
                    },
                    {
                        "type": "text",
                        "content": "Embora o Hawker Hurricane tenha sido vital no conflito, foi o rec�m-lan�ado e mais r�pido Spitfire que ganhou a fama e era at� mais reconhecido pela popula��o no solo, talvez pelo seu desenho singular, que inclui asas com pontas el�pticas. Eles foram o terror dos Messerschmitt BF 109E."
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
                        "content": "A popularidade n�o desapareceu ao longo do tempo. Tanto que uma empresa brit�nica, batizada oportunisticamente como Supermarine, desenvolveu uma r�plica moderna do Spitfire."
                    },
                    {
                        "type": "text",
                        "content": "Como toda r�plica, avi�o n�o � exatamente como o original, uma vez que a sua escala em rela��o ao ca�a chega a 90%, no m�ximo. � algo bem perto, o que n�o d� aquela impress�o de aeronave amadora, por mais que seja vendido em kits para serem montados.\n\tBatizado como MK26B, o modelo maior era acompanhado do MK26 (80% do tamanho) e do MK25 (75% da escala), ambos fora de linha."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/-frai5IBu4_sfNAtnCQs92Ge4QE=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/v8.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Claro que a diferen�a de tamanho n�o � a �nica altera��o. O Spitfire mirim tem motor bem diferente daqueles Rolls-Royce Merlin ou Griffo, e aposta em propulsor de autom�vel. Os menores MK26 e MK25 podiam vir com o V6 3.5 da Isuzu de 253 cv, mas o MK26B carrega o mesmo LS2 V8 6.0 do antigo Corvette, n�o muito diferente do propulsor utilizado pelo Camaro."
                    },
                    {
                        "type": "text",
                        "content": "Dado o menor tamanho e peso, aliviado tamb�m pela aus�ncia de armas ou blindagem, o Spitfire n�o faz feio com o seu oito cilindros de 436 cv, capaz de lev�-lo al�m dos 400 km/h.� Sem falar que faz manobras com for�as que chegam a at� seis gravidades. E tem autonomia de mais de 1.000 km, perfeito para patrulhar o Canal da Mancha por horas."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2ZMAvl1lYgeDuHTQHhHlyhGpn7c=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/sptifire-voo.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Ainda que n�o consigam perseguir os Supermarines mais avan�ados da Segunda Guerra, com motores Rolls-Royce V12 de at� 37 litros e mais de 2.300 cv e capacidade de ultrapassar os 600 km/h, as r�plicas s�o r�pidas e t�m uma vantagem que o Spitfire original n�o tinha: inje��o de gasolina. Os ca�as do passado ainda contavam com carburador e levavam pau do Messerschmitt, com inje��o direta e capaz de fazer mergulhos vertiginosos sem medo de ficar sem combust�vel, enquanto o avi�o brit�nico tinha carburador e lidava com o problema de afogamento nesses manobras."
                    },
                    {
                        "type": "text",
                        "content": "Para se aproximar do avi�o cl�ssico, � poss�vel instalar imita��es dos canh�es autom�ticos de 20 mm que lotavam as asas do original, mas nada que fa�a justi�a ao nome do original (Cospe-fogo), felizmente."
                    },
                    {
                        "type": "image",
                        "content": "https://s2.glbimg.com/2avrzO96sWj616hT33wQfHWoBT8=/620x413/e.glbimg.com/og/ed/f/original/2019/08/06/batalha.jpg"
                    },
                    {
                        "type": "text",
                        "content": "Em festivais como o de Velocidade de Goodwood, o Supermarine � idolatrado at� hoje.�At� mesmo a Ford embarcou no saudosismo no Spitfire: a rival norte-americana fez uma edi��o especial do Mustang com a mesma padronagem dos ca�as da Batalha da Gr�-Bretanha para o evento brit�nico. � at� curioso, uma vez que uma das fontes do batismo do esportivo foi justamente o ca�a North American P-51 Mustang, outra estrela da Segunda Guerra."
                    },
                    {
                        "type": "link",
                        "content": "https://revistaautoesporte.globo.com/Noticias/noticia/2018/07/dez-melhores-coisas-do-festival-de-velocidade-de-goodwood-em-video.html"
                    },
                    {
                        "type": "text",
                        "content": "O V8 Chevrolet j� foi utilizado por outras aeronaves, inclusive, um helic�ptero: o Vertical Hummingbird, vendido como kit e lan�ado em 1991. Por�m, o grande barato � ver um borbulhante oito cilindros embaixo do enorme �cap�� de um ca�a cl�ssico. Gravado em v�deo em, um Spitfire passa em rasante com um ru�do grave e caracter�stico. Um verdadeiro muscle plane, por assim dizer."
                    },
                    {
                        "type": "text",
                        "content": "Acompanha tudo de Autoesporte? Agora voc� pode ler as edi��es e mat�rias exclusivas no Globo Mais, o app com conte�do para todos os momentos do seu dia. Baixe agora!"
                    },
                    {
                        "type": "link",
                        "content": "https://globomais.com.br/"
                    }
                ]
            }
        },
