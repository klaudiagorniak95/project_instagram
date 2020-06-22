from tests.helpers.utils import TestData

class LoginPageLocators():
    LOGIN_WITH_PASSWORD_BUTTON = 'com.instagram.android:id/log_in_button'
    LOGIN_INPUT = 'com.instagram.android:id/login_username'
    PASSWORD_INPUT = 'com.instagram.android:id/password'
    LOGIN_BUTTON = 'com.instagram.android:id/next_button'

class Navigation():
    HOME_BUTTON = '//android.widget.FrameLayout[@content-desc="Szukaj i poznaj"]/android.widget.ImageView'
    SEARCH_BUTTON = '//android.widget.FrameLayout[@content-desc="Szukaj i poznaj"]/android.widget.ImageView'
    CAMERA_BUTTON = '//android.widget.FrameLayout[@content-desc="Aparat"]/android.widget.ImageView'
    ACTIVITY_BUTTON = '//android.widget.FrameLayout[@content-desc="Aktywność"]/android.widget.ImageView'
    PROFILE_BUTTON = '//android.widget.FrameLayout[@content-desc="Profil"]/android.widget.ImageView'

class Profile():
    ID = 'com.instagram.android:id/title_view'
    POSTS_COUNT = 'com.instagram.android:id/row_profile_header_textview_post_count'

class Search():
    SEARCH_INPUT = 'com.instagram.android:id/action_bar_search_edit_text'
    SEARCH_RESULT_KDUSIA = '//*[@text="k._dusia"]'

class TestedPage():
    FIRST_PHOTO_KDUSIA = '//android.widget.ImageView[@content-desc="Autor zdjęcia: Klaudia, wiersz: 1, kolumna: 1"]'
    LIKE_BUTTON = 'com.instagram.android:id/row_feed_button_like'
    COMMENT_BUTTON = 'com.instagram.android:id/row_feed_button_comment'
    COMMENT_INPUT = 'com.instagram.android:id/layout_comment_thread_edittext'
    COMMENT_POST_BUTTON = 'com.instagram.android:id/layout_comment_thread_post_button'
    COMMENT_CONTENT = f'//*[@text="{TestData.login} {TestData.comment_content}"]'
    COMMENT_ARRAY = 'android.widget.TextView'
    FOLLOWERS_COUNT = 'com.instagram.android:id/row_profile_header_textview_followers_count'
    FOLLOW_ACCOUNT_BUTTON = '//android.widget.TextView[@text="Obserwuj"]'
    FOLLOWERS_LIST_MY_LOGIN = f'//android.widget.TextView[@text="{TestData.login}"]'
    SEND_MESSAGE_BUTTON = '//android.widget.TextView[@text="Wiadomość"]'
    EDIT_TEXT_INPUT = 'com.instagram.android:id/row_thread_composer_edittext'
    SEND_BUTTON = 'com.instagram.android:id/row_thread_composer_button_send'
    SENT_TEXT = 'com.instagram.android:id/direct_text_message_text_view'

class Camera():
    CAMERA_BUTTON_COOR = (538, 1702)
    SHUTTER_BUTTON = 'com.instagram.android:id/shutter_button'
    ADD_FILTER = '//android.widget.RadioButton[@content-desc="Moon"]'
    EDIT_PHOTO_COOR = (799, 1702)
    CROP_IMAGE = '//android.widget.RadioButton[@content-desc="Dostosuj"]'
    CROP_READY_BUTTON = 'com.instagram.android:id/button_accept_adjust'
    NEXT_BUTTON = 'com.instagram.android:id/next_button_textview'
    ADD_CAPTION_INPUT = 'com.instagram.android:id/caption_text_view'

