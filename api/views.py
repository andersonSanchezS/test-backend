from rest_framework.decorators import api_view
from base.models import cities, divisions, teams, players, matches, positions
from .serializers import CitySerializer, DivisionSerializer, TeamsSerializer, PlayersSerializer, MatchesSerializer, PositionsSerializer
from django.http import JsonResponse
from django.core import serializers


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def citiesView(request, pk=None):

    if request.method == 'GET':
        data = cities.objects.all()
        serializer = CitySerializer(data, many=True)
        return JsonResponse({'data': serializer.data}, safe=False, status=200)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'PUT':
        data = cities.objects.get(pk=pk)
        serializer = CitySerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=200)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'DELETE':
        data = cities.objects.get(pk=pk)
        data.delete()
        return JsonResponse({'msg': 'city deleted'}, safe=False, status=200)

    else:
        return JsonResponse({'error': 'method not allowed'}, safe=False, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def divisionsView(request, pk=None):
    if request.method == 'GET':
        data = divisions.objects.all()
        serializer = DivisionSerializer(data, many=True)
        return JsonResponse({'data': serializer.data}, safe=False, status=200)

    elif request.method == 'POST':
        serializer = DivisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'PUT':
        data = divisions.objects.get(pk=pk)
        serializer = DivisionSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=200)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'DELETE':
        data = divisions.objects.get(pk=pk)
        data.delete()
        return JsonResponse({'msg': 'division deleted'}, safe=False, status=200)

    else:
        return JsonResponse({'error': 'method not allowed'}, safe=False, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def teamsView(request, pk=None):
    if request.method == 'GET':
        data = teams.objects.all()
        serializer = TeamsSerializer(data, many=True)
        return JsonResponse({'data': serializer.data}, safe=False, status=200)

    elif request.method == 'POST':
        serializer = TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_team = PositionsSerializer(
                data={'pj': 0, 'pg': 0, 'pe': 0, 'pp': 0, 'goals': 0, 'points': 0, 'teamId': serializer.data['id']})
            if new_team.is_valid():
                new_team.save()
            else:
                return JsonResponse({'error': new_team.errors}, safe=False, status=400)
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'PUT':
        data = teams.objects.get(pk=pk)
        serializer = TeamsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=200)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'DELETE':
        data = teams.objects.get(pk=pk)
        data.delete()
        return JsonResponse({'msg': 'team deleted'}, safe=False, status=200)

    else:
        return JsonResponse({'error': 'method not allowed'}, safe=False, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def playersView(request, pk=None):
    if request.method == 'GET':
        data = players.objects.all()
        serializer = PlayersSerializer(data, many=True)
        return JsonResponse({'data': serializer.data}, safe=False, status=200)

    elif request.method == 'POST':
        serializer = PlayersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'PUT':
        data = players.objects.get(pk=pk)
        serializer = PlayersSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=200)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)

    elif request.method == 'DELETE':
        data = players.objects.get(pk=pk)
        data.delete()
        return JsonResponse({'msg': 'player deleted'}, safe=False, status=200)

    else:
        return JsonResponse({'error': 'method not allowed'}, safe=False, status=400)


@api_view(['GET', 'POST', 'PUT'])
def matchesView(request, pk=None):
    if request.method == 'GET':
        data = matches.objects.all()
        serializer = MatchesSerializer(data, many=True)
        return JsonResponse({'data': serializer.data}, safe=False, status=200)

    elif request.method == 'POST':
        if request.data['team1'] == request.data['team2']:
            return JsonResponse({'error': 'home and away teams cannot be the same'}, safe=False, status=400)

        serializer = MatchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data['team1_score'] == request.data['team2_score']:
                team1 = positions.objects.get(teamId_id=request.data['team1'])
                team2 = positions.objects.get(teamId_id=request.data['team2'])
                team1Serializer = PositionsSerializer(team1, data={'teamId': request.data['team1'], 'pj': team1.pj + 1, 'pg': team1.pg, 'pe': team1.pe + 1,
                                                                   'pp': team1.pp, 'goals': team1.goals + request.data['team1_score'], 'points': team1.points + 1})
                team2Serializer = PositionsSerializer(team2, data={'teamId': request.data['team2'], 'pj': team2.pj + 1, 'pg': team2.pg, 'pe': team2.pe + 1,
                                                      'pp': team2.pp, 'goals': team2.goals + request.data['team2_score'], 'points': team2.points + 1})
                if team1Serializer.is_valid() and team2Serializer.is_valid():
                    team1Serializer.save()
                    team2Serializer.save()
                else:
                    return JsonResponse({'error': team1Serializer.errors}, safe=False, status=400)
            elif request.data['team1_score'] > request.data['team2_score']:
                team1 = positions.objects.get(teamId_id=request.data['team1'])
                team2 = positions.objects.get(teamId_id=request.data['team2'])
                team1Serializer = PositionsSerializer(team1, data={'teamId': request.data['team1'], 'pj': team1.pj + 1, 'pg': team1.pg + 1, 'pe': team1.pe,
                                                      'pp': team1.pp, 'goals': team1.goals + request.data['team1_score'], 'points': team1.points + 3})
                team2Serializer = PositionsSerializer(team2, data={'teamId': request.data['team2'], 'pj': team2.pj + 1, 'pg': team2.pg, 'pe': team2.pe,
                                                      'pp': team2.pp + 1, 'goals': team2.goals + request.data['team2_score'], 'points': team2.points})
                if team1Serializer.is_valid() and team2Serializer.is_valid():
                    team1Serializer.save()
                    team2Serializer.save()
                else:
                    return JsonResponse({'error': team1Serializer.errors}, safe=False, status=400)
            else:
                team1 = positions.objects.get(teamId_id=request.data['team1'])
                team2 = positions.objects.get(teamId_id=request.data['team2'])
                team1Serializer = PositionsSerializer(team1, data={'teamId': request.data['team1'], 'pj': team1.pj + 1, 'pg': team1.pg, 'pe': team1.pe,
                                                      'pp': team1.pp + 1, 'goals': team1.goals + request.data['team1_score'], 'points': team1.points})
                team2Serializer = PositionsSerializer(team2, data={'teamId': request.data['team2'], 'pj': team2.pj + 1, 'pg': team2.pg + 1, 'pe': team2.pe,
                                                      'pp': team2.pp, 'goals': team2.goals + request.data['team2_score'], 'points': team2.points + 3})
                if team1Serializer.is_valid() and team2Serializer.is_valid():
                    team1Serializer.save()
                    team2Serializer.save()
                else:
                    return JsonResponse({'error': team1Serializer.errors}, safe=False, status=400)
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)


@api_view(['GET'])
def positionsView(request):
    if request.method == 'GET':
        result = []
        for p in positions.objects.raw(
                r'select bp.*, bt.name as name from base_positions bp inner join base_teams bt on bt.id=bp."teamId_id" order by bp.points desc'):
            result.append({'name': p.name, 'pj': p.pj, 'pg': p.pg,
                          'pe': p.pe, 'pp': p.pp, 'goals': p.goals, 'points': p.points})
        return JsonResponse({'data': result}, safe=False, status=200)
