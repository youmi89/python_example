# baemin/models.py
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# 1측
class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # photo = models.FileField() 모든 파일 포멧 저장가능
    photo = models.ImageField()  # 이미지만


class Meta:
    ordering = ["-id"]


# def naldator_min_1(value):
#     """인자의 값이 1 이상이기를 기대합니다."""
#     if value <1:
#         raise ValidationError("값이 1이상이어야 한다.")

# def naldator_min_3(value):
#     """인자의 값이 3 이상이기를 기대합니다."""
#     if value <3:
#         raise ValidationError("값이 3이상이어야 한다.")


# 위 함수를 만들어주는 함수를 만들어보자 !!! <= JS에서도 활발히 사용되는 패턴.
def make_validator_min(min_value):
    def validator_func(value):
        if value < min_value:
            raise ValidationError(f"값이 {min_value}이상 이어야 합니다.")

        return validator_func


# validator_min_3 = make_validator_min(3)


# N 측에 1에 대한 외래키 필드를 추가
class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    # rating = models.IntegerField()  # 음수/양수 다 담을 수 있어요.
    # rating = models.PositiveIntegerField()   # 양수만 담을 수 있어요. 담을 수 있는 양수의 범위가 2배 커져요.
    rating = models.PositiveSmallIntegerField(
        # Validator : 입력된 값에 대한 유효성 검사를 수행해주는 다수의 함수
        # validators=[
        #     MinValueValidator(1),    # 가급적 장고 기본에서 지원하는 Validators를 최대한 활용해주세요.
        #     # make_validator_min(1),  # 함수가 함수를 생성한 버전
        #     MaxValueValidator(5),   # 클래스를 함수처럼 사용한 버전
        # ],
        # 선택지를 주겠다. => 반드시 이 값 중에 하나여야 한다.
        choices=[  # 모든 모델 필드에서 제공
            (1, "1점"),
            (2, "2점"),
            (3, "3점"),
            (4, "4점"),
            (5, "5점"),
        ],
        help_text="1점 ~ 5점 사이 점수를 주세요.",
    )

    # Review 쿼리셋에 대한 디폴트 정렬
    #  - Review 쿼리셋에서 order_by 를 지정하지 않으면, 자동으로 적용됩니다.
    class Meta:
        ordering = ["-id"]

    # 1 bit => 0 과 1을 표현 => 값을 2가지 표현 가능
    # 2 bit => 2 ** 2 => 총 4가지 표현 가능
    # 3 bit => 8가지
    # 4 bit => 16, 5 => 32, 6 => 64, 7 => 128, 8 => 256가지 숫자를 표현 가능.
    # 1 byte <= 8비트

    # 일반적인 숫자 변수는 4바이트(32비트)로 숫자를 표현. 물론 8바이트(64비트)로 표현도 해요.
