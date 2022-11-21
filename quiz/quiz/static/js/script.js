
let active_button;
let price_modal;
let score_cookie_name = 'score'
let score_cookie_val;

var users = document.getElementsByClassName("user__item-score");




score_cookie_val = Cookies.get(score_cookie_name);
console.log("куки: " + score_cookie_val);
if (score_cookie_val == undefined) {
    score_cookie_val = '0 0 0 0 0 0';
    Cookies.set(score_cookie_name, score_cookie_val);
    console.log("Куки созданы");
}
else {
    var splint_str = score_cookie_val.split(' ');
    for (var i = 0, len = users.length; i < len; i++) {
        if (splint_str[i] == undefined) {
            users[i].innerHTML = 0
        } else {
            users[i].innerHTML = splint_str[i];
        }
    }
}


$('.modal_show_answer').click(function (event) {
    console.log('modal_show_answer active')
    $('.modal_show_answer').css('display', 'none');
    $('.show_answer-text').css('display', 'block');
    $('.instuction-modal').css('display', 'block');
    $('.user__item-click').addClass('show');
    active_button.css('display', 'none');
})


$('.options').click(function () {
    $('.user-row').addClass('noshow');
})

$(".modal").on("hidden.bs.modal", function () {
    $('.user__item-click').removeClass('show');
    $('.modal_show_answer').css('display', 'block');
    $('.show_answer-text').css('display', 'none');
    $('.instuction-modal').css('display', 'none');
    active_button = undefined;
    if ($('.user-row').hasClass('noshow')) {
        $('.user-row').removeClass('noshow');
    }
});



$('.button_open_modal').click(function (e) {
    active_button = $(this);
    price_modal = Number(this.innerHTML);
})

$('.user__item-click').click(function (e) {
    $('.modal').modal('hide');
    this.closest('.user__item').querySelector('.user__item-score').innerHTML = Number(this.closest('.user__item').querySelector('.user__item-score').innerHTML) + price_modal;
    var cookie_val = '';
    for (var i = 0, len = users.length; i < len; i++) {
        cookie_val = cookie_val + users[i].innerHTML + ' ';
    }
    score_cookie_val = cookie_val;
    Cookies.set(score_cookie_name, score_cookie_val);
})



$('#restart_score').click(function () {
    for (var i = 0, len = users.length; i < len; i++) {
        users[i].innerHTML = 0;
    }
    score_cookie_val = '0 0 0 0 0 0';
    Cookies.set(score_cookie_name, score_cookie_val);
    console.log("Очки сброшены");
});