from django.shortcuts import redirect, reverse
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound

import os
from mimetypes import guess_type

from WebFolder.settings import IMAGE_FORMATS

def delete(path):
    ''' Delete file from <path>'''
    
    if os.path.isfile(path):
        try:
            os.remove(path)
            path, fileName = os.path.split(path)
            return redirect(reverse('folder-rendering') + ("?path='%s'" % (path)))
        
        except Exception as Err:
            return HttpResponseServerError
            
    return HttpResponseNotFound

def download(path):
    ''' Init download dialog on user side for downloading file from <path> '''
    
    if not os.path.isfile(path):
        return HttpResponseNotFound
    
    file = open(path,'rb')
    response = (HttpResponse(file.read()))
    
    if os.path.splitext(path)[1] in IMAGE_FORMATS:
        response['Content-Type'] = guess_type(path)[0]
    else:
        response['Content-Type'] = 'application/force-download'
    
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
    return response

def upload(path, file):
    ''' Save <file> to <path> '''

    if os.path.isdir(path):

            # set file.name as file.txt, file1.txt, file2.txt etc
        if os.path.isfile(os.path.join(path,file.name)):
            
            fileName, fileFormat = os.path.splitext(file.name)
            copyCounter = 1
            
            while os.path.isfile(os.path.join(path, '%s%s.%s' % (fileName, copyCounter, fileFormat))):
                copyCounter+=1
            
            file.name = '%s%s.%s' % (fileName, copyCounter, fileFormat)
        
            # save file
        with open(os.path.join(path, file.name), 'wb') as uploadedfile:
            uploadedfile.write(file.read())