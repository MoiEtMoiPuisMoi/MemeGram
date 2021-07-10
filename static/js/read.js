var imageSection = document.querySelector(".instapost__image");
var likeHeart = document.querySelector(".like-heart");
var likeBtn = document.querySelector(".btn-like");
var commentInput = document.querySelector(".comment-input");
var commentSendBtn = document.querySelector(".btn-send-comment");
var ctrlLeft = document.querySelector(".ctrl-left");
var ctrlRight = document.querySelector(".ctrl-right");

commentInput.addEventListener("input", function (e) {
	if (e.target.value.length > 0) {
		commentSendBtn.setAttribute("disabled", "");
	} else {
		commentSendBtn.setAttribute("disabled", "disabled");
	}
});

likeBtn.addEventListener("click", function (e) {
	this.classList.toggle("dislike");
});

imageSection.addEventListener("dblclick", function (e) {
	likeHeart.classList.add("show");
	!likeBtn.classList.contains("dislike") && likeBtn.classList.add("dislike");
	setTimeout(function () {
		return likeHeart.classList.remove("show");
	}, 1000);
});

var nextIndex = 1;

document.onkeydown = function (event) {
    switch (event.keyCode) {
        case 39:
            location.reload();
            break;
    }
}

ctrlRight.addEventListener("click", chageImage(1));
ctrlLeft.addEventListener("click", chageImage(0));