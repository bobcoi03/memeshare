function getMoreMemes(){
	console.log("get more memes funct is called")
}

function timeElapsed(startTime,endTime) {
	var timeDiff = endTime - startTime
	timeDiff /= 1000

	return Math.round(timeDiff)
}

document.addEventListener('DOMContentLoaded', function(e) {
    document.addEventListener('scroll', function(e) {

        let documentHeight = document.body.scrollHeight;
        let currentScroll = window.scrollY + window.innerHeight;
        // When the user is [modifier]px from the bottom, fire the event.
        let modifier = 1; 
        if(currentScroll + modifier > documentHeight) {
            getMoreMemes()
        }
    })
})
