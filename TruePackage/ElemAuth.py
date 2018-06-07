class ElemAuth:
    def __init__(self):
        self.button_choose_location = "com.allgoritm.youla:id/setManualButton"
        self.city_from_list_moscow = '//*[@resource-id="com.allgoritm.youla:id/location_name_tv"][@index="0"]'
        self.label_my_profile = '//*[@class="android.widget.TextView"][@text="Мой профиль"]'  # auth profile screen
        self.button_phone_auth = '//*[@resource-id="com.allgoritm.youla:id/phone_number_textView"][@index="4"]'
        self.field_countrycode = '//*[@resource-id="com.allgoritm.youla:id/code_editText"][@index="0"]'
        self.field_phone_nmbr = '//*[@resource-id="com.allgoritm.youla:id/editText"][@index="1"]'
        self.button_confirm_nmbr = '//*[@resource-id="com.allgoritm.youla:id/submit_textView"][@index="2"]'
        self.field_sms_code = '//*[@resource-id="com.allgoritm.youla:id/editText"][@index="0"]'
        self.button_success_auth = '//*[@resource-id="com.allgoritm.youla:id/done_textView"][@index="5"]'
        self.label_sold = '//*[@resource-id="com.allgoritm.youla:id/titleTextView"][@index="0"]'
        self.label_anon_header = '//*[@class="android.widget.TextView"][@index="1"]'
