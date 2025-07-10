from django import forms
from .models import UserProfile

class EmotionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['emotion']
        widgets = {
            'emotion': forms.RadioSelect,  # 동그란 선택지
        }
        labels = {
            'emotion': '오늘 기분을 골라주세요',
        }

class ActivityLevelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['activity_level']
        widgets = {
            'activity_level': forms.RadioSelect
        }

class RegionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['region']
        widgets = {
            'region': forms.RadioSelect
        }
        labels = {
            'region': '',
        }