window.onload = function(){
    const Images = document.querySelectorAll(".artThumb")
 
    for(var i=0;i<Images.length;i++){
        
        Images[i].addEventListener('mouseover',function (event){

            let Img = document.createElement('img')
            if (event.target==Images[0]){
                Img.src="images/art/thumbs/05030.jpg"
            }else if(event.target==Images[1]){
                Img.src="images/art/thumbs/120010.jpg"
            }else if(event.target==Images[2]){
                Img.src="images/art/thumbs/07020.jpg"
            }else if(event.target==Images[3]){
                Img.src="images/art/13030.jpg"
            }else{
                Img.src="images/art/06010.jpg"
            }

            let new_span = document.createElement('span')
        
            Img.classList.add('bigImg');
            new_span.appendChild(Img)
            event.target.parentNode.appendChild(new_span)
        });
        Images[i].addEventListener('mouseleave',popdown);
    }

    function popdown(){
        const bigImg_find = document.querySelectorAll("span");
        bigImg_find.forEach(element => {
            element.remove()
        })
    }

}

