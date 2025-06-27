# baemin/views.py
from urllib import request

from django.contrib import messages
from django.http import HttpRequest, HttpResponse

# from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Shop, Review
from .forms import ReviewForm


class ShopListView(ListView):
    model = Shop
    paginate_by = 3

    # 아래 설정이 디폴트 설정
    # template_name = "baemin/shop_list.html"
    # 요청에 따라, 사용하는 템플릿을 변경해봅시다.

    # 부모 클래스의 get_template_names 메서드를 재정의 (override)
    def get_template_names(self):
        # 클래스 기반 뷰는 현재 요청 객체 : self.request
        if "naked" in self.request.GET:  # dict에서 해당 Key가 사전에 있는 지만 확인
            # 무한스크롤에서 다음 페이지 내용이라면?
            return "baemin/_shop_list.html"  # !!!

        # 아래의 코드는 원래 메서드의 기본 동작을 수행
        return super().get_template_names()


# 클래스를 통해서 새로운 뷰 함수를 생성을 합니다.
shop_list = ShopListView.as_view()  # 코드라기보다, 설정에 가까운 코드.
# # 최신의 가게 목록 페이지를 보여줄 거예요.
# #  - 최신의 데이터는 DB 안에 있죠. 그러니 매번 DB 조회를 할 겁니다.
# def shop_list(request):
#     # 데이터베이스에서 baemin_shop 테이블의 모든 레코드를
#     # 조회할 준비 (아직 데이터를 가져오진 않았습니다.)
#     qs = Shop.objects.all()  # QuerySet
#     #  qs = qs.order_by('-id')

#     # page = 1
#     page = request.GET.get( ket: "page", default:1)
#     paginate_by = 5

#     # qs = qs[0:5]
#     # qs = qs[5:10]
#     # qs = qs[10:15]

#     start_index = page - 1
#     end_index = page * paginate_by
#     qs = qs[srart_index:end_index]

#     return render(
#         request,
#         template_name="baemin/shop_list.html",
#         context={
#             "shop_list": qs,
#         },
#     )


# TODO: baemin/shop_list.html 템플릿을 만들어보기. 하얀 배경도 OK. chatgpt 등을 통한 코드 생성도 OK.


def shop_detail(request, pk):
    # DB에서 조회했습니다.
    shop = get_object_or_404(Shop, pk=pk)  # 이 필드명 지정이 좀 더 정확한 네이밍.
    # shop = Shop.objects.get(id=pk)  # 위와 동일한 동작

    # 정렬 (sort) : 정렬 기준으로 2개 이상 둘 수도 있습니다.
    # 각 정렬은 오름차순, 내림차순을 지정할 수 있어요.
    # 그런데, 가급적 정렬 기준 컬럼은 1개만 지정하시기를 권장드립니다.
    #  - 데이터가 적으면 (몇 천개) 아무 상관없습니다.
    #  - 데이터베이스 정렬을 요청받으면, 정렬을 모두 한 후에 정렬된 목록을 응답하죠.
    #    정렬 기준이 여러 개면, 정렬을 여러번 하면 그 만큼 시간이 오래 걸립니다.
    #  - 대개의 경우, 정렬은 1개 기준이면 충분.

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)

    # 정렬을 지정하지 않아도 출력은 된다 지정하지 않으면 오름차순인가?- NO!!
    #  - 저장된 순서대로 조회 될 뿐이다.
    #  - 조회할때마다 다른 순서로 조회가 둘수도 있다

    # 정렬을 지정하면, 항상 일관된 순서로 조뢰가 된다.
    # review_qs = review_qs.order_by("-id")  # id 필드 내림차순
    # review_qs = review_qs.order_by("id") # id 필드 오름차순

    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "review_list": review_qs},
    )


def review_new(request, shop_pk):
    # shop = Shop.objects.get(
    #     pk=shop_pk)  # form 시작할 때, 지정 pk의 Shop의 존재 유무를 확인.
    shop = get_object_or_404(shop, pk=shop_pk)

    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():  # 유효성 검사 수행 !!!

            # commit=False 를 지정해서, form.save 내부에서 model.save 가 호출되지 않도록.
            unsaved_review: Review = form.save(
                commit=False
            )  # 입력받은 폼 필드 값으로 데이터베이스로의 저장을 시도 !!!
            unsaved_review.shop = shop  # Shop Instance
            unsaved_review.save()

            # 한국어를 쓰는 사람을 대상으로만 하는 서비스니까, 메시지는 한국어로 쓰셔도 됩니다.
            # 만약 영어 등 다국어를 지원해야한다면, 메시지를 쓰는 방법이 조금 달라요.
            messages.success(request, messages="고객님의 리뷰에 감사드립니다. ;")
            # 위 메시지는 요청을 한 유저에게만 보여질 거예요.

            next_url = f"/baemin/{shop_pk}/"
            return redirect(
                next_url
            )  # django view 함수에서만 씁니다. 브라우저에게 이 주소로 이동하세요.

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )


def review_edit(request, shop_pk, pk):
    # 모델클래스.object => Model Manager
    # .all
    # .get
    # .filter
    # .exclude
    # .order_by

    # 지정 조건의 레코드가 DB에 없을 때 Review.DoesNotExist 예외가 발생합니다.
    # try:
    #     review = Review.objects.get(pk=pk)  # 지정 조건의 레코드가 데이터베이스가 1개 있어야 한다.
    # except Review.DoesNotExist:
    #     raise Http404

    review = get_object_or_404(Review, pk=pk)

    if request.method == "GET":
        form = ReviewForm(instance=review)

    else:
        form = ReviewForm(instance=review, data=request.POST, files=request.FILES)
        if form.is_valid():  # 유효성 검사 수행 !!!
            # 리뷰 수정 시에는 ReviewForm 클래스 안에서 정의된 필드에 대해서만 저장되어도 OK.
            form.save()
            messages.success(request, "리뷰가 수정되었습니다. ;)")

            next_url = f"/baemin/{shop_pk}/"
            return redirect(
                next_url
            )  # django view 함수에서만 씁니다. 브라우저에게 이 주소로 이동하세요.

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )


# 장고 스타일의 삭제 방식
#  1) GET 요청 : 삭제를 요청했을 때 -> 확인 과정을 거칩니다. (정말 삭제하시겠습니까?)
#  2) POST 요청 : 삭제 확인 (confirm) -> 삭제를 합니다.
def review_delete(request: HttpRequest, shop_pk: int, pk: int) -> HttpResponse:
    if request.method == "GET":
        return render(request, template_name="baemin/review_confirm_delete.html")
    Review = get_object_or_404(Review, pk=pk)
    Review.delete()  # 데이터베이스에서 호출 즉시 삭제 됩니다.

    messages.success(request, "지정 리뷰를 삭제했습니다.")

    shop_url = f"/baemin/{shop_pk}/"
    return redirect(shop_url)
