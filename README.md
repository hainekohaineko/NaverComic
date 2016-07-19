# NaverComic
python http client for Naver Webtoon service(http://comic.naver.com)

## How to run
### \# 1
`pip install -r requirements.txt`

### \# 2
`index.py`의 맨 아래줄 `getPage(titleId, weekDay, max_pages)`를
 * `titleId` : 네이버 웹툰별 id
 * `weekDay` : 요일
 * `max_pages` : 1화에서 `max_pages`화까지 파싱

로 바꾸면 끝

### 예시 : 노네임드 파싱 결과
```
['http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_001.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_002.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_003.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_004.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_005.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_006.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_007.jpg']
[Finished in 1.01s]
```

## TODO list
* 웹툰 id 검색
* 에피소드 제목 출력
  * 특정 에피소드 제목
  * 전체 에피소드 제목

## Note
NaverComic is developed in Python 2.7.11

## License
```
The MIT License (MIT)

Copyright (c) 2016 BetaFish
```
