from django.shortcuts import render, get_object_or_404, redirect
from account.models import Club, Profile
from account.forms import RegisterClubForm
from .forms import CreateFixtureForm, SelectTeamForm, PlayerAvailabilityForm, EditFixtureForm, PositionAssignmentForm, ResultForm, PlayerPerformanceForm
from .models import Fixture, PlayerAvailability, PositionAssignment, PlayerPerformance, Result
from django.contrib import messages
from django.forms import formset_factory, inlineformset_factory, modelformset_factory
from django.db.models import Avg, Count, Min, Sum


# Create your views here.

def clubs(request):
    context = {
        'title': "All Clubs",
        'heading': "MyTeam Club Search",
        'clubs': Club.objects.all(),
    }
    if request.method == "POST":
        user_input = request.POST.get("club")
        if Club.objects.filter(name=user_input):
            club = Club.objects.get(name=user_input)
            return redirect("club_details", club.id)
        else:
            messages.warning(request, "Sorry - there is no club with that name at MYTEAM.")
    return render(request, "clubs.html", context)

def club_details(request, club_id):
    club = get_object_or_404(Club, id=club_id)

    context = {
        'title': "Club Details",
        'club': club,
        'players': club.players.all(),
    }

    return render(request, "clubdetails.html", context)

def club_squad(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    players = club.players.all()

    player_performances = PlayerPerformance.objects.filter(player__in=players)

    for player in players:
        player.games = PlayerPerformance.objects.filter(player=player).aggregate(Sum('appearances'))['appearances__sum']
        player.goals = PlayerPerformance.objects.filter(player=player).aggregate(Sum('goals'))['goals__sum']
        player.assists = PlayerPerformance.objects.filter(player=player).aggregate(Sum('assists'))['assists__sum']
        rating = PlayerPerformance.objects.filter(player=player).aggregate(Avg('rating'))['rating__avg']
        if not rating == None:
            player.rating = str(round(rating, 1))
        else:
            player.rating = 'N/A'


    # .aggregate(Sum('goals_for'))['goals_for__sum']

    context = {
        'title': "Club Details",
        'club': club,
        'players': players,
    }
    return render(request, "squad.html", context)

def club_fixtures(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    fixtures = Fixture.objects.filter(club=club)


    context = {
        'title': "Club Fixtures",
        'club': club,
        'form': CreateFixtureForm(),
        'fixtures': fixtures,

    }



    if request.method == 'POST':
        form = CreateFixtureForm(request.POST)
        if form.is_valid():
            fixture = form.save(commit=False)
            fixture.club = club
            fixture.save()
            return render(request, "clubfixtures.html", context)

    return render(request, "clubfixtures.html", context)

def add_fixture(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Club Fixtures",
        'heading': f"Add Fixture for {club.name}",
        'club': club,
        'form': CreateFixtureForm(),
    }
    if request.method == 'POST':
        form = CreateFixtureForm(request.POST)
        if form.is_valid():
            fixture = form.save(commit=False)
            fixture.club = club
            fixture.save()
            return redirect("club_fixtures", club_id)

    return render(request, "addfixture.html", context)


def player_registration(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Player Registration",
        'heading': "Join a team",
        'summary': "This is where a player can join a team if they have the password.",
        'club': club,
    }

    return render(request, "playerregistration.html", context)

def join_club(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    if request.user.profile in club.players.all():
        messages.warning(request, "You are already a member of this club.")
        return redirect("club_details", club.id)
    context = {
        'title': "Player Registration",
        'heading': f"Join {club.name}",
        'summary': "Enter the password you have been sent by the manager below.",
        'club': club,
    }
    if request.method == "POST":
        user_input = request.POST.get("password")
        if user_input == club.password:
            club.players.add(request.user.profile)
            messages.warning(request, f"Congratulations! You have joined {club.name}!")
            return redirect("club_details", club.id)
        else:
            messages.warning(request, f"Incorrect password for {club.name}. Contact manager {club.manager.first_name} {club.manager.last_name} for the correct password.")

    return render(request, "joinclub.html", context)

def edit_club_details(request, club_id):
    instance = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Edit Club Details",
        'heading': f"Edit Club Details for {instance.name}",
        'club': instance,
        'form': RegisterClubForm(request.POST or None, instance=instance)
    }
    if request.method == 'POST':
        form = RegisterClubForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("club_details", instance.id)
    return render(request, "editclubdetails.html", context)


def edit_fixture(request, club_id, fixture_id):
    instance = get_object_or_404(Fixture, id=fixture_id)
    club = get_object_or_404(Club, id=club_id)
    context = {
        'title': "Edit Fixture Details",
        'heading': f"Edit Details for {instance.club.name} vs. {instance.opposition} - {instance.date}",
        'club': club,
        'fixture': instance,
        'form': EditFixtureForm(request.POST or None, instance=instance)
    }
    if request.method == 'POST':
        form = EditFixtureForm(request.POST, instance=instance)
        if form.is_valid():

            fixture = form.save(commit=False)
            form.save_m2m()
            fixture.club = club
            fixture.save()

            return redirect("club_fixtures", club_id)
    return render(request, "editfixturedetails.html", context)


def select_team(request, club_id, fixture_id):
    instance = get_object_or_404(Fixture, id=fixture_id)
    club = get_object_or_404(Club, id=club_id)

    context = {
        'title': "Team Selection",
        'heading': f"Team Selection:\n\n {instance.club.name} vs. {instance.opposition} - {instance.date}",
        'club': club,
        'fixture': instance,
        'form': SelectTeamForm(request.POST or None, instance=instance),
        'availability_declarations': PlayerAvailability.objects.filter(fixture=instance),
    }
    if request.method == 'POST':
        form = SelectTeamForm(request.POST, instance=instance)
        if form.is_valid():

            fixture = form.save(commit=False)
            form.save_m2m()
            fixture.club = club
            fixture.save()

            return redirect("club_fixtures", club_id)
    return render(request, "selectteam.html", context)


def tactics(request, club_id, fixture_id):
    fixture = get_object_or_404(Fixture, id=fixture_id)
    club = get_object_or_404(Club, id=club_id)
    players = fixture.selected_team.all()

    for player in players:
        position_assignment, created = PositionAssignment.objects.get_or_create(fixture=fixture, player=player)

    position_assignment_formset = modelformset_factory(PositionAssignment, form=PositionAssignmentForm, extra=0)
    formset = position_assignment_formset(queryset=PositionAssignment.objects.filter(fixture=fixture, player__in=players))

    context = {
        'title': "Postion Assignments",
        'formset': formset,
        'club': club,
        'fixture': fixture,
        'positions': PositionAssignment.objects.filter(fixture=fixture)
    }

    if request.method == 'POST':
        formset = position_assignment_formset(request.POST, queryset=PositionAssignment.objects.filter(fixture=fixture, player__in=players))
        formset.save()
        return redirect("tactics", club_id, fixture_id)

    return render(request, "tactics.html", context)



def cancel_fixture(request, club_id, fixture_id):
    fixture = get_object_or_404(Fixture, id=fixture_id)
    fixture.delete()
    return redirect("club_fixtures", club_id)


def post_match_stats(request, club_id, fixture_id):
    fixture = get_object_or_404(Fixture, id=fixture_id)
    club = get_object_or_404(Club, id=club_id)
    players = fixture.selected_team.all()
    result, created = Result.objects.get_or_create(fixture=fixture)

    for player in players:
        player_performance, created = PlayerPerformance.objects.get_or_create(fixture=fixture, player=player)

    player_performance_formset = modelformset_factory(PlayerPerformance, form=PlayerPerformanceForm, extra=0)
    formset = player_performance_formset(queryset=PlayerPerformance.objects.filter(fixture=fixture, player__in=players))

    context = {
        'title': "Player Performances",
        'formset': formset,
        'club': club,
        'fixture': fixture,
        'form': ResultForm(request.POST or None, instance=result),
        'performances': PlayerPerformance.objects.filter(fixture=fixture)
    }

    if request.method == 'POST':

        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            result = form.save(commit=False)
            form.save_m2m()
            result.fixture = fixture
            result.save()
        formset = player_performance_formset(request.POST, queryset=PlayerPerformance.objects.filter(fixture=fixture, player__in=players))
        formset.save()
        return redirect("club_fixtures", club_id)

    return render(request, "postmatchstats.html", context)


def results (request, club_id):
    club = get_object_or_404(Club, id=club_id)
    fixtures = Fixture.objects.filter(club=club)
    results = Result.objects.filter(fixture__in=fixtures)
    played = Result.objects.filter(result='Win')
    context = {
        'title': "Results",
        'club': club,
        'results': results,
        'played': Result.objects.filter(fixture__in=fixtures).count(),
        'won': Result.objects.filter(fixture__in=fixtures, result='Win').count(),
        'lost': Result.objects.filter(fixture__in=fixtures, result='Lose').count(),
        'drawn': Result.objects.filter(fixture__in=fixtures, result='Draw').count(),
        'gf': Result.objects.filter(fixture__in=fixtures).aggregate(Sum('goals_for'))['goals_for__sum'],
        'ga': Result.objects.filter(fixture__in=fixtures).aggregate(Sum('goals_against'))['goals_against__sum'],
    }
    return render(request, "results.html", context)

















def player_availability(request, club_id):
    club = get_object_or_404(Club, id=club_id)
    fixtures = club.fixture_set.all()
    for fixture in fixtures:
        match_availability, created = PlayerAvailability.objects.get_or_create(fixture=fixture, player=request.user.profile)

    player_availability_formset = modelformset_factory(PlayerAvailability, form=PlayerAvailabilityForm, extra=0)
    formset = player_availability_formset(queryset=PlayerAvailability.objects.filter(fixture__in=fixtures, player=request.user.profile))

    context = {
        'title': "Availability Declarations",
        'summary': "Indicate which matches you are available for...",
        'formset': formset,
        'club': club,
        'fixtures': fixtures,

    }

    if request.method == 'POST':
        formset = player_availability_formset(request.POST, queryset=PlayerAvailability.objects.filter(fixture__in=fixtures, player=request.user.profile))
        formset.save()
        return redirect("profile")




    return render(request, "playeravailability.html", context)














