Criar função que receba uma representação no formato string de um tipo de refeição e um local.

Enviar a localização para o API de geocode do Google, para obter as coordenadas.

Enviar as coordenadas juntamente com a representação do tipo de refeição para o API do
Foursquare e salvar o nome e o endereço do primeiro local, em seguida utilizar
o ID do primeiro restaurante retornado pelo API do Foursquare e enviar para o API de
fotos do Foursquare e selecionar a primeira imagen na dimensão 300x300, caso contrário
retornar um link de uma imagem qualquer.

Ao final a função deve exibir o nome do local, endereço e link da imagem do respectivo local
além de rtornar uma tupla contendo os valores retornados anteriormente
