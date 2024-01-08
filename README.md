## 머신러닝 기반 퀀트 포트폴리오 구성 - 산타랠리를 대상으로

### 주제 : 산타랠리에 맞는 포트폴리오 수립

#### 1. 국면 설정하기
+ 코스피와 CD금리 차트로 표시 

#### 2. 통계 검증 방식
+ 각 연도마다 일일수익률을 기준으로 a, b, c 집단에 대한 통계 검증을 진행

#### 3. 데이터 전처리
+ 시총과 재무 데이터 합치기
+ PEG 구하기
+ NCAV 구하기

#### 4. 각 연도마다 종목 선정 및 포트폴리오 수립
+ 연도마다 PEG값을 작은 순으로 정렬하고 추가적인 요소를 고려하여 성장주 종목 선정(최대 20)
+ 연도마다 NACV값을 큰 순으로 정렬하고 가치주 종목 선정(최대 20)
+ 연도마다 투자할 종목의 비중을 포트폴리오 전략을 통해 배분

#### 5. 국면에 따라 포트폴리오 전략 검증 및 수익률 비교
+ 최종적으로 만든 포트폴리오의 일일 수익률을 계산하기
+ 만든 포트폴리오로 통계 검증을 진행

#### 6. 결과
+ 각 국면마다 어떤 것들이 유의한지와 평균 수익률을 비교

*****

### Datasets
- datasets/시장금리(일별)_04194502.csv
	- 콜금리(1일), CD(91일), 국고채(1년) 
	- 1999.12.03 ~ 2022.01.28
	- 출처: ECOS

- datasets/kospi_cap_total.csv
	- 산타랠리 시작 전날(연말 6영업일) 시가총액 및 종목리스트
	- 2000 ~ 2023
	- pykrx, yfinance

- datasets/data.csv
	- PER, ..., 유동자산, 부채 등 재무데이터
	- 2000 ~ 2023
	- ts2000

- datasets/kospi_total.csv
	- kospi_cap_total.csv, data.csv 병합

- datasets/data_growth.csv
	- datasets/kospi_total.csv 전처리 후 PEG 전략 데이터만 추출
- datasets/data_value_low.csv
	- datasets/kospi_total.csv 전처리 후 LOW 전략 데이터만 추출
- datasets/data_value_ncav.csv
	- datasets/kospi_total.csv 전처리 후 NCAV 전략 데이터만 추출

*****

### Documents
[기획발표자료](https://docs.google.com/presentation/d/1vjd3hYQoOvpeZVV09vvSayqFNWzef-Y2/edit?usp=sharing&ouid=111847199610168823392&rtpof=true&sd=true)

*****

### References
[(Petal, 2023) The Santa Claus Rally in U.S. Stock Market Returns.](https://openurl.ebsco.com/EPDB%3Agcd%3A15%3A17783471/detailv2?sid=ebsco%3Aplink%3Ascholar&id=ebsco%3Agcd%3A163860960&crl=c)
