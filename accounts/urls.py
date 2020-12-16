from .views import PostViewset, ProfileViewset, PostLikeViewset
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
# from django.conf import settings
# from django.conf.urls.static import static
from .views import RegisterAPI, LoginAPI, UserAPI, LoadMorePosts
from .views import MiniProfileViewset,ListProfileViewset
from .views import NoticeViewset, EventViewset,MiniListViewset,EventFiveViewset
from .views import RecommentViewset, CommentViewset,EventJoinViewset
from .views import FollowerViewset,FollowingViewset

from .views import MainListViewset
from .views import ProfileEmailViewset
from .views import PostSearchViewset, ProfileSearchViewset
from .views import GalleryViewset,ProfilePostViewset,ProfileLikeViewset
from .views import MiniGalleryViewset
from .views import ProfileConfirmViewset


router = routers.DefaultRouter()
router.register('posts', PostViewset)
router.register('profile', ProfileViewset)
router.register('notice', NoticeViewset)
router.register('event', EventViewset)


# 게스트북
router.register('miniprofile', MiniProfileViewset)
router.register('minilist', MiniListViewset)
router.register('listprofile', ListProfileViewset)


# 코멘트 리코멘트
router.register('comments', CommentViewset)
router.register('recomments', RecommentViewset)

# 쿼리
router.register('eventjoin', EventJoinViewset)
router.register('postlike', PostLikeViewset)

# 팔로워 팔로잉
router.register('follower', FollowerViewset)
router.register('following', FollowingViewset)

# 메인 리스트
router.register('mainlist', MainListViewset)

router.register('emailprofile', ProfileEmailViewset)
router.register('postsearch', PostSearchViewset)
router.register('profilesearch', ProfileSearchViewset)
router.register('gallery', GalleryViewset)

router.register('eventfive', EventFiveViewset)
router.register('profilelike', ProfileLikeViewset)
router.register('profilepost', ProfilePostViewset)

router.register('minigallery', MiniGalleryViewset)
router.register('confirm',ProfileConfirmViewset)

urlpatterns = [
    path('', include(router.urls)),
    path("auth/register/", RegisterAPI.as_view()),
    path("auth/login/", LoginAPI.as_view()),
    path("auth/user/", UserAPI.as_view()),
]

# urlpatterns += static('/accounts/', document_root=settings.MEDIA_ROOT)
