# 20230516_THE_COMMUNITY_DREAM_PROJECT_BACK🌠

잠은 도대체 뭘까요?
<br/>
우리는 모두 하루 중 1/4 이상 잠을 잡니다.
<br/>
그렇지만 자신의 잠에 만족하는 현대인은 별로 없는 것 같습니다.
<br/>
누군가는 잠을 더 자고 싶어 고민하고, 누군가는 잠을 안 자고 싶어 고민하죠.
<br/>
고민이 고민으로 끝나지 않게, 여러 사람들과 경험담을 나누며 뾰족한 방법을 찾아봅시다.
<br/>
저희 dream 프로젝트가 여러분과 함께합니다.

![image](https://github.com/sodasora/dream/assets/127713314/8de383df-8823-49b2-ba55-ce9cdde15b5d) 
![image](https://github.com/sodasora/dream/assets/127713314/75166302-ec51-404f-b5bc-564696be43a4)
![image](https://github.com/sodasora/dream/assets/127713314/b31450c4-063c-47f8-841a-958645abf90c)
![image](https://github.com/sodasora/dream/assets/127713314/8551eccc-2a49-4c70-9fa8-ab194e330ef1)


## 📚 Stacks

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

## 🚩 Installation

`python manage.py makemigrations`, `python manage.py migrate`로 모델 생성 후
<br/>
구글 접속 > 브라우저 로그인 > 계정관리 > 보안 > 2단계 인증
> 앱 비밀번호 > 기타 > django로 앱 생성 > 기기용 앱 비밀번호 복사 > secret.json 파일 > email_password 자리에 넣기


secret.json 파일에
'''
{
    "SECRET_KEY": "장고 시크릿키",
    "EAIL": "이메일 인증 발송용 이메일",
    "EMAIL_PASSWORD": "구글에서 발급받은 기기용 앱 비밀번호 코드",
    "REST_API_KEY": "카카오 인증용 키",
}
'''

하고 터미널에 python manage.py runserver


## 💡 Features

1. 로그인, 회원 가입
    - 회원가입 기능
    - 로그인 기능
    - 로그아웃 기능
2. 게시글 CRUD
    - 게시글 작성 페이지(각 피드 페이지에서 가능)
        - 로그인한 사용자만 들어올수 있게!
    - 상세 게시글 페이지
        - 게시글의 세부내용 보기
        - 글 작성자만! 수정/삭제 가능하다
    - 댓글 작성
    - 대댓글 작성
    - 마이 페이지 (내가 작성한 게시글, 댓글 조회, 유저 및 게시글 상호작용 조회)

3. 유저 및 게시글 상호작용 기능
    -팔로잉/언팔로잉
    -북마크
    -게시글 좋아요

## 📋 Procedure
<br/>
-유저 기능
1. 홈페이지 방문 후 회원가입한다. (구글, 카카오, 사이트 회원가입 중 선택)
2. 이메일 인증 통과 필요
3. 회원로그인 후 게시글 작성 권한, 각종 상호작용 기능 권한 부여


- 게시글작성(게시판 3종: BOARD TO SLEEP, BOARD TO AWAKE, BOARD TO HEAL)
1. 사용자가 게시글을 조회
2. 사용자가 게시글 작성 버튼 클릭
3. 3가지 타입의 게시판 중 하나 선택하여 게시글 작성
4. 각 게시판은 해당 타입의 게시글만 모아서 띄운다

<br/>


 ## Team
 
 - https://github.com/sodasora
 - https://github.com/kimty9627
 - https://github.com/OCmonet
 - https://github.com/torigasuki
