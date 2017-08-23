function onLoad() {
    // resize canvas to table size
    
    canvas = document.getElementById("folder_canvas");
    rectangle_folder_content = document.getElementById("rectangle_folder_content");
    canvas.width = rectangle_folder_content.offsetWidth;
    canvas.height = rectangle_folder_content.offsetHeight;
}

function clearCanvas(event) {
    // clear canvas

    canvas = document.getElementById("folder_canvas");
    var ctx = canvas.getContext('2d');
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawImage(canvas, image, x, y) {
    // draw preview image on canvas

    var context = canvas.getContext('2d');
    
        // image too big
    if (image.width > 200 || image.height > 200) {
    
        ratio = image.width/image.height;
        
            //resize with saving ration
        if (image.width > image.height) {
            image.width = 200;
            image.height = image.width/ratio;
        }
        else {
            image.height = 200;
            image.width = image.height*ratio;
        }
    }
    
        // check image not going out canvas (x)
    if (x>canvas.width-image.width) {
        x = canvas.width-image.width;
    }
    
    if (y>canvas.height-image.height) {
        y = canvas.height-image.height;
    }
    
        // draw it
    context.drawImage(image, x, y, image.width, image.height);
}

function showImage(event, imageLink) {
    // showImage from <imageLink>
    
    if (imageLink != '') {
        
        canvas = document.getElementById("folder_canvas");
        
        img = new Image();
        img.src = imageLink;
        
            // get mouse position on page with scroll offset
        mouseX = event.clientX + document.body.scrollLeft;
        mouseY = event.clientY + document.body.scrollTop;
        
            // draw on load (100px offset from head-menu in folder.html)
        img.onload = function() {
            drawImage(canvas, img, mouseX, mouseY-100);
        };
        
        img.onerror = function() {
            console.log("Image failed:",img.src);
        };
    }
}

window.onload = onLoad;