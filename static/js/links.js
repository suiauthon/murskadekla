function links_setup() {
    $('#instagram_footer').click(function () {
      this.blur();
     });

    $('#mail_footer').click(function () {
      this.blur();
     });

    $('#youtube_footer').click(function () {
      this.blur();
     });

    $('#twitter_footer').click(function () {
      this.blur();
     });

    $('#facebook_footer').click(function () {
      this.blur();
     });

    $('#facebook_footer').attr('href','https://www.facebook.com/murskadekla');
    $('#twitter_footer').attr('href','https://twitter.com/murskadekla');
    $('#youtube_footer').attr('href','https://www.youtube.com/channel/UCfNsn5DSPArA8Wy3rtljoIQ');
    $('#instagram_footer').attr('href','https://www.instagram.com/murskadekla/');
    $('#mail_footer').attr('href','mailto:info@murskadekla.com');
}