# Análise de Defeitos em Soldas com CNN e Dataset RIAWELC

Este projeto utiliza o dataset **RIAWELC** como base para a criação e validação de um modelo de análise de defeitos em soldas. 

---

## Sobre o Dataset RIAWELC

O RIAWELC é um dataset de imagens radiográficas projetado para classificação de defeitos em soldas. Ele contém:
- **24.407 imagens** digitalizadas no formato `.png`.
- **Classes**: 
  - **LP**: Falta de penetração (Lack of Penetration).
  - **PO**: Porosidade (Porosity).
  - **CR**: Trincas (Cracks).
  - **ND**: Sem defeito (No Defect).

O dataset está disponível gratuitamente e foi descrito em:
- [RIAWELC: A Novel Dataset of Radiographic Images for Automatic Weld Defects Classification](https://www.researchgate.net/publication/369294451_RIAWELC_A_Novel_Dataset_of_Radiographic_Images_for_Automatic_Weld_Defects_Classification).
- [Repositório oficial no GitHub](https://github.com/stefyste/RIAWELC).

Se você utilizar o dataset, favor citar:
1. Benito Totino, Fanny Spagnolo, Stefania Perri, "RIAWELC: A Novel Dataset of Radiographic Images for Automatic Weld Defects Classification", ICMECE 2022, 6-7 Outubro, Barcelona, Espanha.
2. Stefania Perri, Fanny Spagnolo, Fabio Frustaci, Pasquale Corsonello, "Welding Defects Classification Through a Convolutional Neural Network", Manufacturing Letters, Elsevier.

---

## Detalhes do Nosso Modelo

Para este projeto, utilizamos uma **Convolutional Neural Network (CNN)** com **Transfer Learning** baseada na arquitetura **ResNet**. A abordagem de classificação foi adaptada para o nosso objetivo específico: detectar a presença ou ausência de defeitos (classificação binária). 

- **Escolha da Classificação Binária**: 
  - A decisão foi tomada considerando que nosso problema envolve radiografias completas, enquanto o dataset RIAWELC fornece imagens aproximadas.
  - A classificação binária foi pensada para simplificar a análise, mas resultou em um modelo enviesado devido à maior quantidade de imagens com defeito no dataset.

- **Resultados**:
  - Acurácia: **75%**
  - Problemas: O modelo mostrou viés para as classes com defeito.

- **Simulação de Análise de Radiografias Completas**:
  - Dividimos as radiografias completas em segmentos menores (similar às imagens do RIAWELC).
  - Cada segmento foi analisado individualmente, e os resultados foram combinados para avaliar a imagem completa.
  - Limitações: Radiografias completas podem incluir elementos extras, dificultando a análise e comprometendo a precisão.

---

## Pontos de Melhoria

1. **Adotar a Metodologia Original do RIAWELC**:
   - Utilizar as quatro classes (LP, PO, CR, ND) para uma classificação mais robusta.
2. **Explorar Outros Algoritmos**:
   - Testar abordagens como **Random Forest** ou **AdaBoost** para melhorar a generalização do modelo.
3. **Segmentação de Imagens**:
   - Implementar técnicas como **U-Net** ou **YOLO** para localizar e identificar com precisão os defeitos.
4. **Treinamento com Radiografias Completas**:
   - Coletar e treinar o modelo com radiografias completas para evitar simulações baseadas em outro dataset.

---

## Referências

1. [RIAWELC: A Novel Dataset of Radiographic Images for Automatic Weld Defects Classification - ResearchGate](https://www.researchgate.net/publication/369294451_RIAWELC_A_Novel_Dataset_of_Radiographic_Images_for_Automatic_Weld_Defects_Classification)  
2. [RIAWELC Dataset - GitHub](https://github.com/stefyste/RIAWELC)

---

Este trabalho representa um passo inicial no uso de machine learning para análise de soldas, com aprendizados importantes para aprimorar os modelos futuros. Feedbacks e sugestões são bem-vindos!
