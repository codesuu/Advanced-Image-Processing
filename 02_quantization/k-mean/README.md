# Histogram Equalization / K-Means Clustering

## Abstract

## Introduction

### Histogram Equalization
히스토그램 평활화(equalization; 평준화, 균일화)는 이미지의 히스토그램을 사용해 대비를 조정하는 이미지 처리 방법이다[^1]. 이미지 히스토그램에서 특정영역에 값들이 집중되면, 이는 대비(contrast)가 나쁜 이미지라고 할 수 있다. 이를 전체 영역에 고루 퍼뜨림으로써, 전체 이미지의 대비를 개선할 수 있다.  
이론적으로 이미지의 각 픽셀에 대해 누적 분포 함수(Cumulative distribution function) 값을 계산하고 이를 $y' = y(max)$


### K-Means Clustering
수학과 디지털 신호 처리에서 양자화는 유한 집합에 대량의 입력값을 매핑하는 과정을 말한다.(예를 들어 반올림값을 정밀 단위로) 좀 더 구체적으로는 샘플링한 PAM신호(아날로그 데이터)를 이산적인 값(디지털 데이터)으로 바꾸어 표시하는 것을 말한다 [^10]. 즉, 이미지 처리 분야에서 이를 바라보면, 색상의 값을 이산적 혹은 더욱 이산적으로 변환하는 것을 의미한다. 

## REFERENCE
[^1]: https://en.wikipedia.org/wiki/Histogram_equalization

[^10]: https://ko.wikipedia.org/wiki/%EC%96%91%EC%9E%90%ED%99%94_(%EC%A0%95%EB%B3%B4_%EC%9D%B4%EB%A1%A0)

[https://ko.wikipedia.org/wiki/%EC%96%91%EC%9E%90%ED%99%94_(%EC%A0%95%EB%B3%B4_%EC%9D%B4%EB%A1%A0)](https://ko.wikipedia.org/wiki/%EC%96%91%EC%9E%90%ED%99%94_(%EC%A0%95%EB%B3%B4_%EC%9D%B4%EB%A1%A0))  
[K-Means Clustering in Python - Blog by Mubaris NK](https://mubaris.com/posts/kmeans-clustering/)