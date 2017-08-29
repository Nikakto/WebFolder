from django import template
from django.template.loader import get_template

import os

from WebFolder.settings import ROOT_DIR, IMAGE_FORMATS

register = template.Library()

@register.simple_tag()
def drawFolderContent(request, path):
    ''' Rendering content of folder <path> '''
    
    if not os.path.exists(path):
        return 'Wrong path %s' % (path)
    
    if not os.path.isdir(path):
        return 'Cannot get folder contents'
        
    folderContent = []
    content = os.listdir(path)
    
    for item in content:
        
        image = False
        
        if os.path.isfile(os.path.join(path,item)):
            size = os.path.getsize(os.path.join(path,item))
            size = round(size/1024,2)
            
                # check format in image formats
            if os.path.splitext(item)[1] in IMAGE_FORMATS:
                image = True
            
        else:
            size = None
            
        folderContent.append((item, size, image))
            
    return get_template('folder_content.html').render({'request': request,
                                                       'path': path,
                                                       'folderContent': folderContent,
                                                       })
            
@register.simple_tag()
def drawFolderContentPath(path):
    ''' Rendering path to folder as links to each subfolders'''
    
    if not os.path.exists(path):
        return 'Wrong path %s' % (path)
    
    pathFolders = []
    pathPart = path
    
        # get path for all folders in path
    while os.path.normpath(pathPart) != os.path.normpath(ROOT_DIR):
        
        pathFolders.append( (os.path.basename(pathPart), pathPart) )
        pathPart = os.path.dirname(pathPart)
        
    pathFolders.append( (ROOT_DIR, ROOT_DIR) )
    pathFolders.reverse()
    
    return get_template('folder_content_path.html').render({'path': path,
                                                           'pathFolders': pathFolders,
                                                           })

@register.simple_tag()
def drawSelected(path, fileName):
    ''' Rendering menu and information about <fileName> from <path>'''
    
    if not fileName:
        return ''
    
    fullPath = os.path.join(path, fileName)
    fileSize = round(os.path.getsize(fullPath)/1024,2)
    if os.path.isfile(fullPath):
        return get_template('selected.html').render({'path': fullPath,
                                                    'fileName': fileName,
                                                    'fileType': os.path.splitext(fileName)[1],
                                                    'fileSize': fileSize,
                                                    })