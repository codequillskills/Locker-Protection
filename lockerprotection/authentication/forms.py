from django import forms
from .models import Data
import os

class FileUploadForm(forms.Form):
    fileName = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    fileUpload = forms.FileField(required=False)

    def clean_fileUpload(self):
        file = self.cleaned_data.get('fileUpload', False)
        if file:
            ext = os.path.splitext(file.name)[1]
            valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.txt']
            if not ext.lower() in valid_extensions:
                raise forms.ValidationError('Unsupported file extension.')
            if file.size > 1024*1024:
                raise forms.ValidationError('File size too large. The maximum file size allowed is 1MB.')
        return file
