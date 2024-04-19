# Sparta Market
스파르타 코딩 클럽 Django 기초 주간 개인 과제

## 프로젝트 소개
Django를 사용하여 스파르타 마켓의 기본적이 기능을 구현하는 것으로, 상품에 대한 CRUD, 회원 기능, 프로필 등을 직접 구현하는 것입니다.

## 개발 기간
- 2024.04.12(금) ~ 2024.04.19(금)
- ERD 특강
- git, github 특강

## 개발 환경
- OS: window, ubuntu
- IDE: VSC
- Language: Python
- Github

## 기술 스택
- Django
- SQLite3
- bootstrap
- Git

## 주요 기능
1. 필수 기능
    - 회원 기능
        - 회원 가입
        - 로그인
        - 로그아웃

    - 유저 기능(프로필 페이지)
        - 프로필 페이지에는 username, 가입일, 내가 등록한 물품들을 볼 수 있어야 한다.
        - 프로필 페이지에는 내가 찜한 물건들의 목록이 보여야 한다.
        - 각 유저의 프로필 페이지에는 팔로우(follow) 할 수 있는 기능이 있고 팔로우, 팔로워가 몇 명인지 볼수 있어야 한다.

    - 게시 기능
        - 물건 목록을 볼 수 있는 페이지, 개별 물건에 대한 디테일 페이지가 있어야 한다.
        - 물건 조회 / 등록 / 수정 / 삭제가 포함되어야 한다.
        - 각 물건은 찜하기 기능이 있다.

2. 심화
    - 회원 기능
        - 개별 프로필 사진, 프로필 사진을 등록하지 않은 유저는 기본 프로필 사진이 등록된다.
    
    - 게시 기능
        - 각 물건에 찜수 / 조회수를 보이게 한다.
        - 인기도순, 최신순으로 정렬하는 기능을 추가한다, 인기도순은 찜한 횟수를 기준으로 하고 동일한 인기도라면 최신순으로 보여야 한다.


## ERD
![erd](https://github.com/Juunsik/spartamarket/blob/main/Task_image/erd.png)

## 화면 구성
- 메인 페이지
  ![main1](https://github.com/Juunsik/spartamarket/blob/main/Task_image/Task_main_1.png)
  ![main2](https://github.com/Juunsik/spartamarket/blob/main/Task_image/Task_main_2.png)

- 상세 페이지
  ![detail1](https://github.com/Juunsik/spartamarket/blob/main/Task_image/Task_detail_1.png)
  ![detail2](https://github.com/Juunsik/spartamarket/blob/main/Task_image/Task_detail_2.png)
  
- 프로필 페이지
  ![profile](https://github.com/Juunsik/spartamarket/blob/main/Task_image/Task_profile.png)
