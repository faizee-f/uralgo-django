from django.urls import path, include
from challenges.views import (
    ChallengeDetail,
    ChallengeList,
    TagManager,
    UserChallenge,
)


urlpatterns = [
    path("", ChallengeList.as_view(), name="view_challenges"),
    path("<int:pk>/", ChallengeDetail.as_view(), name="challenge_details"),
    path("my_challenges/", UserChallenge.as_view(), name="user_challenge"),
    path("tag_list", TagManager.as_view(), name="tag_list"),
]
