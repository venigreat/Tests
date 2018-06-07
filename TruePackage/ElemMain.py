
class ElemMain:
    def __init__(self):
        self.button_profile = '//*[@class="android.widget.FrameLayout"][@index="4"]'
        self.button_home = '//*[@content-desc="Вкладка Главная"]'
        self.button_add = '//*[@class="android.widget.RelativeLayout"][@index="2"]'
        self.category_stuff = '//*[@resource-id="com.allgoritm.youla:id/category_container"][@index="3"]'

        self.icon_photo = '//*[@class="android.widget.FrameLayout"][@index="0"][@content-desc="Добавить фото"]'
        self.button_chose_from_gallery = '//*[@class="android.widget.LinearLayout"][@index="1"]'
        self.permission_images_allow = \
            '//*[@resource-id="com.android.packageinstaller:id/permission_allow_button"][@index="1"]'
        self.first_image_in_gallery = \
            '//*[@resource-id="com.allgoritm.youla:id/check_view"][@class="android.view.View"][@index="1"]'
        self.button_apply_images = '//*[@resource-id="com.allgoritm.youla:id/button_apply"][@index="1"]'

        self.field_header_ad = '//*[@resource-id="com.allgoritm.youla:id/title_editText"][@index="1"]'

        self.field_cost = '//*[@resource-id="com.allgoritm.youla:id/price_et"][@index="1"]'
        self.button_choose_category = '//*[@resource-id="com.allgoritm.youla:id/category_tv"][@index="1"]'
        self.choose_subcategory = '//*[@resource-id="com.allgoritm.youla:id/category_container"][@index="%d"]'

        self.button_done = '//*[@resource-id="com.allgoritm.youla:id/action_done"][@index="0"]'
        self.button_cancel_promotion = '//*[@class="android.widget.ImageButton"][@index="0"]'
        self.button_promo_swipe = '//*[@resource-id="com.allgoritm.youla:id/closeWizardButton"][@index="2"]'

        self.ad_on_main = '//*[@class="android.widget.FrameLayout"][@index="2"]'
        self.ad_on_filter = '//*[@class="android.widget.FrameLayout"][@index="0"]'
        self.linear_clickable_ad = '//*[@resource-id="com.allgoritm.youla:id/root_linearLayout"]'
        self.promoted_clickable_ad = '//*[@resource-id="com.allgoritm.youla:id/contentWrapper"]'

        self.frame_ad = '//*[@class="android.widget.FrameLayout"][@index="0"]'
        self.relative_ad = '//*[@resource-id="com.allgoritm.youla:id/root_relativeLayout"]'

        self.button_profile_back = '//*[@class="android.widget.ImageButton"][@index="0"]'
        self.button_product_promotion = '//*[@resource-id="com.allgoritm.youla:id/promoteButton"][@index="5"]'

        self.button_promotion_premium = '//*[@resource-id="com.allgoritm.youla:id/typePlugInButton"][@index="6"]'
        self.button_promotion_x5 = '//*[@resource-id="com.allgoritm.youla:id/buyPromoteButton"][@index="2"]'
        self.button_promotion_pay = '//*[@resource-id="com.allgoritm.youla:id/payButton"][@index="2"]'
        self.button_webview_card_pay = '//*[@class="android.widget.Button"][@index="0"]'
        self.button_promotion_success = '//*[@resource-id="com.allgoritm.youla:id/show_product_btn"][@index="3"]'

        self.avito_first_ad = '//*[@resource-id="com.avito.android:id/advert_grid_root"][@index="2"]'

        self.button_filtres_linear = '//*[@class="android.support.v7.widget.LinearLayoutCompat"][@index="2"]'
        self.button_filtres_text = '//*[@class="android.widget.TextView"][@index="0"]'
        self.chbox_filter_BS = '//*[@resource-id="com.allgoritm.youla:id/filterPaymentSwitch"][@index="1"]'
        self.chbox_filter_delivery = '//*[@resource-id="com.allgoritm.youla:id/filterDeliverySwitch"][@index="1"]'
        self.button_filter_accept = '//*[@resource-id="com.allgoritm.youla:id/filters_accept"][@index="0"]'
