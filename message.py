#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

#協力廠商資訊
#ImagemapSendMessage(組圖訊息)
def imagemap_message():
    message = ImagemapSendMessage(
        base_url="http://140.125.94.23/IOT/bg.jpg", #[注意]圖片為超連結
        alt_text='最新的協力廠商',
        base_size=BaseSize(height=2000, width=2000),
        actions=[
            URIImagemapAction(
                #左上圖片廠商
                link_uri="https://tw.shop.com/search/%E5%AE%B6%E6%A8%82%E7%A6%8F", #[學生改]可以改網址
                area=ImagemapArea(
                    x=0, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #右上廠商
                link_uri="https://tw.shop.com/search/%E7%94%9F%E6%B4%BB%E5%B8%82%E9%9B%86",#[學生改]可以改網址
                area=ImagemapArea(
                    x=1000, y=0, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #左下
                link_uri="https://tw.shop.com/search/%E9%98%BF%E7%98%A6%E7%9A%AE%E9%9E%8B",#[學生改]可以改網址
                area=ImagemapArea(
                    x=0, y=1000, width=1000, height=1000
                )
            ),
            URIImagemapAction(
                #右下前半部 (雲科大)
                link_uri="https://www.yuntech.edu.tw/",
                area=ImagemapArea(
                    x=1000, y=1000, width=1000, height=500
                )
            ),
            URIImagemapAction(
                #右下後半部 (工管系)
                link_uri="https://www.iem.yuntech.edu.tw/",
                area=ImagemapArea(
                    x=1000, y=1500, width=1000, height=500
                )
            )
        ]
    )
    return message

#關於本企業
#TemplateSendMessage - ButtonsTemplate (按鈕介面訊息)
def buttons_message():
    message = TemplateSendMessage(
        alt_text='關於我們',
        template=ButtonsTemplate(
            thumbnail_image_url="https://www.yuntech.edu.tw/images/mainmenu/about/yuntech_logo.jpg",#[學生改]圖片為超連結必須提供網址
            title="雲寶寶公司", #[學生改]標頭自己改
            text="更加了解我們企業資訊",#[學生改]副標題可以自己改
            actions=[
                MessageTemplateAction(
                    label="認識雲科大", #[學生改]靜態標題
                    text="YunTech成立於1991年，為技職教育之高等學府，從創校、紮根....." #[學生改]使用者點選靜態標題的自動回復文字
                ),
                URITemplateAction(
                    label="雲科大首頁", #[學生改]你可以改成其他網站標題
                    uri="https://www.yuntech.edu.tw/index.php" #[學生改]可以改網址
                ),
                URITemplateAction(
                    label="雲科大工管首頁", #[學生改]你可以改成其他網站標題
                    uri="https://www.iem.yuntech.edu.tw/"  #[學生改]可以改網址
                )
            ]
        )
    )
    return message

#功能列表
def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='多欄位訊息展示',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.fengtay.com/upfiles/ADUpload/tw_index_pic2303371073.jpg', #[學生改]圖片超連結
                    title='研究發展與創新', #[學生改]標題
                    text='本企業重視研發,並設定產品開發中心與研發中心', #[學生改]副標題
                    actions=[
                        URITemplateAction(
                            label='產品開發中心',#[學生改]網站標題
                            uri='https://www.fengtay.com/chinese/07_innovations/01_development.aspx'#[學生改]網站網址
                        ),
                        URITemplateAction(
                            label='研發中心',#[學生改]網站標題
                            uri='https://www.fengtay.com/chinese/07_innovations/01_development.aspx?iid=3'#[學生改]網站網址
                        ),
                        MessageTemplateAction(
                            label='研發團隊介紹',#[學生改]標題
                            text='豐泰企業自2012年起積極投入先進製程技術研究，逐年增加研發投資金額，從早期的傳統製造發展至以技術領導生產的營運模式。' #[學生改]點選該標題時自動回復資訊
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.fengtay.com/upfiles/ADUpload/tw_link369220087.jpg',#[學生改]圖片超連結
                    title='知識管理專區', #[學生改]標題
                    text='此為歷年文件下載專區', #[學生改]副標題
                    actions=[
                        MessageTemplateAction(
                            label='關於此專區',#[學生改]標題
                            text='此為公司知識管理文件之下載區' #[學生改]點選該標題時自動回復資訊
                        ),
                        URITemplateAction(
                            label='2021文件下載',#[學生改]網站標題
                            uri='https://www.fengtay.com/chinese/04_ir/down.aspx?file_name=tw_procedure2691298701.pdf&file_url=../../upfiles/ADUpload/'#[學生改]網站網址
                        )
                        ,
                        URITemplateAction(
                            label='2020文件下載',#[學生改]網站標題
                            uri='https://www.fengtay.com/chinese/04_ir/down.aspx?file_name=tw_procedure2691298701.pdf&file_url=../../upfiles/ADUpload/' #[學生改]網站網址
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.fengtay.com/upfiles/ADUpload/tw_link424528342.jpg',#[學生改]圖片超連結
                    title='經營團隊', #[學生改]標題
                    text='豐泰企業以誠信守法的精神維持良好之公司治理，堅持營運透明、重視股東權益',#[學生改]網站標題
                    actions=[
                        MessageTemplateAction(
                            label='董事會資訊',#[學生改]標題
                            text='目前董事會成員共十三席，包含四席獨立董事及一席女性董事；董事中九席具產業經歷(其中六席為本公司所屬鞋類產業高階管理經歷、三席為大型製造業高階管理經歷)、三席具會計財務或企業經營管理專業背景、一席具法律專業背景，符合董事會多元化目標。' #[學生改]點選該標題時自動回復資訊
                        ),
                        URITemplateAction(
                            label='即時股價查詢',#[學生改]網站標題
                            uri='https://mis.twse.com.tw/stock/fibest.jsp?stock=9910' #[學生改]網站網址
                        )
                    ]
                )
            ]
        )
    )
    return message
#產品資訊
#TemplateSendMessage - ImageCarouselTemplate
def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='產品資訊',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://www.fanuctaiwan.com.tw/upload/Product/Class/F_201803011008JfP1W625.PNG", #[學生改]顯示圖片圖片連結網址
                    action=URITemplateAction(
                        label="CNC 機台系列產品", #[學生改]顯示圖片圖片標題
                        uri="https://www.fanuctaiwan.com.tw/product-fa.php?t=1"  #[學生改]點選圖片時的超連結
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.fanuctaiwan.com.tw/upload/Product/PHOTO/F_201804161323oJUqJD38.JPEG",#[學生改]顯示圖片圖片連結網址
                    action=URITemplateAction(
                        label="Servo Motor系列產品", #[學生改]顯示圖片圖片標題
                        uri="https://www.fanuctaiwan.com.tw/product-sort-1.php?i=69"  #[學生改]點選圖片時的超連結
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.fanuctaiwan.com.tw/upload/Product/PHOTO/F_2022042111456YZlAe25.PNG",#[學生改]顯示圖片圖片連結網址
                    action=URITemplateAction(
                        label="產品型錄", #[學生改]顯示圖片圖片標題
                        uri="https://www.fanuc.co.jp/en/product/catalog/pdf/robot/Roboti(C)-40.pdf" #[學生改]點選圖片時的超連結
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.fanuctaiwan.com.tw/upload/Product/F_201804101612lhtzG131.JPEG",#[學生改]顯示圖片圖片連結網址
                    action=URITemplateAction(
                        label="產品影片", #[學生改]顯示圖片圖片標題
                        uri="https://youtu.be/tP10GBmun2Y"  #[學生改]點選圖片時的超連結
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例