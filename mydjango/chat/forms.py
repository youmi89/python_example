from django import forms
from chat.models import PuzzleRoom

# forms. Form : 입력 HTML Form과의 인터페이스
# 입력 폼 HTML 생성
# 유저가 입력한 값에 대해서 유효성 검사
# 유효성 검사에 통화한 값들을 정리해서. cleaned_data 사전으로 제공
# models.Model : 데이터베이스와의 인터페이스


# 상속(Inheritance) 문법
class PuzzleRoomForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        fields = "__all__"


# 수정방법
# 수정시에는 레벨만 수정토록 허용하고 싶다?
class PuzzleRoomEditForm(forms.ModelForm):
    class Meta:
        model = PuzzleRoom
        # 지정 모델의 지정 필드 내역만 읽어와서, 폼 필드 구성을 자동으로 해줘.
        # 유저는 level 필드만 입력 필드를 제공하고, 값을 변경 할수 있다.
        # 지정필드에 대해서만 수정을 허용
        fields = ["level"]
