# NaverComic
python http client for Naver Webtoon service(http://comic.naver.com)

## How to use?
맨 아래줄의 `getPage(titleId, weekDay, max_pages)`를
 * `titleId` : 네이버 웹툰별 id
 * `weekDay` : 요일
 * `max_pages` : 1화에서 `max_pages`화까지 파싱

로 바꾸면 끝

### 예시 : 노네임드 파싱 결과
```
['http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_001.jpg', None, 'http://static.naver.net/m/comic/im/2012/bg_transparency.png', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_002.jpg', 'http://static.naver.net/m/comic/im/2012/bg_transparency.png', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_003.jpg', 'http://static.naver.net/m/comic/im/2012/bg_transparency.png', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_004.jpg', 'http://static.naver.net/m/comic/im/2012/bg_transparency.png', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_005.jpg', 'http://static.naver.net/m/comic/im/2012/bg_transparency.png', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_006.jpg', 'http://imgcomic.naver.com/mobilewebimg/460688/1/8d031f97349e0ceeec0ed280daf904c4_007.jpg', None]
[Finished in 1.03s]
```
## Notice
`bg_transparency.png`는 네이버 웹툰의 JPG 이미지 간격으로 쓰입니다. 해당 정규식 코드를 나중에 추가할 예정입니다.

## TODO list
* 웹툰 id 검색
* `bg_transparency.png` 정규식 코드 작성
* 에피소드 제목 출력
  * 특정 에피소드 제목
  * 전체 에피소드 제목

## License
```
The MIT License (MIT)

Copyright (c) 2016 BetaFish
```
