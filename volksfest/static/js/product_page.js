$('a').click(function (event){
    var largeImageURL = $('img', this).attr("large-img-url");
    if (largeImageURL != '') {
        console.log(largeImageURL);
        var originalURL = $('#image-view-target').attr('src');
        console.log(originalURL);
        $('#image-view-target').attr('src',largeImageURL);
        $('.active').removeClass("active");
        $('img', this).addClass("active");
    }
    
})