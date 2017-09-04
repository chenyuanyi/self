# -*- coding: utf-8 -*-


if __name__ == '__main__':
    from web import app
    tmp_app = app.test_client()
    # print(tmp_app.get('/api/admin/login?account=admin&password=123456').data)
    # print(tmp_app.get('/api/admin/system/user_manage').data)
    # print(tmp_app.get('/api/business/newbie_guide').data)
    # print(tmp_app.get('/api/business/newbie_guide_info?type=newbie_guide_1').data)
    # print (tmp_app.get('/api/business/news?page_now=1&page_size=10&type=selected').data)
    # print (tmp_app.get('/api/business/discuss_data?page_now=1&page_size=10&mark=admin3_mark').data)
    # print(tmp_app.post('/api/business/discuss_star?discuss_id=3').data)
    # print (tmp_app.get('/api/business/doujin_info?doujin_id=6').data)
    # print(tmp_app.get('/api/business/game_strategy_info?game_strategy_id=8').data)
    # print(tmp_app.get('/api/business/news_info?dynamic_teletext_id=6').data)
    # print(tmp_app.post('/api/business/like_plus?doujin_id=3').data)
    # print(tmp_app.post('/api/business/watch_plus?doujin_id=3').data)


