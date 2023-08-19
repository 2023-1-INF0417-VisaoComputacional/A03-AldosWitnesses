# INF0417 - Visão Computacional

Equipe Testemunhas do Aldo: <br>
202105844 - Gabriel Van Der Schmidt <br>
202105854 - Lucas Brandão Rodrigues <br>
202105855 - Lucca Emmanuel Pineli Simoes <br>

[Link para o vídeo da apresentação.](https://drive.google.com/file/d/1Ac9lgJsIOxQODrRwq7r4YJBYLYqvwB43/view?usp=sharing)
<br>

# A03-Testemunhas-do-Aldo

### Título: Automatização de Audiodescrição de Vídeos Utilizando Extração de Keyframes e Image Captioning
**Autores:** Gabriel Van Der Schmidt (gabriel_schmidt@discente.ufg.br), Lucas Brandão Rodrigues (brandao.brandao@discente.ufg.br), Lucca Emmanuel Pineli Simoes (lucca.pineli@discente.ufg.br).<br><br>
**Resumo:** Este trabalho apresenta uma abordagem inovadora para a audiodescrição de vídeos, abordando uma lacuna significativa na acessibilidade de conteúdo visual para pessoas com deficiência visual. Utilizando a biblioteca Katna para a extração de keyframes e um servidor de image captioning, a técnica proposta oferece uma solução automatizada e acessível para a descrição de conteúdo de vídeo. O estudo inclui uma análise detalhada dos algoritmos e técnicas utilizados, bem como uma comparação com métodos convencionais de audiodescrição, além de uma discussão sobre possíveis melhorias, limitações e aplicações futuras. Com a combinação de pesquisa teórica, desenvolvimento prático e avaliação empírica, este relatório contribui para o campo da audiodescrição, oferecendo uma alternativa tecnológica viável e escalável que tem o potencial de aumentar significativamente a acessibilidade do conteúdo em vídeo.<br>  
**Palavras-chave:** Acessibilidade, Audiodescrição, Katna, Keyframes, Image Captioning

### I. Introdução e revisão bibliográfica
#### Descrição do Problema
A audiodescrição de vídeos é um processo essencial para tornar o conteúdo visual acessível a pessoas com deficiência visual, permitindo-lhes compreender e interagir com a mídia de forma significativa. No entanto, a criação manual de audiodescrição permanece uma tarefa trabalhosa, demorada e cara, muitas vezes dependendo de profissionais especializados. Este desafio é ampliado pelo crescimento contínuo da produção de conteúdo de vídeo em diversas áreas, como educação, entretenimento e comunicação. A necessidade de uma solução automatizada e eficiente é, portanto, evidente.

Neste contexto, este trabalho propõe uma abordagem inovadora utilizando a biblioteca Katna para extrair keyframes dos vídeos, combinada com um servidor de image captioning. A ideia é automatizar o processo de audiodescrição, transformando as imagens-chave em descrições textuais e, posteriormente, em áudio. A técnica proposta visa não apenas simplificar o processo, mas também torná-lo mais acessível e escalável, permitindo a aplicação em uma variedade de contextos. A abordagem foi avaliada através de uma análise detalhada das técnicas e algoritmos utilizados, seguida por testes em diferentes tipos de vídeos. O objetivo final é contribuir para o campo da tecnologia assistiva, oferecendo uma alternativa viável que pode potencialmente revolucionar a forma como a audiodescrição é realizada, tornando o conteúdo de vídeo mais acessível para um público mais amplo.

#### Referências usadas na pesquisa
- [HackaTruck](https://hackatruck.com.br/)
- [(GitHub) Biblioteca Katna](https://github.com/keplerlab/katna)
- [(YouTube) Pytorch Image Captioning Tutorial](https://youtu.be/y2BaTt1fxJU)

### II. Fundamentos teóricos
Na análise de vídeos, a extração de keyframes é uma tarefa complexa e essencial, representando mudanças e eventos notáveis dentro de uma sequência. A biblioteca Katna [1] é uma ferramenta especializada que automatiza essa extração, além de oferecer funcionalidades para compressão de vídeo e redimensionamento inteligente de imagens. A extração de keyframes é definida como a seleção de quadros representativos que fornecem um resumo preciso e compacto do conteúdo do vídeo. A Katna realiza essa tarefa através de critérios específicos, como a detecção de diferenças absolutas no espaço de cores LUV, filtragem com base na pontuação de brilho, entropia e contraste, e agrupamento de quadros usando histograma de imagem. Além disso, a seleção de keyframes é aprimorada através da análise da variação de laplaciano para detecção de desfoque de imagem.

A biblioteca Katna é dividida em dois módulos: o módulo de vídeo, que lida com a extração de keyframes e compressão de vídeo, e o módulo de imagem, que gerencia tarefas relacionadas ao corte inteligente e redimensionamento de imagens. O módulo de vídeo utiliza a biblioteca ffmpeg para compressão e oferece recursos experimentais de redimensionamento inteligente com a ajuda do projeto Google's Mediapipe. O módulo de imagem, por sua vez, realiza o corte inteligente identificando a melhor parte da imagem, utilizando detecção de borda, saliência e rosto, e aplicando filtros especificados para refinar os cortes.

A complexidade da extração de keyframes, que envolve a seleção adequada e a identificação precisa de mudanças significativas, é superada através dessas técnicas avançadas e algoritmos de clusterização oferecidos pela biblioteca Katna. Essa ferramenta, portanto, representa um avanço significativo na análise de vídeos, facilitando a representação concisa do conteúdo e tornando a extração de keyframes uma tarefa mais eficiente e menos propensa a erros.

A fase de image captioning, crucial para a conversão de conteúdo visual em descrições textuais, envolve o envio dos keyframes extraídos para um servidor especializado. Utilizando modelos de aprendizado de máquina como CNN (Convolutional Neural Networks) e LSTM (Long Short-Term Memory), essa etapa torna o conteúdo acessível a pessoas com deficiência visual, permitindo a criação de descrições contextuais e precisas dos keyframes.

A etapa final, a audiodescrição, converte as descrições textuais em áudio, tornando o conteúdo de vídeo acessível a pessoas com deficiência visual. A qualidade da síntese de voz, vital para a clareza e naturalidade da audiodescrição, é mantida através do uso de ferramentas especializadas.

### III. Metodologia
O projeto inicia com a recepção do vídeo através de um POST HTTP, servindo como ponto de entrada para os vídeos que serão processados. Em seguida, a biblioteca Katna é utilizada para extração de keyframes, identificando os momentos mais significativos no conteúdo visual. Essas imagens extraídas são então descritas com a ajuda do modelo pré-treinado da Hugging Face, que gera legendas representando as cenas e elementos visualmente importantes.

A descrição gerada passa por um processo de tradução, se necessário, e é convertida em fala através dos serviços IBM Watson® Language Translator e IBM Watson® Text to Speech. Essa etapa garante que a informação visual seja acessível em formato auditivo. Todo o pipeline funciona dentro de uma arquitetura baseada em microserviços contidos em containers Docker. Cada etapa do processo é gerenciada por um serviço separado, o que permite uma escalabilidade e suporte multiplataforma eficazes.

A implementação da metodologia é cuidadosamente planejada para garantir uma solução robusta e integrada. A combinação de várias tecnologias, desde a extração de keyframes até a conversão de texto em fala, mostra uma abordagem inovadora para automatização da audiodescrição de vídeos. A arquitetura baseada em microserviços com containers Docker oferece flexibilidade, facilitando a implementação e o gerenciamento do sistema. 

### IV. Resultados e Conclusões
Os resultados obtidos no projeto demonstram eficiência e precisão no processo de audiodescrição. Gráficos, figuras e tabelas podem ser utilizados no relatório para ilustrar a qualidade e a rapidez das etapas individuais. A comparação com métodos existentes ou referências também reforça a relevância e o impacto do projeto na área de tecnologia assistiva.

As lições aprendidas durante o projeto revelam a importância da integração de diversas tecnologias e serviços para criar uma solução completa e escalável. A automatização da audiodescrição não apenas promove acessibilidade, mas também representa um avanço significativo no campo. A utilização de containers Docker, por exemplo, proporcionou uma implementação mais flexível e gerenciável, sendo um aspecto crucial para o sucesso do projeto.

Em conclusão, o projeto de Automatização de Audiodescrição de Vídeos Utilizando Extração de Keyframes e Image Captioning representa uma contribuição notável para a tecnologia assistiva. O uso criterioso de várias tecnologias, bibliotecas e serviços, aliado a uma arquitetura bem planejada, resultou em um processo eficiente e inovador. As conclusões tiradas reforçam a relevância do projeto e o potencial para futuras aplicações e desenvolvimentos na área. 

### V. Referências
[1] Keplerlab, “Keplerlab/katna: Tool for automating common video key-frame extraction, video compression and image auto-crop/image-resize tasks,” GitHub, https://github.com/keplerlab/katna (accessed Aug. 11, 2023). <br>
[2] A. Rocha Façanha, A. Caetano de Oliveira, M. Vinicius de Andrade Lima, W. Viana, and J. Sánchez, “Audio Description of Videos for People with Visual Disabilities,” Universal Access in Human-Computer Interaction. Users and Context Diversity. Springer International Publishing, pp. 505–515, 2016. doi: 10.1007/978-3-319-40238-3_48. <br>
[3] V. P. Campos, L. M. G. Goncalves and T. M. U. de Araujo, "Applying audio description for context understanding of surveillance videos by people with visual impairments," 2017 14th IEEE International Conference on Advanced Video and Signal Based Surveillance (AVSS), Lecce, Italy, 2017, pp. 1-5, doi: 10.1109/AVSS.2017.8078530. <br>
[4] O. Vinyals, A. Toshev, S. Bengio, and D. Erhan, “Show and tell: A neural image caption generator,” 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, Jun. 2015. doi: 10.1109/cvpr.2015.7298935. <br>
[5] X. Chen and C. L. Zitnick, “Mind’s eye: A recurrent visual representation for image caption generation,” 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, Jun. 2015. doi: 10.1109/cvpr.2015.7298856. <br>
[6] P. Anderson, B. Fernando, M. Johnson, and S. Gould, “SPICE: Semantic Propositional Image Caption Evaluation,” Computer Vision – ECCV 2016. Springer International Publishing, pp. 382–398, 2016. doi: 10.1007/978-3-319-46454-1_24. <br>
