from rest_framework import serializers
from snippetApp import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES



class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields