Criar função que receba uma representação no formato string de um tipo de refeição e um local.

Enviar a localização para o API de geocode do Google, para obter as coordenadas.

Enviar as coordenadas juntamente com o tipo de refeição para o API do Foursquare e salvar
o nome do local e o endereço, em seguida utilizar o ID do primeiro restaurante retornado
pelo API do Foursquare e enviar para o API de fotos do Foursquare e selecionar a primeira
opção na dimensão 300x300, caso contrário retornar um link de imagem qualquer.

Ao final a função deve exibir o nome do local, endereço e link da imagem do respectivo local
além de rtornar uma tupla contendo os valores retornados anteriormente
