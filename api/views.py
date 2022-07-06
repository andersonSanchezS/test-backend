from rest_framework.decorators import api_view
from base.models import cities, divisions, teams, players, matches, positions
from .serializers import CitySerializer, DivisionSerializer, TeamsSerializer, PlayersSerializer, MatchesSerializer, PositionsSerializer
from django.http import JsonResponse


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
        serializer = MatchesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'data': serializer.data}, safe=False, status=201)
        return JsonResponse({'error': serializer.errors}, safe=False, status=400)
