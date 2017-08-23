from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect

import os
from .common import file_actions as file

from .settings import ROOT_DIR, BASE_DIR

def pathChecker(fun):
    ''' Decorator. 
        - Remove quotes in path if need
        - redirect if path wrong'''
    
    def inner(request):
        
        path = request.GET.get('path', ROOT_DIR)
    
            # if path not BASE_DIR, remove url parameter quotes
        if path != ROOT_DIR:
            path = path[1:-1]
            
            # path should start as BASE_DIR AND shouldn't be the project folder
        if not path.startswith(ROOT_DIR) or os.path.normpath(BASE_DIR) in os.path.normpath(path):
            return redirect('folder-rendering')
        
        return fun(request, path)
        
    return inner

@pathChecker
def fileDelete(request, path=BASE_DIR):
    ''' Initiate dialog to delete file from <path>,
        <path> get from decorator'''
    
        # redirect to folder-rendering if not file
    if not os.path.isfile(path):
        return redirect('folder-rendering')
    
        # delete file if confirm delete from dialog
    if request.GET.get('confirm', ROOT_DIR)=='yes':
        return file.delete(path)
    
        # start dialog for delete file (yes/no)
    fullPath = path
    path, fileName = os.path.split(path)
    return render(request, 'file_dialog_delete.html', {'path': path,
                                                       'fileName': fileName,
                                                       'fullPath': fullPath,
                                                       })

@pathChecker
def fileDownload(request, path=BASE_DIR):
    ''' Initiate download file from <path>,
        <path> get from decorator'''
    
    return file.download(path)

@pathChecker
def fileUpload(request, path=BASE_DIR):
    ''' Upload file to path,
        <path> get from decorator'''
    
      # file upload
    if request.method == 'POST':
        if 'file_upload' in request.FILES.keys():
            file_upload = request.FILES['file_upload']
            file.upload(path, file_upload)
    
    return folderRender(request)

@pathChecker
def folderRender(request, path=BASE_DIR):
    ''' Render folder from request,
        <path> get from decorator'''
    
        # get filename if file
    if os.path.isfile(path):
        path, fileName = os.path.split(path)
    else:
        fileName = None
    
    return render(request, 'folder.html', {'path': path,
                                           'fileName': fileName,
                                           })