# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:22:08 2024

@author: cmkkws
"""
## 1. 깃허브 관련 코드

# git init : 깃 저장소 생성(폴더 생성)
# git remote add origin 레파지토리주소 : 로컬 저장소와 원격 저장소 연결
# git status : 깃 상태 체크
# git add 파일명 : 변경된 파일들 트래킹
# git commit -m "메세지 명" : 이름
# git push origin master : 마스터 브런치 업로드

## 2. 깃허브와 내 pc remote 절차

'''
1. 코드를 작성할 git 폴더 생성
2. 생성한 폴더 우클릭, Open git bash here 클릭
3. 깃 처음 할때 설정할 것
   git config --global user.name(github name 입력)
   git config --global user.email(github email 입력)
4. 깃 생성코드 입력
   git init
5. 내 계정 github cloud 동기화
  git remote add origin(이름은 자유) "github url"
6. 만든 code 추가하기
 특정파일 : git add "파일 이름"
 전체파일 : git add .
7. commit 하기
 git commit -m '적고싶은 메모'
8. 내PC code 연동
 git push origin master
9.변경될 시, 6번부터 계속 반복!
 '''