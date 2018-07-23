//var windowWidth = $(window).width();
//var windowSm = 767;
//if (windowWidth <= windowSm) {
//    //スマホに行う処理を書く
//    //ドロワーメニュー（スマホ版）
//    $(document).ready(function() {
//        $('.drawer').drawer();
//    });        
//} else {
//    //タブレット、PCに行う処理を書く
//    //ドロップダウンメニュー　グロナビ
//    $(function(){
//        $('#menu li').hover(function(){
//            $("ul:not(:animated)", this).slideDown();
//        }, function(){
//            $("ul.child",this).slideUp();
//        });
//    });    
//}

// ページトップへ戻るボタン
$(function() {
    var topBtn = $('.pagetop');
    topBtn.hide();
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            topBtn.fadeIn();
        } else {
            topBtn.fadeOut();
        }
    });
    topBtn.click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 500);
        return false;
    });
});

//コンテンツ項目　読み込みアニメーション
$(function(){
  $(".effect").each(function(){
    $(this).css("opacity","1");
    $(this).css("top","0px");
  });
});
