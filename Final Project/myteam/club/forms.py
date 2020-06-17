from django.forms import ModelForm, forms
from .models import Fixture, PlayerAvailability, PositionAssignment, Result, PlayerPerformance
from account.models import Club, Profile
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User


class CreateFixtureForm(ModelForm):
    class Meta:
        model = Fixture
        fields = ["date", "time", "opposition", "home_away", "venue", "competition"]
        labels = {
            "date": "Date:",
            "time": "Time:",
            "opposition": "Opposition:",
            "home_away": "Home/Away:",
            "venue": "Ground Location:",
            "competition": "Competition:",
        }


class EditFixtureForm(ModelForm):
    class Meta:
        model = Fixture
        fields = ["date", "time", "opposition", "home_away", "venue", "competition"]
        labels = {
            "date": "Date:",
            "time": "Time:",
            "opposition": "Opposition:",
            "home_away": "Home/Away:",
            "venue": "Ground Location:",
            "competition": "Competition:",
        }

class ResultForm(ModelForm):
    class Meta:
        model = Result
        exclude = ["fixture"]


class SelectTeamForm(ModelForm):
    class Meta:
        model = Fixture
        fields = ["selected_team"]

    def __init__(self, *args, **kwargs):
        super(SelectTeamForm, self).__init__(*args, **kwargs)

        x = PlayerAvailability.objects.filter(fixture=self.instance, availability='Available')

        self.fields['selected_team'].required = False
        self.fields['selected_team'].queryset = Profile.objects.filter(playeravailability__in=x)
        self.fields["selected_team"].widget = CheckboxSelectMultiple()
        self.fields["selected_team"].label = "Avilable Players (Check to Select Team):"


class PlayerAvailabilityForm(ModelForm):
    class Meta:
        model = PlayerAvailability
        fields = ["availability"]

class PositionAssignmentForm(ModelForm):
    class Meta:
        model = PositionAssignment
        fields = ["position"]

class PlayerPerformanceForm(ModelForm):
    class Meta:
        model = PlayerPerformance
        exclude = ["player", "fixture"]











