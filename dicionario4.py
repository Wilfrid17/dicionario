# Exercícios

## 1. Identificando Locais de Risco

#Digamos que você está construindo um programa para identificar níveis de CO2 (gás carbônico) em determinados locais para evitar potenciais acidentes. Em cada um desses locais a sua empresa tem 5 sensores que captam o nível de CO2 do local.

#Os níveis normais de CO2 são em média 350. O nível de CO2 de um local é dado pela média captada pelos 5 sensores.

#Isso significa que se tivermos os 5 sensores do Rio de Janeiro marcando: 350, 400, 450, 350, 300, o nível de CO2 do Rio de Janeiro será dado por: (350 + 400 + 450 + 350 + 300) / 5 = 370.

#Caso o nível seja maior do que 450, um aviso deve ser exibido pelo seu programa dizendo, por exemplo: Rio de Janeiro está com níveis altíssimos de CO2 (490), chamar equipe especializada para verificar a região.

#Os resultados dos sensores são monitorados frequentemente e são dados para o sistema em forma de dicionário:

niveis_co2 = {
    'AC': [325,405,429,486,402],
    'AL': [492,495,310,407,388],
    'AP': [507,503,368,338,400],
    'AM': [429,456,352,377,363],
    'BA': [321,508,372,490,412],
    'CE': [424,328,425,516,480],
    'ES': [449,506,461,337,336],
    'GO': [425,460,385,485,460],
    'MA': [361,310,344,425,490],
    'MT': [358,402,425,386,379],
    'MS': [324,357,441,405,427],
    'MG': [345,367,391,427,516],
    'PA': [479,514,392,493,329],
    'PB': [418,499,317,302,476],
    'PR': [420,508,419,396,327],
    'PE': [404,444,495,320,343],
    'PI': [513,513,304,377,475],
    'RJ': [502,481,492,502,506],
    'RN': [446,437,519,356,317],
    'RS': [427,518,459,317,321],
    'RO': [517,466,512,326,458],
    'RR': [466,495,469,495,310],
    'SC': [495,436,382,483,479],
    'SP': [495,407,362,389,317],
    'SE': [508,351,334,389,418],
    'TO': [339,490,304,488,419],
    'DF': [376,516,320,310,518], 
}

for estado in niveis_co2:#para cada estado no dicionario niveis_co2
    qtde_sensores = len(niveis_co2[estado])# a quantidade de sensores é igual ao tamanho do dicionarioa do estado
    total_c02 = sum(niveis_co2[estado]) # o total de co2 é a soma dos valores do estado
    media_c02 = total_c02 / qtde_sensores # a media de co2 é o total de co2 dividido pela quantidade de sensores
    if media_c02 > 450: #se a media de co2 for maior que 450 
        print(f"{estado} está com níveis altíssimos de CO2 ({media_c02}), chamar equipe especializada para verificar a região.") #imprime o esta com niveis altissimos de co2 e amedia de co2
    
#A alternativa é gerar um código em Python que converse com a API do Vimeo (API é uma integração que as ferramentas abrem para programadores poderem fazer integrações dos seus próprios programas/scripts com a ferramenta).

video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}
#print(video)

#Agora com base no dicionário acima crie um código aqui:

for item in video: #para cada video no dicionario video
    print(item)# imprimir o item
    
print(video['download'][0]['link'])#imprimir o link do download.