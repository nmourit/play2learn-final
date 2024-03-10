from django.urls import path

from games.views import MathFactsView, AnagramHuntView, GameHistoryView, LeaderBoardsView, record_score

app_name = 'games'
urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('game-history/', GameHistoryView.as_view(), name='game-history'),
    path('leader-boards/', LeaderBoardsView.as_view(), name='leader-boards'),
]