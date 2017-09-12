# 함께 이뤄가는 한국어 Part of speech tagging / Named enttiy recognition

현재 (2017.9.12) [soynlp project][soynlp]와 [customized_konlpy][ckonlpy]에서 파이썬 사용자들을 위한 한국어 자연어처리기를 개발 중에 있습니다. 

품사 사전이 풍부하게 구축되어 있을수록 품사 판별의 문제는 쉬워집니다. 

하나의 퓸사 사전에 여러 분야의 단어를 합쳐서 넣을 수도 있습니다. 하지만 모든 분야의 단어를 하나의 사전에 넣어도 어려움은 생깁니다.다른 분야에서 사용되는 예상하지 못한 단어들이 엉뚱한 품사로 판단될 수도 있습니다. 더 나아가서는 분석 텍스트에 적합한 사전, 품사 판별기의 세팅을 자동으로 맞추기 위해서도 분야별로 사전이 다르게 구축되어 있는 것은 도움이 될 것 입니다. 

이 repository에서 구축되는 언어자원은 soynlp project와 customized konlpy project에 연동할 예정입니다.


[soynlp]: https://github.com/lovit/soynlp
[ckonlpy]: https://github.com/lovit/customized_konlpy
