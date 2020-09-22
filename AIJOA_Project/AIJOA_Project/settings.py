"""
Django settings for AIJOA_Project project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from gensim.models import FastText

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7024j&f3@3q#gz^n*b@h2v=kkgk54q*z31j+2(ty4skmh#6k*6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'AIJOA_App',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AIJOA_Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AIJOA_Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 'en-us'

TIME_ZONE = 'Asia/Seoul' # 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MODEL = FastText.load(r'C:\Users\NA\Desktop\Workspace\GJAI_WarmingUpProject\AIJOA_Project\wiki.ko\wiki_ko_v3.model')

MENULIST = {
        '폴더버거 핫키친':['골드버거 치킨','오늘도 봐봐 치킨','오늘도 보고 와 치킨','불도 먹었어 치킨',
                    '골드버거 핫치킨', '골드버거 치킨', '월드 보고 아침에', '오늘도 보고 와 치킨',
                    '폴더 버거 킹', '홀더 버거 치킨', '뭘 더 먹어 치킨', '너 먹어 치킨', '뭐 먹어 치킨'],
        '폴더버거 비프':['골드버그 비프', '올더 버거 비프', '폴더 버거 비프', '골드버그 비프 세트',
                '올더 버거 비프 세트', '어디서 먹어 핑크색', '물 더 먹어 비트 세트', '골드버그 비프 세트',
                '올 더 버거 비틀 세트', '홀더 버거 비프', '뭘 더 먹어 비프', '너 먹어 피프 세트',
                '뭐 먹어 비프'],
        '리아미라클버거':['리아미라클버거', '미아 미라클버거', '리아미라클버거 세트', '미라클버거 세트','리아 미라클 버거 세트'],
        '와규 에디션 투':['외규에디션 2', '마귀 에디션 2', '와규에디션 2', '와 귀신 전화', '월요일 좀 주세요 전화',
                    '와규에디션 2 세트', '와규에디션 2 세트', '목요일 샘플 세트'],
        '더블엑스투':['브렉시트', '더블엑스 2', '더블 X2 세트', '저번에 지출 세트', '버그 렉스필드 전화',
                '노래 치킨 세트', '더블 X2 세트', '더블엑스 풀세트', '더블엑스 두 세트'],
        '티렉스':['티렉스 버거', '티렉스 버거 세트', '티렉스버거세트', '티렉스버거 찾아',
            '티렉스 버거 세트 두 개', '티렉스버거세트 두 개'],
        '클래식 치즈버거':['클래식 치즈버거', '클래식 치즈버거 세트 하나', '클래식 치즈버거 틀어',
                    '클래식 치즈버거 세트', '클래식 치즈버거 세트 두 개'],
        '한우불고기':['한우 불고기', '한우불고기 세트 하나', '한우 불고기 집 전화', '한우 불고기 제주 TV',
                '한우불고기 두 개', '한우불고기 세트 두 개'],
        '모짜렐라 인 더 버거 베이컨':['모짜렐라인 더 버거', '모짜렐라인 더 버거 세트 하나',
                        '모짜렐라 인더버거 베트남', '모짜렐라인 더 버거 세트 두 개',
                        '모짜렐라인 더 버거 세트'],
        # '모짜렐라 in the 버거':['모짜렐라인 더 버거', '모짜렐라인 더 버거 세트 하나',
        #                    '모짜렐라 인더버거 베트남', '모짜렐라인 더 버거 세트 두 개',
        #                    '모짜렐라인 더 버거 세트'],
        # '모짜렐라 인 더 버거':['모짜렐라인 더 버거', '모짜렐라인 더 버거 세트 하나',
        #                    '모짜렐라 인더버거 베트남', '모짜렐라인 더 버거 세트 두 개',
        #                    '모짜렐라인 더 버거 세트'],
        '에이지버거':['az버거', 'az버거 세트', '에이지버거', '에이지버거 세트', '아재버거', '아재버거 세트 하나', '거제도 가서 찾아',
                '아재 동생 두 개', '아재버거세트 두 개', '아재버거 세트 두 개'],
        'az버거':['az버거', 'az버거 세트', '에이지버거', '에이지버거 세트', '아재버거', '아재버거 세트 하나', '거제도 가서 찾아',
                '아재 동생 두 개', '아재버거세트 두 개', '아재버거 세트 두 개'],
        '에이제트버거':['az버거', 'az버거 세트', '에이제트버거', '에이제트버거 세트', '아재버거', '아재버거 세트 하나', '거제도 가서 찾아',
                '아재 동생 두 개', '아재버거세트 두 개', '아재버거 세트 두 개'],
        '원조 빅불':['원조빅불', '원조빅불 세트', '원조빅불세트', '언제 도착하나', '물제 를 풀 세트',
                '원조 빅불 세트', '오늘 이불세트'],
        '핫크리스피버거':['핫크리스피버거', '하트스피가방', '핫크리스피버거 세트', '크리스피 버거 세트',
                '핫 크리스피버거 세트', '하트 스트커 세트'],
        '불고기버거':['불고기 버거', '불고기 버거 세트 하나', '불고기 버거 세트', '불고기버거 세트 두 개'],
        '데리버거':['데리버거', '데리버거 세트 하나', '데리버거 찾아', '데리버거 두 개', '데리버거 세트 두 개',
                '데리버거세트 두 개'],
        '치킨버거':['치킨버거', '치킨 먹어', '치킨 버거 세트', '치킨 먹었다', '치킨 먹어서 두 개',
                '치킨 버거 세트 두 개'],
        '새우버거':['새우버거', '재봉 설탕', '새우버거 세트', '일본어 태어나', '여보 가서 켜',
                '새우버거 속']
    }