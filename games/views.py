import json
from django.http import JsonResponse
from django.db.models import Q

from games.models import GameScore

# Create your views here.
from django.views.generic import TemplateView

class MathFactsView(TemplateView):
    template_name = "math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "anagram-hunt.html"

class GameScoresView(TemplateView):
    template_name = "games/game-scores.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(GameScoresView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-created')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-created')
        return context
    
class LeaderBoardsView(TemplateView):
    template_name = "games/leader-boards.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(LeaderBoardsView, self).get_context_data(**kwargs)
        context['anagram_scores'] = GameScore.objects.filter(game__exact='ANAGRAM').order_by('-score')
        context['math_scores'] = GameScore.objects.filter(game__exact='MATH').order_by('-score')
        return context

def record_score(request):
    data = json.loads(request.body)

    user_name = data["user-name"]
    game = data["game"]
    settings = data["settings"]
    score = data["score"]

    new_score = GameScore(user_name=user_name, game=game, settings=settings, score=score)
    new_score.save()

    response = {
        "success": True
    }

    return JsonResponse(response)